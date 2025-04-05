
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Mic, MicOff, Info } from 'lucide-react';
import VoiceVisualizer from '@/components/VoiceVisualizer';
import CommandHistory from '@/components/CommandHistory';

const VoiceCommandPage: React.FC = () => {
  const [isListening, setIsListening] = useState(false);
  const [recognizedText, setRecognizedText] = useState("");
  
  // Demo commands history - fixed type values to match CommandProps interface
  const commands = [
    { id: '1', type: 'voice' as const, command: 'Open Browser', timestamp: '10:15 AM', status: 'success' as const },
    { id: '2', type: 'voice' as const, command: 'Volume Up', timestamp: '10:12 AM', status: 'success' as const },
    { id: '3', type: 'voice' as const, command: 'Launch Spotify', timestamp: '10:10 AM', status: 'error' as const },
    { id: '4', type: 'voice' as const, command: 'Next Slide', timestamp: '10:05 AM', status: 'success' as const },
  ];

  const toggleListening = () => {
    setIsListening(!isListening);
    if (!isListening) {
      // Would integrate with actual voice recognition in the Python backend
      setRecognizedText("");
    } else {
      setRecognizedText("");
    }
  };

  return (
    <div className="container max-w-4xl mx-auto px-4">
      <motion.div
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.5 }}
        className="mb-6"
      >
        <h1 className="text-2xl font-bold">Voice Command Control</h1>
        <p className="text-muted-foreground">Control your system using voice commands</p>
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
                <span>Voice Recognition</span>
                <Badge variant={isListening ? "default" : "outline"}>
                  {isListening ? "Listening" : "Idle"}
                </Badge>
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex flex-col items-center mb-6">
                <motion.div 
                  className="relative mb-6"
                  whileTap={{ scale: 0.95 }}
                >
                  <Button 
                    size="lg" 
                    className={`rounded-full w-20 h-20 ${isListening ? 'bg-primary glow-effect' : 'bg-muted'}`}
                    onClick={toggleListening}
                  >
                    {isListening ? (
                      <Mic size={32} />
                    ) : (
                      <MicOff size={32} />
                    )}
                  </Button>
                  
                  {isListening && (
                    <motion.div 
                      className="absolute inset-0 rounded-full border-4 border-primary/30"
                      animate={{ scale: [1, 1.2, 1], opacity: [1, 0, 0] }}
                      transition={{ duration: 2, repeat: Infinity }}
                    />
                  )}
                </motion.div>
                
                <VoiceVisualizer isActive={isListening} className="mb-4" />
                
                <div className="text-center w-full">
                  <div className="bg-secondary/50 rounded-md p-3 min-h-16 flex items-center justify-center">
                    {recognizedText ? (
                      <p>{recognizedText}</p>
                    ) : (
                      <p className="text-muted-foreground">
                        {isListening ? "Listening..." : "Click the microphone to start"}
                      </p>
                    )}
                  </div>
                </div>
              </div>
              
              <div className="bg-secondary/30 p-3 rounded-md flex gap-2 items-start mt-4">
                <Info size={20} className="text-primary mt-0.5" />
                <div className="text-sm">
                  <p className="font-medium">Voice Command Tips</p>
                  <p className="text-muted-foreground">
                    Try commands like "Open Browser", "Volume Up", "Close Window", 
                    or "Scroll Down" to control your system.
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

export default VoiceCommandPage;
