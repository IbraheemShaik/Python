class P1:
    staVariable = 5

    @classmethod
    def mod_static_variable(cls, value):
        cls.staVariable = value
        print(f"Class-level staticVariable changed to: {cls.staVariable}")

    def __init__(self):
        self.instanceVariable = P1.staVariable

    def mod_instance_variable(self, value):
        self.instanceVariable = value
        print(f"Instance-level instanceVariable changed to: {self.instanceVariable}")

# Access the static variable through the class
print(f"Initial class-level staticVariable: {P1.staVariable}")

# Modify the static variable using a class method
P1.mod_static_variable(60)

# Access the static variable through an instance
instance = P1()
print(f"Instance-level staticVariable: {instance.instanceVariable}")

instance.mod_instance_variable(55)

print(f"Class-level staticVariable remains: {P1.staVariable}")
