
import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Label } from '@/components/ui/label';
import { Switch } from '@/components/ui/switch';
import { Slider } from '@/components/ui/slider';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { cn } from '@/lib/utils';

interface SettingsCardProps {
  title: string;
  description?: string;
  icon: React.ReactNode;
  className?: string;
  children?: React.ReactNode;
}

const SettingsCard: React.FC<SettingsCardProps> = ({
  title,
  description,
  icon,
  className,
  children,
}) => {
  return (
    <Card className={cn("bg-card/80 backdrop-blur-sm futuristic-border", className)}>
      <CardHeader className="pb-2">
        <div className="flex items-center gap-2">
          <div className="bg-primary/20 p-1.5 rounded-md text-primary">
            {icon}
          </div>
          <div>
            <CardTitle className="text-base">{title}</CardTitle>
            {description && <CardDescription>{description}</CardDescription>}
          </div>
        </div>
      </CardHeader>
      <CardContent>
        {children}
      </CardContent>
    </Card>
  );
};

export function ToggleSetting({ 
  label, 
  description,
  defaultChecked = false,
  onChange
}: { 
  label: string;
  description?: string;
  defaultChecked?: boolean;
  onChange?: (checked: boolean) => void;
}) {
  return (
    <div className="flex items-center justify-between space-y-1 py-2">
      <div>
        <Label htmlFor={`toggle-${label}`}>{label}</Label>
        {description && <p className="text-xs text-muted-foreground">{description}</p>}
      </div>
      <Switch 
        id={`toggle-${label}`} 
        defaultChecked={defaultChecked}
        onCheckedChange={onChange}
      />
    </div>
  );
}

export function SliderSetting({
  label,
  min = 0,
  max = 100,
  step = 1,
  defaultValue = 50,
  onChange
}: {
  label: string;
  min?: number;
  max?: number;
  step?: number;
  defaultValue?: number;
  onChange?: (value: number[]) => void;
}) {
  return (
    <div className="space-y-2 py-2">
      <div className="flex items-center justify-between">
        <Label htmlFor={`slider-${label}`}>{label}</Label>
        <span className="text-xs text-muted-foreground">{defaultValue}%</span>
      </div>
      <Slider
        id={`slider-${label}`}
        min={min}
        max={max}
        step={step}
        defaultValue={[defaultValue]}
        onValueChange={onChange}
      />
    </div>
  );
}

export function SelectSetting({
  label,
  options,
  defaultValue,
  onChange
}: {
  label: string;
  options: { value: string; label: string }[];
  defaultValue?: string;
  onChange?: (value: string) => void;
}) {
  return (
    <div className="space-y-2 py-2">
      <Label htmlFor={`select-${label}`}>{label}</Label>
      <Select defaultValue={defaultValue} onValueChange={onChange}>
        <SelectTrigger id={`select-${label}`}>
          <SelectValue placeholder={`Select ${label}`} />
        </SelectTrigger>
        <SelectContent>
          {options.map((option) => (
            <SelectItem key={option.value} value={option.value}>
              {option.label}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </div>
  );
}

export default SettingsCard;
