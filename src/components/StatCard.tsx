
import React from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { cn } from '@/lib/utils';

interface StatCardProps {
  title: string;
  value: string | number;
  icon: React.ReactNode;
  description?: string;
  trend?: 'up' | 'down' | 'neutral';
  trendValue?: string;
  className?: string;
}

const StatCard: React.FC<StatCardProps> = ({
  title,
  value,
  icon,
  description,
  trend,
  trendValue,
  className,
}) => {
  return (
    <Card className={cn("bg-card/80 backdrop-blur-sm", className)}>
      <CardContent className="p-4">
        <div className="flex justify-between items-start">
          <div>
            <p className="text-sm text-muted-foreground mb-1">{title}</p>
            <div className="flex items-baseline gap-1">
              <p className="text-2xl font-bold">{value}</p>
              {trend && trendValue && (
                <span 
                  className={cn(
                    "text-xs",
                    trend === 'up' ? 'text-green-400' : 
                    trend === 'down' ? 'text-red-400' : 
                    'text-muted-foreground'
                  )}
                >
                  {trend === 'up' ? '↑' : trend === 'down' ? '↓' : '•'} {trendValue}
                </span>
              )}
            </div>
            {description && <p className="text-xs text-muted-foreground mt-1">{description}</p>}
          </div>
          <div className="bg-secondary p-2 rounded-md">
            {icon}
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default StatCard;
