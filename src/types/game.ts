export type Difficulty = 'easy' | 'medium' | 'hard';

export interface Monster {
  id: string;
  name: string;
  title: string;
  maxHp: number;
  hp: number;
  sprite: 'slime' | 'goblin' | 'skeleton' | 'gargoyle' | 'wraith' | 'treant' | 'spider' | 'dragon' | 'lich' | 'orc' | 'golem';
  color: string;
  attackName: string;
  attackPower: number;
  defeatQuote: string;
}

export interface PlayerStats {
  maxHp: number; // default 100
  hp: number; // default 100
  shield: number; // active shield % (e.g. 0 to 75%)
  shieldPassedCount: number; // number of passed test cases granting shield
  gold: number;
  level: number;
  xp: number;
  potions: number;
  totalSolved: number;
}

export type DungeonTopic = 
  | 'data-structures'
  | 'backtracking'
  | 'graphs'
  | 'binary-search-greedy'
  | 'bit-manipulation';

export interface DungeonWing {
  id: DungeonTopic;
  name: string;
  subtitle: string;
  description: string;
  icon: string;
  floorsCount: number;
  unlocked: boolean;
  color: string;
}

export interface CombatLog {
  id: string;
  sender: 'hero' | 'monster' | 'system';
  message: string;
  type: 'damage' | 'heal' | 'info' | 'critical' | 'victory' | 'defeat';
  timestamp: number;
}

export type GameScreen = 'map' | 'battle' | 'shop' | 'victory' | 'gameover';
