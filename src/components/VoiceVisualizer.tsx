
import React from 'react';
import { cn } from '@/lib/utils';

interface VoiceVisualizerProps {
  isActive: boolean;
  className?: string;
}

const VoiceVisualizer: React.FC<VoiceVisualizerProps> = ({ isActive, className }) => {
  return (
    <div className={cn("flex items-end justify-center h-20 gap-1", className)}>
      {[...Array(12)].map((_, i) => (
        <div
          key={i}
          className={cn(
            "w-2 bg-primary/60 rounded-full transition-all duration-150",
            isActive ? "animate-voice-wave" : "h-1"
          )}
          style={{
            animationDelay: `${i * 0.1}s`,
            height: isActive ? `${Math.sin((i / 11) * Math.PI) * 30 + 5}px` : "5px"
          }}
        />
      ))}
    </div>
  );
};

export default VoiceVisualizer;
