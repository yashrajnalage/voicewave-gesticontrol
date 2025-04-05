
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Hand, Camera, Info } from 'lucide-react';
import HandGestureVisualizer from '@/components/HandGestureVisualizer';
import CommandHistory from '@/components/CommandHistory';

const GestureControlPage: React.FC = () => {
  const [isDetecting, setIsDetecting] = useState(false);
  
  // Demo commands history for gesture controls - using non-readonly array
  const commands = [
    { id: '1', type: 'gesture', command: 'Swipe Left', timestamp: '10:20 AM', status: 'success' },
    { id: '2', type: 'gesture', command: 'Pinch Zoom', timestamp: '10:18 AM', status: 'success' },
    { id: '3', type: 'gesture', command: 'Scroll Down', timestamp: '10:15 AM', status: 'error' },
    { id: '4', type: 'gesture', command: 'Click', timestamp: '10:14 AM', status: 'success' },
  ];

  const toggleDetection = () => {
    setIsDetecting(!isDetecting);
  };

  return (
    <div className="container max-w-4xl mx-auto px-4">
      <motion.div
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.5 }}
        className="mb-6"
      >
        <h1 className="text-2xl font-bold">Gesture Control</h1>
        <p className="text-muted-foreground">Control your system using hand gestures</p>
      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <motion.div 
          className="md:col-span-2"
          initial={{ x: -20, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ delay: 0.1, duration: 0.5 }}
        >
          <Card className="bg-card/80 backdrop-blur-sm futuristic-border">
            <CardHeader className="pb-2">
              <CardTitle className="flex items-center justify-between">
                <span>Hand Gesture Recognition</span>
                <Badge variant={isDetecting ? "default" : "outline"}>
                  {isDetecting ? "Active" : "Inactive"}
                </Badge>
              </CardTitle>
            </CardHeader>
            <CardContent>
              <HandGestureVisualizer isDetecting={isDetecting} className="mb-4" />
              
              <div className="flex justify-center mb-4">
                <Button 
                  onClick={toggleDetection}
                  className={isDetecting ? 'bg-primary glow-effect' : 'bg-muted'}
                >
                  <Camera className="mr-2 h-4 w-4" />
                  {isDetecting ? 'Stop Camera' : 'Start Camera'}
                </Button>
              </div>
              
              <div className="bg-secondary/30 p-3 rounded-md flex gap-2 items-start">
                <Info size={20} className="text-primary mt-0.5" />
                <div className="text-sm">
                  <p className="font-medium">Gesture Control Tips</p>
                  <p className="text-muted-foreground">
                    Try gestures like swiping left/right to navigate, pinch to zoom,
                    or raising your hand with an open palm to pause/resume.
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>
        
        <motion.div
          initial={{ x: 20, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.5 }}
        >
          <CommandHistory commands={commands} />
        </motion.div>
      </div>
    </div>
  );
};

export default GestureControlPage;
