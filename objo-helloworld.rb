class Hello
def initialize(name)
  @name = name
end

def greeting
  puts "Hello #{@name}!"
end
end

hello1 = Hello.new("World")
hello1.greeting