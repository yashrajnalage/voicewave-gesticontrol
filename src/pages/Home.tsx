
import React from 'react';
import { motion } from 'framer-motion';
import { Button } from '@/components/ui/button';
import { Mic, Hand, ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';
import { Card, CardContent } from '@/components/ui/card';

const Home: React.FC = () => {
  return (
    <div className="container max-w-4xl mx-auto px-4 py-8">
      <motion.div
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.5 }}
        className="text-center mb-8"
      >
        <h1 className="text-4xl font-bold mb-2 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-cyan-300 to-teal-300">
          Welcome to GAMINATOR
        </h1>
        <p className="text-muted-foreground">
          Control your computer with voice and gesture commands
        </p>
      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <motion.div
          initial={{ x: -20, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.5 }}
        >
          <Card className="h-full glass-panel">
            <CardContent className="p-6 flex flex-col items-center text-center">
              <div className="bg-blue-500/20 p-4 rounded-full mb-4 glow-effect">
                <Mic size={32} className="text-blue-400" />
              </div>
              <h2 className="text-xl font-semibold mb-2">Voice Commands</h2>
              <p className="text-muted-foreground mb-4">
                Control your computer using simple voice commands for navigation, 
                application control, and system functions.
              </p>
              <Button asChild variant="outline" className="mt-auto">
                <Link to="/voice" className="gap-2">
                  Try Voice Commands <ArrowRight size={16} />
                </Link>
              </Button>
            </CardContent>
          </Card>
        </motion.div>

        <motion.div
          initial={{ x: 20, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ delay: 0.3, duration: 0.5 }}
        >
          <Card className="h-full glass-panel">
            <CardContent className="p-6 flex flex-col items-center text-center">
              <div className="bg-green-500/20 p-4 rounded-full mb-4 glow-effect">
                <Hand size={32} className="text-green-400" />
              </div>
              <h2 className="text-xl font-semibold mb-2">Gesture Control</h2>
              <p className="text-muted-foreground mb-4">
                Use hand gestures to navigate and interact with your applications
                without touching your keyboard or mouse.
              </p>
              <Button asChild variant="outline" className="mt-auto">
                <Link to="/gesture" className="gap-2">
                  Try Gesture Control <ArrowRight size={16} />
                </Link>
              </Button>
            </CardContent>
          </Card>
        </motion.div>
      </div>

      <motion.div
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ delay: 0.4, duration: 0.5 }}
        className="text-center"
      >
        <div className="glass-panel p-6 rounded-lg">
          <h3 className="text-lg font-medium mb-2">Getting Started</h3>
          <p className="text-muted-foreground mb-4">
            GAMINATOR allows you to control your computer without touching it.
            Try saying "Open Browser" or use a swipe gesture to navigate between apps.
          </p>
          <Button asChild>
            <Link to="/dashboard">
              Go to Dashboard
            </Link>
          </Button>
        </div>
      </motion.div>
    </div>
  );
};

export default Home;
