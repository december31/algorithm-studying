import { create } from 'zustand';
import {
  HeroProfile,
  apiGetMe,
  apiLogin,
  apiMarkProblemPassed,
  apiSignUp,
  apiUnmarkProblemPassed,
} from '../services/api';

const TOKEN_KEY = 'algo_dungeon_hero_token';
const HIDE_PASSED_KEY = 'algo_dungeon_hide_passed';

interface AuthState {
  hero: HeroProfile | null;
  token: string | null;
  isAuthenticated: boolean;
  hidePassedProblems: boolean;
  isAuthModalOpen: boolean;
  authModalMode: 'signup' | 'login';
  isLoading: boolean;
  errorMessage: string | null;

  // Actions
  openAuthModal: (mode?: 'signup' | 'login') => void;
  closeAuthModal: () => void;
  signUp: (heroName: string, secretIncantation: string) => Promise<boolean>;
  login: (heroName: string, secretIncantation: string) => Promise<boolean>;
  logout: () => void;
  checkAuth: () => Promise<void>;
  markProblemConquered: (problemId: string) => Promise<void>;
  unmarkProblemConquered: (problemId: string) => Promise<void>;
  toggleHidePassed: () => void;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  hero: null,
  token: typeof window !== 'undefined' ? localStorage.getItem(TOKEN_KEY) : null,
  isAuthenticated: false,
  hidePassedProblems: typeof window !== 'undefined' ? localStorage.getItem(HIDE_PASSED_KEY) !== 'false' : true,
  isAuthModalOpen: false,
  authModalMode: 'signup',
  isLoading: false,
  errorMessage: null,

  openAuthModal: (mode = 'signup') => {
    set({ isAuthModalOpen: true, authModalMode: mode, errorMessage: null });
  },

  closeAuthModal: () => {
    set({ isAuthModalOpen: false, errorMessage: null });
  },

  signUp: async (heroName, secretIncantation) => {
    set({ isLoading: true, errorMessage: null });
    try {
      const profile = await apiSignUp(heroName, secretIncantation);
      if (profile.token) {
        localStorage.setItem(TOKEN_KEY, profile.token);
      }
      set({
        hero: profile,
        token: profile.token || null,
        isAuthenticated: true,
        isLoading: false,
        isAuthModalOpen: false,
      });
      import('./useGameStore').then(({ useGameStore }) => {
        useGameStore.getState().syncActiveRunsFromDatabase();
      }).catch(() => {});
      return true;
    } catch (err: any) {
      set({ isLoading: false, errorMessage: err.message || 'Summoning failed' });
      return false;
    }
  },

  login: async (heroName, secretIncantation) => {
    set({ isLoading: true, errorMessage: null });
    try {
      const profile = await apiLogin(heroName, secretIncantation);
      if (profile.token) {
        localStorage.setItem(TOKEN_KEY, profile.token);
      }
      set({
        hero: profile,
        token: profile.token || null,
        isAuthenticated: true,
        isLoading: false,
        isAuthModalOpen: false,
      });
      import('./useGameStore').then(({ useGameStore }) => {
        useGameStore.getState().syncActiveRunsFromDatabase();
      }).catch(() => {});
      return true;
    } catch (err: any) {
      set({ isLoading: false, errorMessage: err.message || 'Login failed' });
      return false;
    }
  },

  logout: () => {
    localStorage.removeItem(TOKEN_KEY);
    set({
      hero: null,
      token: null,
      isAuthenticated: false,
      isAuthModalOpen: false,
      errorMessage: null,
    });
  },

  checkAuth: async () => {
    const token = get().token;
    if (!token) return;

    try {
      const profile = await apiGetMe(token);
      set({
        hero: profile,
        isAuthenticated: true,
      });
      import('./useGameStore').then(({ useGameStore }) => {
        useGameStore.getState().syncActiveRunsFromDatabase();
      }).catch(() => {});
    } catch (err) {
      console.warn('Hero token expired or invalid:', err);
      localStorage.removeItem(TOKEN_KEY);
      set({ hero: null, token: null, isAuthenticated: false });
    }
  },

  markProblemConquered: async (problemId: string) => {
    const { token, hero } = get();
    if (!hero) return;

    // Optimistically update local passed list
    const currentPassed = new Set(hero.passed_problems || []);
    if (!currentPassed.has(problemId)) {
      currentPassed.add(problemId);
      const updatedPassed = Array.from(currentPassed);
      set({
        hero: {
          ...hero,
          passed_problems: updatedPassed,
          xp: hero.xp + 100,
          level: 1 + Math.floor((hero.xp + 100) / 300),
        },
      });
    }

    if (token) {
      try {
        const res = await apiMarkProblemPassed(token, problemId);
        if (res && res.passed_problems) {
          set((s) => (s.hero ? { hero: { ...s.hero, passed_problems: res.passed_problems } } : {}));
        }
      } catch (err) {
        console.warn('Failed to sync conquered problem to server:', err);
      }
    }
  },

  unmarkProblemConquered: async (problemId: string) => {
    const { token, hero } = get();
    if (!hero) return;

    const filtered = (hero.passed_problems || []).filter((id) => id !== problemId);
    set({
      hero: {
        ...hero,
        passed_problems: filtered,
      },
    });

    if (token) {
      try {
        await apiUnmarkProblemPassed(token, problemId);
      } catch (err) {
        console.warn('Failed to unmark conquered problem on server:', err);
      }
    }
  },

  toggleHidePassed: () => {
    const current = get().hidePassedProblems;
    const next = !current;
    localStorage.setItem(HIDE_PASSED_KEY, String(next));
    set({ hidePassedProblems: next });
  },
}));
