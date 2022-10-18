import appdaemon.plugins.hass.hassapi as hass

class WakeUp(hass.Hass):

  def initialize(self):
  # create two callbacks: time_change and turn_on_light
 
     self.listen_state(self.time_change, "input_datetime.set_wake_up_light", duration = 10) # helper entity on dashboard
     self.handle = self.run_daily(self.turn_on_light, (self.get_state("input_datetime.set_wake_up_light"))) 

  def turn_on_light(self, kwargs):
     self.switch = self.get_entity("input_boolean.wake_up_light_switch") # switch on dashboard to turn on/off the automation
     self.bedroom_light = self.get_entity("light.the_bedroom_light")
    
     if self.switch.is_state("on"):
        self.bedroom_light.turn_on(transition = 120)
     else:
        self.log("wake up light automation is off")

  def time_change(self, entity, attribute, old, new, kwargs):
     self.handle = self.run_daily(self.turn_on_light, (self.get_state("input_datetime.set_wake_up_light"))) # recreates the run_daily callback with new time set from the dashboard
  