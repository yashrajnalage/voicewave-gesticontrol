
import React from 'react';
import { motion } from 'framer-motion';
import { Cpu } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <header className="border-b border-border bg-card/90 backdrop-blur-md sticky top-0 z-10">
      <div className="container mx-auto py-3 px-4 flex justify-between items-center">
        <div className="flex items-center space-x-2">
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5 }}
            className="bg-primary rounded-full p-1.5 glow-effect"
          >
            <Cpu size={24} className="text-primary-foreground" />
          </motion.div>
          
          <motion.h1 
            initial={{ x: -20, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{ delay: 0.2, duration: 0.5 }}
            className="text-xl md:text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300"
          >
            GAMINATOR
          </motion.h1>
        </div>
        
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.4, duration: 0.5 }}
          className="flex items-center space-x-1 text-xs md:text-sm text-muted-foreground"
        >
          <div className="h-2 w-2 rounded-full bg-accent pulse-effect"></div>
          <span>System Active</span>
        </motion.div>
      </div>
    </header>
  );
};

export default Header;
