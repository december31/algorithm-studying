import React from 'react';
import { useGameStore } from '../../store/useGameStore';
import { motion } from 'framer-motion';
import { ShoppingBag, ArrowLeft, Heart, Sparkles } from 'lucide-react';
import { sfx } from '../../engine/sfx';

export const ShopModal: React.FC = () => {
  const { stats, buyPotion, setScreen } = useGameStore();

  const buyHpUpgrade = () => {
    const cost = 100;
    if (stats.gold >= cost) {
      sfx.playCoin();
      useGameStore.setState((s) => ({
        stats: {
          ...s.stats,
          gold: s.stats.gold - cost,
          maxHp: s.stats.maxHp + 25,
          hp: s.stats.hp + 25,
        },
      }));
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-md p-4">
      <motion.div
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        className="max-w-md w-full bg-dungeon-darkest border-2 border-amber-500 rounded-2xl p-6 shadow-[0_0_50px_rgba(245,158,11,0.3)] relative"
      >
        {/* Header */}
        <div className="flex items-center justify-between pb-4 border-b border-slate-800 mb-6">
          <div className="flex items-center gap-2">
            <ShoppingBag className="w-6 h-6 text-amber-400" />
            <h2 className="font-pixel text-base text-amber-400">DUNGEON SHOP</h2>
          </div>
          <div className="font-pixel text-xs text-amber-300 bg-amber-950/70 border border-amber-600/50 px-3 py-1 rounded-lg">
            💰 {stats.gold} GOLD
          </div>
        </div>

        {/* Shop Items List */}
        <div className="space-y-4 mb-6">
          {/* Health Potion */}
          <div className="p-4 rounded-xl bg-dungeon-card border border-slate-800 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <span className="text-3xl">🧪</span>
              <div>
                <div className="font-pixel text-xs text-slate-200">HEALTH POTION</div>
                <div className="text-[11px] font-mono text-slate-400">Restores +35 HP during battle</div>
              </div>
            </div>
            <button
              onClick={buyPotion}
              disabled={stats.gold < 40}
              className="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-pixel text-xs font-bold disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
            >
              40 💰
            </button>
          </div>

          {/* Max HP Upgrade */}
          <div className="p-4 rounded-xl bg-dungeon-card border border-slate-800 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Heart className="w-8 h-8 text-rose-500 fill-rose-500" />
              <div>
                <div className="font-pixel text-xs text-slate-200">VITALITY CRYSTAL</div>
                <div className="text-[11px] font-mono text-slate-400">+25 Max HP capacity</div>
              </div>
            </div>
            <button
              onClick={buyHpUpgrade}
              disabled={stats.gold < 100}
              className="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-pixel text-xs font-bold disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
            >
              100 💰
            </button>
          </div>
        </div>

        {/* Return Button */}
        <button
          onClick={() => setScreen('battle')}
          className="w-full py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-pixel text-xs flex items-center justify-center gap-2 transition-colors border border-slate-700"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>RETURN TO TOWER</span>
        </button>
      </motion.div>
    </div>
  );
};
