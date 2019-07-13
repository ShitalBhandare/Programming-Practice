
# python polymorphism

class India:
    def capital(self):
        print("India is capital")
        
    def speak(self):
        print("Hindi is national language")
        
class USA:
    def capital(self):
        print("Washington D. C. is capital")
        
    def speak(self):
        print("English is national language")
        
ind_obj = India()
usa_obj = USA()

for obj in (ind_obj, usa_obj):
    obj.capital()
    obj.speak()


def do_obj(obj):
    obj.capital()
    obj.speak()
    
do_obj(ind_obj)
do_obj(usa_obj)


output:

$python3 main.py
India is capital
Hindi is national language
Washington D. C. is capital
English is national language
India is capital
Hindi is national language
Washington D. C. is capital
English is national language