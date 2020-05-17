class Validatable:
  def validate(self):
      return

  @property
  def is_valid(self):
    try:
      self.validate()
      return True
    except:
      return False