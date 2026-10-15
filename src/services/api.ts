export interface HeroProfile {
  id: number;
  hero_name: string;
  level: number;
  xp: number;
  dungeon_floor: number;
  passed_problems: string[];
  token?: string;
  created_at?: string;
}

export interface PassedProblemsResponse {
  hero_name: string;
  passed_problems: string[];
  total_passed: number;
}

const API_BASE = '/api/v1';

function getHeaders(token?: string | null): Record<string, string> {
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
  };
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
    headers['X-Hero-Token'] = token;
  }
  return headers;
}

export async function apiSignUp(heroName: string, secretIncantation: string): Promise<HeroProfile> {
  const res = await fetch(`${API_BASE}/auth/signup`, {
    method: 'POST',
    headers: getHeaders(),
    body: JSON.stringify({
      hero_name: heroName,
      secret_incantation: secretIncantation,
    }),
  });

  const data = await res.json();
  if (!res.ok) {
    throw new Error(data.detail || 'Failed to summon hero to the guild');
  }
  return data;
}

export async function apiLogin(heroName: string, secretIncantation: string): Promise<HeroProfile> {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: 'POST',
    headers: getHeaders(),
    body: JSON.stringify({
      hero_name: heroName,
      secret_incantation: secretIncantation,
    }),
  });

  const data = await res.json();
  if (!res.ok) {
    throw new Error(data.detail || 'The dungeon doors remain barred. Invalid credentials');
  }
  return data;
}

export async function apiGetMe(token: string): Promise<HeroProfile> {
  const res = await fetch(`${API_BASE}/auth/me`, {
    method: 'GET',
    headers: getHeaders(token),
  });

  const data = await res.json();
  if (!res.ok) {
    throw new Error(data.detail || 'Failed to fetch hero profile');
  }
  return data;
}

export async function apiMarkProblemPassed(token: string, problemId: string): Promise<PassedProblemsResponse> {
  const res = await fetch(`${API_BASE}/auth/passed-problems`, {
    method: 'POST',
    headers: getHeaders(token),
    body: JSON.stringify({ problem_id: problemId }),
  });

  const data = await res.json();
  if (!res.ok) {
    throw new Error(data.detail || 'Failed to mark problem as passed');
  }
  return data;
}

export async function apiUnmarkProblemPassed(token: string, problemId: string): Promise<PassedProblemsResponse> {
  const res = await fetch(`${API_BASE}/auth/passed-problems/${encodeURIComponent(problemId)}`, {
    method: 'DELETE',
    headers: getHeaders(token),
  });

  const data = await res.json();
  if (!res.ok) {
    throw new Error(data.detail || 'Failed to unmark problem');
  }
  return data;
}

export async function apiRecordSubmission(payload: {
  problem_id: string;
  language: string;
  code: string;
  status: string;
  tests_passed: number;
  total_tests: number;
  execution_time_ms?: number;
}): Promise<any> {
  try {
    const res = await fetch(`${API_BASE}/submissions`, {
      method: 'POST',
      headers: getHeaders(),
      body: JSON.stringify(payload),
    });
    return await res.json();
  } catch (err) {
    console.warn('Submission recording failed in background:', err);
    return null;
  }
}

export interface DungeonRunPayload {
  wing_id: string;
  current_floor: number;
  max_floor_reached?: number;
  status?: string;
  run_catalog: any[];
  current_problem_id: string;
  code?: string;
  language?: string;
  hp?: number;
  max_hp?: number;
  gold?: number;
  potions?: number;
}

export async function apiSaveDungeonRun(token: string | null, payload: DungeonRunPayload): Promise<any> {
  if (!token) return null;
  try {
    const res = await fetch(`${API_BASE}/dungeon/runs`, {
      method: 'POST',
      headers: getHeaders(token),
      body: JSON.stringify(payload),
    });
    if (!res.ok) return null;
    return await res.json();
  } catch (err) {
    console.warn('Failed to sync dungeon run to database:', err);
    return null;
  }
}

export async function apiGetActiveRuns(token: string | null): Promise<any[]> {
  if (!token) return [];
  try {
    const res = await fetch(`${API_BASE}/dungeon/runs`, {
      method: 'GET',
      headers: getHeaders(token),
    });
    if (!res.ok) return [];
    return await res.json();
  } catch (err) {
    console.warn('Failed to fetch active runs from database:', err);
    return [];
  }
}

export async function apiAbandonDungeonRun(token: string | null, wingId: string): Promise<any> {
  if (!token) return null;
  try {
    const res = await fetch(`${API_BASE}/dungeon/runs/${encodeURIComponent(wingId)}/abandon`, {
      method: 'POST',
      headers: getHeaders(token),
    });
    if (!res.ok) return null;
    return await res.json();
  } catch (err) {
    console.warn('Failed to abandon dungeon run on database:', err);
    return null;
  }
}

