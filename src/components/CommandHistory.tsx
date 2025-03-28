
import React from 'react';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Mic, Hand, Clock } from 'lucide-react';

interface CommandProps {
  id: string;
  type: 'voice' | 'gesture';
  command: string;
  timestamp: string;
  status: 'success' | 'error' | 'pending';
}

interface CommandHistoryProps {
  commands: CommandProps[];
}

const CommandHistory: React.FC<CommandHistoryProps> = ({ commands }) => {
  return (
    <Card className="bg-card/80 backdrop-blur-sm futuristic-border">
      <CardHeader className="pb-2">
        <CardTitle className="text-sm flex items-center gap-2">
          <Clock size={16} className="text-muted-foreground" />
          Command History
        </CardTitle>
      </CardHeader>
      <CardContent>
        <ScrollArea className="h-72 pr-4">
          <ul className="space-y-2">
            {commands.length > 0 ? (
              commands.map((cmd) => (
                <li 
                  key={cmd.id} 
                  className="p-2 rounded-md bg-secondary/50 border border-border flex items-start gap-3 hover:bg-secondary/80 transition-colors"
                >
                  <span className="mt-1">
                    {cmd.type === 'voice' ? (
                      <Mic size={16} className="text-blue-400" />
                    ) : (
                      <Hand size={16} className="text-green-400" />
                    )}
                  </span>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between">
                      <p className="font-medium truncate">{cmd.command}</p>
                      <Badge 
                        variant={
                          cmd.status === 'success' ? 'default' : 
                          cmd.status === 'error' ? 'destructive' : 'outline'
                        }
                        className="ml-2 text-xs"
                      >
                        {cmd.status}
                      </Badge>
                    </div>
                    <p className="text-xs text-muted-foreground">{cmd.timestamp}</p>
                  </div>
                </li>
              ))
            ) : (
              <li className="text-center text-muted-foreground text-sm py-4">
                No commands recorded yet
              </li>
            )}
          </ul>
        </ScrollArea>
      </CardContent>
    </Card>
  );
};

export default CommandHistory;
