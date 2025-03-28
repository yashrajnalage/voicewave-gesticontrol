
import React from 'react';
import { motion } from 'framer-motion';
import { cn } from '@/lib/utils';

interface HandGestureVisualizerProps {
  isDetecting: boolean;
  className?: string;
}

const HandGestureVisualizer: React.FC<HandGestureVisualizerProps> = ({ isDetecting, className }) => {
  return (
    <div className={cn("relative w-full aspect-video rounded-lg overflow-hidden bg-black/60", className)}>
      {/* Camera feed placeholder */}
      <div className="absolute inset-0 flex items-center justify-center">
        {!isDetecting ? (
          <p className="text-muted-foreground text-sm">Camera feed not active</p>
        ) : (
          <div className="text-accent text-sm">Scanning for hand gestures...</div>
        )}
      </div>
      
      {isDetecting && (
        <>
          {/* Scanning grid effect */}
          <div className="absolute inset-0 pointer-events-none">
            <div className="absolute inset-0 bg-grid-pattern opacity-20"></div>
            <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-accent/60 to-transparent animate-gesture-scanning"></div>
          </div>
          
          {/* Hand detection corners */}
          {[
            'top-0 left-0 border-t border-l',
            'top-0 right-0 border-t border-r',
            'bottom-0 left-0 border-b border-l',
            'bottom-0 right-0 border-b border-r',
          ].map((position, i) => (
            <motion.div
              key={i}
              className={cn("absolute w-6 h-6 border-accent", position)}
              animate={{ opacity: [0.3, 1, 0.3] }}
              transition={{ duration: 2, repeat: Infinity, delay: i * 0.5 }}
            />
          ))}
        </>
      )}
    </div>
  );
};

export default HandGestureVisualizer;
