
import React from 'react';
import { motion } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Tabs, TabsList, TabsTrigger, TabsContent } from '@/components/ui/tabs';
import { Mic, Hand, Activity, Clock, Zap, Command } from 'lucide-react';
import StatCard from '@/components/StatCard';
import CommandHistory from '@/components/CommandHistory';

const DashboardPage: React.FC = () => {
  // Demo commands for both voice and gestures
  const allCommands = [
    { id: '1', type: 'voice', command: 'Open Browser', timestamp: '10:15 AM', status: 'success' },
    { id: '2', type: 'gesture', command: 'Swipe Left', timestamp: '10:20 AM', status: 'success' },
    { id: '3', type: 'voice', command: 'Volume Up', timestamp: '10:12 AM', status: 'success' },
    { id: '4', type: 'gesture', command: 'Pinch Zoom', timestamp: '10:18 AM', status: 'success' },
    { id: '5', type: 'voice', command: 'Launch Spotify', timestamp: '10:10 AM', status: 'error' },
    { id: '6', type: 'gesture', command: 'Scroll Down', timestamp: '10:15 AM', status: 'error' },
    { id: '7', type: 'voice', command: 'Next Slide', timestamp: '10:05 AM', status: 'success' },
    { id: '8', type: 'gesture', command: 'Click', timestamp: '10:14 AM', status: 'success' },
  ] as const;

  const voiceCommands = allCommands.filter(cmd => cmd.type === 'voice');
  const gestureCommands = allCommands.filter(cmd => cmd.type === 'gesture');

  return (
    <div className="container max-w-6xl mx-auto px-4">
      <motion.div
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.5 }}
        className="mb-6"
      >
        <h1 className="text-2xl font-bold">Dashboard</h1>
        <p className="text-muted-foreground">Monitor your control activity and performance</p>
      </motion.div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.1, duration: 0.5 }}
        >
          <StatCard
            title="Voice Commands"
            value={24}
            description="Used today"
            trend="up"
            trendValue="12%"
            icon={<Mic size={20} />}
          />
        </motion.div>
        
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.5 }}
        >
          <StatCard
            title="Gesture Controls"
            value={18}
            description="Used today"
            trend="up"
            trendValue="8%"
            icon={<Hand size={20} />}
          />
        </motion.div>
        
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.3, duration: 0.5 }}
        >
          <StatCard
            title="Recognition Rate"
            value="92%"
            description="Accuracy"
            trend="neutral"
            trendValue="0%"
            icon={<Zap size={20} />}
          />
        </motion.div>
        
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.4, duration: 0.5 }}
        >
          <StatCard
            title="Active Time"
            value="3h 24m"
            description="Today"
            trend="down"
            trendValue="5%"
            icon={<Clock size={20} />}
          />
        </motion.div>
      </div>
      
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <motion.div 
          className="lg:col-span-2"
          initial={{ x: -20, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ delay: 0.3, duration: 0.5 }}
        >
          <Card className="bg-card/80 backdrop-blur-sm futuristic-border">
            <CardHeader className="pb-2">
              <CardTitle className="flex items-center gap-2">
                <Activity size={18} />
                Activity History
              </CardTitle>
            </CardHeader>
            <CardContent>
              <Tabs defaultValue="all">
                <TabsList className="mb-4">
                  <TabsTrigger value="all">All Commands</TabsTrigger>
                  <TabsTrigger value="voice">Voice Only</TabsTrigger>
                  <TabsTrigger value="gesture">Gestures Only</TabsTrigger>
                </TabsList>
                
                <TabsContent value="all">
                  <CommandHistory commands={allCommands} />
                </TabsContent>
                
                <TabsContent value="voice">
                  <CommandHistory commands={voiceCommands} />
                </TabsContent>
                
                <TabsContent value="gesture">
                  <CommandHistory commands={gestureCommands} />
                </TabsContent>
              </Tabs>
            </CardContent>
          </Card>
        </motion.div>
        
        <motion.div
          initial={{ x: 20, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ delay: 0.4, duration: 0.5 }}
        >
          <Card className="bg-card/80 backdrop-blur-sm h-full futuristic-border">
            <CardHeader className="pb-2">
              <CardTitle className="flex items-center gap-2">
                <Command size={18} />
                Popular Commands
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="bg-secondary/30 rounded-md p-3">
                  <h3 className="font-medium text-sm mb-2">Voice Commands</h3>
                  <ul className="text-sm space-y-2">
                    <li className="flex justify-between">
                      <span className="text-muted-foreground">Open Browser</span>
                      <span className="text-xs bg-primary/20 px-2 py-0.5 rounded-full">28 times</span>
                    </li>
                    <li className="flex justify-between">
                      <span className="text-muted-foreground">Volume Up</span>
                      <span className="text-xs bg-primary/20 px-2 py-0.5 rounded-full">24 times</span>
                    </li>
                    <li className="flex justify-between">
                      <span className="text-muted-foreground">Close Window</span>
                      <span className="text-xs bg-primary/20 px-2 py-0.5 rounded-full">19 times</span>
                    </li>
                  </ul>
                </div>
                
                <div className="bg-secondary/30 rounded-md p-3">
                  <h3 className="font-medium text-sm mb-2">Gesture Controls</h3>
                  <ul className="text-sm space-y-2">
                    <li className="flex justify-between">
                      <span className="text-muted-foreground">Swipe Left</span>
                      <span className="text-xs bg-primary/20 px-2 py-0.5 rounded-full">32 times</span>
                    </li>
                    <li className="flex justify-between">
                      <span className="text-muted-foreground">Click</span>
                      <span className="text-xs bg-primary/20 px-2 py-0.5 rounded-full">26 times</span>
                    </li>
                    <li className="flex justify-between">
                      <span className="text-muted-foreground">Scroll Down</span>
                      <span className="text-xs bg-primary/20 px-2 py-0.5 rounded-full">15 times</span>
                    </li>
                  </ul>
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </div>
  );
};

export default DashboardPage;
