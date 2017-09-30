class dogs:
  
  def __init__(self,name):
    self.name = name
    self.stuff = []
    
  def add_command(self,command):
    self.stuff.append(command)
  
  
dog_1 = dogs('bobby_little')
dog_1.add_command("jump")
for i in range (0,2):
  dog_1.add_command("eat food")
  dog_1.add_command("sleep")
print(dog_1.stuff)

  
