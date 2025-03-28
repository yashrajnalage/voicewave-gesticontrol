
import React from 'react';
import { Link, Outlet, useLocation } from 'react-router-dom';
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Mic, Hand, Settings, Gauge, Home } from 'lucide-react';
import Header from './Header';

const Layout: React.FC = () => {
  const location = useLocation();
  const currentPath = location.pathname;

  return (
    <div className="min-h-screen flex flex-col bg-background hexagon-grid">
      <Header />
      
      <main className="flex-1 container mx-auto py-6 px-4">
        <Outlet />
      </main>
      
      <footer className="sticky bottom-0 bg-card/80 backdrop-blur-md border-t border-border py-2">
        <div className="container mx-auto">
          <Tabs value={currentPath} className="w-full">
            <TabsList className="w-full justify-between bg-secondary/50">
              <TabsTrigger value="/" asChild className="data-[state=active]:bg-primary">
                <Link to="/" className="flex flex-col items-center gap-1 px-1">
                  <Home size={20} />
                  <span className="text-xs">Home</span>
                </Link>
              </TabsTrigger>
              <TabsTrigger value="/voice" asChild className="data-[state=active]:bg-primary">
                <Link to="/voice" className="flex flex-col items-center gap-1 px-1">
                  <Mic size={20} />
                  <span className="text-xs">Voice</span>
                </Link>
              </TabsTrigger>
              <TabsTrigger value="/gesture" asChild className="data-[state=active]:bg-primary">
                <Link to="/gesture" className="flex flex-col items-center gap-1 px-1">
                  <Hand size={20} />
                  <span className="text-xs">Gesture</span>
                </Link>
              </TabsTrigger>
              <TabsTrigger value="/dashboard" asChild className="data-[state=active]:bg-primary">
                <Link to="/dashboard" className="flex flex-col items-center gap-1 px-1">
                  <Gauge size={20} />
                  <span className="text-xs">Dashboard</span>
                </Link>
              </TabsTrigger>
              <TabsTrigger value="/settings" asChild className="data-[state=active]:bg-primary">
                <Link to="/settings" className="flex flex-col items-center gap-1 px-1">
                  <Settings size={20} />
                  <span className="text-xs">Settings</span>
                </Link>
              </TabsTrigger>
            </TabsList>
          </Tabs>
        </div>
      </footer>
    </div>
  );
};

export default Layout;
