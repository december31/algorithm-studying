import React, { useEffect } from 'react';
import { useGameStore } from '../../store/useGameStore';
import { ArrayVisualizer } from './ArrayVisualizer';
import { StackVisualizer } from './StackVisualizer';
import { LinkedListVisualizer } from './LinkedListVisualizer';
import { TreeVisualizer } from './TreeVisualizer';
import { GraphVisualizer } from './GraphVisualizer';
import { DPVisualizer } from './DPVisualizer';
import { TempleVisualizer } from './TempleVisualizer';
import { BitVisualizer } from './BitVisualizer';
import { Play, Pause, SkipBack, SkipForward, FastForward, RotateCcw } from 'lucide-react';

export const VisualizerHost: React.FC = () => {
  const {
    currentProblem,
    frames,
    currentFrameIndex,
    isPlayingTimeline,
    playbackSpeed,
    setCurrentFrameIndex,
    togglePlayTimeline,
    setPlaybackSpeed,
    stepForward,
    stepBackward,
    takeSacrificeHealth,
  } = useGameStore();

  const currentFrame = frames[currentFrameIndex] || frames[0];

  // Auto-play timeline timer
  useEffect(() => {
    if (!isPlayingTimeline) return;

    const intervalTime = Math.max(250, 1000 / playbackSpeed);
    const timer = setInterval(() => {
      if (currentFrameIndex < frames.length - 1) {
        stepForward();
      } else {
        // Reached end of animation
        togglePlayTimeline();
      }
    }, intervalTime);

    return () => clearInterval(timer);
  }, [isPlayingTimeline, currentFrameIndex, frames.length, playbackSpeed, stepForward, togglePlayTimeline]);

  if (!currentFrame) {
    return (
      <div className="w-full h-48 flex items-center justify-center text-slate-500 font-pixel text-xs">
        Preparing visualizer data...
      </div>
    );
  }

  const handleTogglePlay = () => {
    if (!isPlayingTimeline) {
      if (takeSacrificeHealth(3, 'Visualizer Vision')) {
        togglePlayTimeline();
      }
    } else {
      togglePlayTimeline();
    }
  };

  return (
    <div className="w-full flex flex-col bg-dungeon-dark/90 border border-dungeon-border rounded-xl overflow-hidden shadow-xl">
      {/* Top Bar: Visualizer Header & Step Count */}
      <div className="flex items-center justify-between px-4 py-2.5 bg-dungeon-darker/90 border-b border-dungeon-border text-xs">
        <div className="flex items-center gap-2">
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse" />
          <span className="font-pixel text-[11px] text-slate-200 uppercase tracking-wider">
            {currentProblem.visualizerType} Visualizer
          </span>
        </div>
        <div className="font-mono text-slate-400 text-xs flex items-center gap-1.5">
          <span>STEP</span>
          <span className="text-emerald-400 font-bold">{currentFrameIndex + 1}</span>
          <span>/</span>
          <span>{frames.length}</span>
        </div>
      </div>

      {/* Main Visualizer Stage */}
      <div className="w-full min-h-[220px] flex items-center justify-center bg-gradient-to-b from-dungeon-darkest/60 to-dungeon-dark/40 overflow-hidden relative">
        {currentFrame.type === 'array' && <ArrayVisualizer frame={currentFrame} />}
        {currentFrame.type === 'stack' && <StackVisualizer frame={currentFrame} />}
        {currentFrame.type === 'linkedList' && <LinkedListVisualizer frame={currentFrame} />}
        {currentFrame.type === 'tree' && <TreeVisualizer frame={currentFrame} />}
        {currentFrame.type === 'graph' && <GraphVisualizer frame={currentFrame} />}
        {currentFrame.type === 'dp' && <DPVisualizer frame={currentFrame} />}
        {currentFrame.type === 'temple' && <TempleVisualizer frame={currentFrame} />}
        {currentFrame.type === 'bits' && <BitVisualizer frame={currentFrame} />}
      </div>

      {/* Step Explanation Banner */}
      <div className="px-4 py-2 bg-dungeon-darker/70 border-t border-dungeon-border/60 min-h-[44px] flex items-center">
        <p className="font-mono text-xs sm:text-sm text-slate-300">
          <span className="text-amber-400 font-bold mr-2">▶</span>
          {currentFrame.message || 'Executing algorithmic state transition...'}
        </p>
      </div>

      {/* Bottom Controls: Playback & Scrubbing */}
      <div className="flex flex-wrap items-center justify-between gap-3 px-4 py-2.5 bg-dungeon-darkest/90 border-t border-dungeon-border">
        {/* Playback Buttons */}
        <div className="flex items-center gap-1.5">
          <button
            onClick={() => setCurrentFrameIndex(0)}
            title="Reset to beginning"
            className="p-1.5 rounded hover:bg-slate-800 text-slate-400 hover:text-slate-200 transition-colors"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
          <button
            onClick={stepBackward}
            disabled={currentFrameIndex === 0}
            title="Step Back"
            className="p-1.5 rounded hover:bg-slate-800 text-slate-400 hover:text-slate-200 disabled:opacity-30 transition-colors"
          >
            <SkipBack className="w-4 h-4" />
          </button>
          <button
            onClick={handleTogglePlay}
            title={isPlayingTimeline ? 'Pause' : 'Play (-3 HP)'}
            className="px-3 py-1.5 rounded bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-bold flex items-center gap-1 transition-colors text-xs font-pixel"
          >
            {isPlayingTimeline ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
            <span>{isPlayingTimeline ? 'PAUSE' : 'PLAY (-3 HP)'}</span>
          </button>
          <button
            onClick={stepForward}
            disabled={currentFrameIndex >= frames.length - 1}
            title="Step Forward"
            className="p-1.5 rounded hover:bg-slate-800 text-slate-400 hover:text-slate-200 disabled:opacity-30 transition-colors"
          >
            <SkipForward className="w-4 h-4" />
          </button>
        </div>

        {/* Timeline Scrub Slider */}
        <div className="flex-1 min-w-[140px] max-w-[320px] flex items-center gap-2">
          <input
            type="range"
            min={0}
            max={Math.max(0, frames.length - 1)}
            value={currentFrameIndex}
            onChange={(e) => setCurrentFrameIndex(Number(e.target.value))}
            className="w-full accent-emerald-500 cursor-pointer h-1.5 bg-slate-700 rounded-lg appearance-none"
          />
        </div>

        {/* Speed Controls */}
        <div className="flex items-center gap-1">
          <FastForward className="w-3.5 h-3.5 text-slate-400 mr-1" />
          {[0.5, 1, 2, 4].map((spd) => (
            <button
              key={spd}
              onClick={() => setPlaybackSpeed(spd)}
              className={`px-2 py-0.5 rounded text-[10px] font-pixel transition-colors ${
                playbackSpeed === spd
                  ? 'bg-amber-500 text-slate-950 font-bold'
                  : 'bg-slate-800 text-slate-400 hover:text-slate-200'
              }`}
            >
              {spd}x
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};
