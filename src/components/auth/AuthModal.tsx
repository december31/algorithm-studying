import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useAuthStore } from '../../store/useAuthStore';
import { X, Shield, KeyRound, Sparkles, UserCheck, Eye, EyeOff, CheckCircle2, RotateCcw } from 'lucide-react';

export const AuthModal: React.FC = () => {
  const {
    isAuthModalOpen,
    authModalMode,
    closeAuthModal,
    openAuthModal,
    hero,
    isAuthenticated,
    signUp,
    login,
    logout,
    isLoading,
    errorMessage,
    hidePassedProblems,
    toggleHidePassed,
    unmarkProblemConquered,
  } = useAuthStore();

  const [heroName, setHeroName] = useState('');
  const [secretIncantation, setSecretIncantation] = useState('');
  const [showSpell, setShowSpell] = useState(false);

  if (!isAuthModalOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!heroName.trim() || !secretIncantation.trim()) return;

    if (authModalMode === 'signup') {
      await signUp(heroName, secretIncantation);
    } else {
      await login(heroName, secretIncantation);
    }
  };

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm">
        <motion.div
          initial={{ opacity: 0, scale: 0.95, y: 15 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 15 }}
          className="w-full max-w-md bg-dungeon-darker border border-amber-500/40 rounded-2xl shadow-2xl overflow-hidden text-slate-100 flex flex-col max-h-[90vh]"
        >
          {/* Header Banner */}
          <div className="relative bg-gradient-to-r from-amber-950/80 via-slate-900 to-rose-950/80 border-b border-amber-600/30 p-4 sm:p-5 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-xl shadow-inner">
                🧙‍♂️
              </div>
              <div>
                <h3 className="font-pixel text-sm sm:text-base text-amber-300 tracking-wide">
                  {isAuthenticated ? 'HERO CITADEL' : 'GUILD REGISTRY'}
                </h3>
                <p className="text-xs text-slate-400">
                  {isAuthenticated
                    ? 'Your legendary journey & conquered trials'
                    : 'No blood oaths or OTP scrolls needed! Just a name & spell.'}
                </p>
              </div>
            </div>
            <button
              onClick={closeAuthModal}
              className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800/60 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          <div className="p-5 overflow-y-auto space-y-5">
            {/* Authenticated Hero View */}
            {isAuthenticated && hero ? (
              <div className="space-y-4">
                {/* Hero Badge */}
                <div className="p-4 rounded-xl bg-slate-900/90 border border-amber-500/30 flex items-center justify-between shadow-inner">
                  <div className="flex items-center gap-3">
                    <div className="w-12 h-12 rounded-full bg-amber-500/20 border-2 border-amber-400 flex items-center justify-center text-2xl shadow-lg">
                      ⚔️
                    </div>
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="font-bold text-slate-100 text-base">{hero.hero_name}</span>
                        <span className="px-2 py-0.5 rounded text-[10px] font-pixel bg-amber-500/20 text-amber-300 border border-amber-500/30">
                          LVL {hero.level}
                        </span>
                      </div>
                      <p className="text-xs font-mono text-slate-400">XP: {hero.xp} pts</p>
                    </div>
                  </div>
                  <button
                    onClick={logout}
                    className="px-3 py-1.5 rounded-lg text-xs font-pixel bg-rose-950/60 text-rose-400 border border-rose-800/40 hover:bg-rose-900/80 transition-colors"
                  >
                    DEPART
                  </button>
                </div>

                {/* Hide Passed Problems Filter Setting */}
                <div className="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800 flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <Shield className="w-5 h-5 text-sky-400" />
                    <div>
                      <div className="text-xs font-bold text-slate-200">Hide Conquered Problems</div>
                      <div className="text-[11px] text-slate-400">Skip challenges you already solved in dungeon runs</div>
                    </div>
                  </div>
                  <button
                    onClick={toggleHidePassed}
                    className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
                      hidePassedProblems ? 'bg-sky-600' : 'bg-slate-700'
                    }`}
                  >
                    <span
                      className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                        hidePassedProblems ? 'translate-x-6' : 'translate-x-1'
                      }`}
                    />
                  </button>
                </div>

                {/* Conquered Problems List */}
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-pixel text-xs text-amber-400 flex items-center gap-1.5">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                      CONQUERED CHALLENGES ({hero.passed_problems?.length || 0})
                    </span>
                  </div>

                  {hero.passed_problems && hero.passed_problems.length > 0 ? (
                    <div className="max-h-48 overflow-y-auto space-y-1.5 pr-1">
                      {hero.passed_problems.map((probId) => (
                        <div
                          key={probId}
                          className="px-3 py-2 rounded-lg bg-slate-900/50 border border-slate-800 flex items-center justify-between text-xs"
                        >
                          <span className="font-mono text-emerald-400">{probId}</span>
                          <button
                            onClick={() => unmarkProblemConquered(probId)}
                            className="text-[10px] text-slate-500 hover:text-amber-400 flex items-center gap-1 transition-colors"
                            title="Reset so this problem can appear again"
                          >
                            <RotateCcw className="w-3 h-3" />
                            <span>Replay</span>
                          </button>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <div className="p-4 rounded-xl bg-slate-900/30 border border-dashed border-slate-800 text-center text-xs text-slate-500">
                      No dungeon trials conquered yet. Attack monsters and pass all tests to claim victory!
                    </div>
                  )}
                </div>
              </div>
            ) : (
              /* Non-authenticated Form (Sign up / Login) */
              <div>
                {/* Mode Selector Tabs */}
                <div className="grid grid-cols-2 p-1 bg-slate-900 rounded-xl mb-4 border border-slate-800">
                  <button
                    type="button"
                    onClick={() => openAuthModal('signup')}
                    className={`py-2 text-xs font-pixel rounded-lg transition-colors flex items-center justify-center gap-1.5 ${
                      authModalMode === 'signup'
                        ? 'bg-amber-600 text-slate-950 font-bold shadow'
                        : 'text-slate-400 hover:text-white'
                    }`}
                  >
                    <Sparkles className="w-3.5 h-3.5" />
                    JOIN GUILD
                  </button>
                  <button
                    type="button"
                    onClick={() => openAuthModal('login')}
                    className={`py-2 text-xs font-pixel rounded-lg transition-colors flex items-center justify-center gap-1.5 ${
                      authModalMode === 'login'
                        ? 'bg-amber-600 text-slate-950 font-bold shadow'
                        : 'text-slate-400 hover:text-white'
                    }`}
                  >
                    <KeyRound className="w-3.5 h-3.5" />
                    HERO RETURN
                  </button>
                </div>

                {/* Error Banner */}
                {errorMessage && (
                  <div className="p-3 mb-4 rounded-xl bg-rose-950/60 border border-rose-600/50 text-xs text-rose-300">
                    ⚠️ {errorMessage}
                  </div>
                )}

                <form onSubmit={handleSubmit} className="space-y-4">
                  {/* Hero Name / Call-Sign Field */}
                  <div>
                    <label className="block text-xs font-pixel text-amber-400/90 mb-1.5">
                      ADVENTURER CALL-SIGN (PLAYER NAME)
                    </label>
                    <input
                      type="text"
                      required
                      placeholder="e.g. GandalfTheCode, ByteKnight"
                      value={heroName}
                      onChange={(e) => setHeroName(e.target.value)}
                      className="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-slate-100 placeholder-slate-500 text-sm focus:outline-none focus:border-amber-400 focus:ring-1 focus:ring-amber-400 font-mono"
                    />
                  </div>

                  {/* Secret Incantation / Password Field */}
                  <div>
                    <label className="block text-xs font-pixel text-amber-400/90 mb-1.5">
                      SECRET INCANTATION (PASSWORD)
                    </label>
                    <div className="relative">
                      <input
                        type={showSpell ? 'text' : 'password'}
                        required
                        placeholder="Your secret magical passphrase"
                        value={secretIncantation}
                        onChange={(e) => setSecretIncantation(e.target.value)}
                        className="w-full pl-3.5 pr-10 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-slate-100 placeholder-slate-500 text-sm focus:outline-none focus:border-amber-400 focus:ring-1 focus:ring-amber-400 font-mono"
                      />
                      <button
                        type="button"
                        onClick={() => setShowSpell(!showSpell)}
                        className="absolute right-3 top-2.5 text-slate-500 hover:text-slate-300"
                        title={showSpell ? 'Conceal spell' : 'Reveal spell'}
                      >
                        {showSpell ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                      </button>
                    </div>
                  </div>

                  {/* Submit Button */}
                  <button
                    type="submit"
                    disabled={isLoading}
                    className="w-full py-3 rounded-xl font-pixel text-xs text-slate-950 bg-gradient-to-r from-amber-500 to-amber-400 hover:from-amber-400 hover:to-amber-300 font-bold shadow-lg shadow-amber-500/20 transition-all flex items-center justify-center gap-2 mt-2 disabled:opacity-50"
                  >
                    {isLoading ? (
                      <span className="flex items-center gap-2">
                        <Sparkles className="w-4 h-4 animate-spin" />
                        COMMUNING WITH REALM...
                      </span>
                    ) : authModalMode === 'signup' ? (
                      <span>⚔️ FORGE ADVENTURER IDENTITY</span>
                    ) : (
                      <span>🗝️ UNLOCK CITADEL GATES</span>
                    )}
                  </button>
                </form>
              </div>
            )}
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
};
