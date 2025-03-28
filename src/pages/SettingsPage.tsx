
import React from 'react';
import { motion } from 'framer-motion';
import { Mic, Hand, Laptop, BellRing, Camera, User, Languages } from 'lucide-react';
import SettingsCard, { ToggleSetting, SliderSetting, SelectSetting } from '@/components/SettingsCard';

const SettingsPage: React.FC = () => {
  return (
    <div className="container max-w-4xl mx-auto px-4">
      <motion.div
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.5 }}
        className="mb-6"
      >
        <h1 className="text-2xl font-bold">Settings</h1>
        <p className="text-muted-foreground">Customize your GAMINATOR experience</p>
      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <motion.div
          initial={{ x: -20, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ delay: 0.1, duration: 0.5 }}
        >
          <SettingsCard
            title="Voice Command Settings"
            description="Configure voice recognition options"
            icon={<Mic size={18} />}
          >
            <div className="space-y-4">
              <ToggleSetting
                label="Enable Voice Commands"
                description="Turn voice command recognition on or off"
                defaultChecked={true}
              />
              
              <SliderSetting
                label="Microphone Sensitivity"
                defaultValue={75}
              />
              
              <SelectSetting
                label="Language"
                options={[
                  { value: 'en-US', label: 'English (US)' },
                  { value: 'en-UK', label: 'English (UK)' },
                  { value: 'es', label: 'Spanish' },
                  { value: 'fr', label: 'French' },
                  { value: 'de', label: 'German' },
                ]}
                defaultValue="en-US"
              />
              
              <ToggleSetting
                label="Continuous Listening"
                description="Keep listening for commands without manually activating"
                defaultChecked={false}
              />
            </div>
          </SettingsCard>
        </motion.div>
        
        <motion.div
          initial={{ x: 20, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.5 }}
        >
          <SettingsCard
            title="Gesture Control Settings"
            description="Configure hand gesture recognition options"
            icon={<Hand size={18} />}
          >
            <div className="space-y-4">
              <ToggleSetting
                label="Enable Gesture Control"
                description="Turn hand gesture recognition on or off"
                defaultChecked={true}
              />
              
              <SelectSetting
                label="Camera Source"
                options={[
                  { value: 'default', label: 'Default Camera' },
                  { value: 'usb', label: 'USB Camera' },
                  { value: 'external', label: 'External Webcam' },
                ]}
                defaultValue="default"
              />
              
              <SliderSetting
                label="Detection Sensitivity"
                defaultValue={65}
              />
              
              <ToggleSetting
                label="Show Hand Skeleton"
                description="Display skeletal tracking on detected hands"
                defaultChecked={true}
              />
            </div>
          </SettingsCard>
        </motion.div>
        
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.3, duration: 0.5 }}
        >
          <SettingsCard
            title="System Settings"
            description="Configure general system behavior"
            icon={<Laptop size={18} />}
          >
            <div className="space-y-4">
              <ToggleSetting
                label="Start with System"
                description="Launch application when computer starts"
                defaultChecked={false}
              />
              
              <ToggleSetting
                label="Run in Background"
                description="Keep program running in the system tray"
                defaultChecked={true}
              />
              
              <SelectSetting
                label="Interface Theme"
                options={[
                  { value: 'system', label: 'System Default' },
                  { value: 'dark', label: 'Dark Mode' },
                  { value: 'light', label: 'Light Mode' },
                ]}
                defaultValue="dark"
              />
              
              <SliderSetting
                label="UI Animation Speed"
                defaultValue={80}
              />
            </div>
          </SettingsCard>
        </motion.div>
        
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.4, duration: 0.5 }}
        >
          <SettingsCard
            title="Notification Settings"
            description="Configure alerts and feedback"
            icon={<BellRing size={18} />}
          >
            <div className="space-y-4">
              <ToggleSetting
                label="Sound Feedback"
                description="Play sounds on command recognition"
                defaultChecked={true}
              />
              
              <ToggleSetting
                label="Visual Notifications"
                description="Show on-screen notifications for actions"
                defaultChecked={true}
              />
              
              <SliderSetting
                label="Notification Duration"
                min={1}
                max={10}
                step={0.5}
                defaultValue={3}
              />
              
              <SelectSetting
                label="Notification Position"
                options={[
                  { value: 'top-right', label: 'Top Right' },
                  { value: 'top-left', label: 'Top Left' },
                  { value: 'bottom-right', label: 'Bottom Right' },
                  { value: 'bottom-left', label: 'Bottom Left' },
                ]}
                defaultValue="top-right"
              />
            </div>
          </SettingsCard>
        </motion.div>
      </div>
    </div>
  );
};

export default SettingsPage;
