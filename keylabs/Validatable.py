class Validatable:
  def validate(self):
      return

  @property
  def isValid(self):
    try:
      self.validate()
      return True
    except:
      return False