
class Identifier:
    def validate_identifier(self, s: str):
        valid_id = False

        if (len(s) > 0):
            achar = s[0]
            valid_id = self.valid_s(achar)
            if (len(s) > 1):
                achar = s[1]
                i = 1
                while (i < len(s)):
                    achar = s[i]
                    if not self.valid_f(achar):
                        valid_id = False
                    
                    i = i + 1
                
        
        if (valid_id and (len(s) >= 1) and (len(s) <= 6)):
            return True
        else:
            return False
    
    def valid_s(self, ch):
        if (((ch >= 'A') and (ch <= 'Z')) or ((ch >= 'a') and (ch <= 'z'))):
            return True
        else:
            return False
    
    
    def valid_f(self, ch):
        if (((ch >= 'A') and (ch <= 'Z')) or ((ch >= 'a') and (ch <= 'z'))
            or ((ch >= '0') and (ch <= '9'))):
            return True
        else:
            return False
        

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if len(args) > 0:
        id = Identifier()
        if(id.validate_identifier(args[0])):
            print("Valido")
        else:
            print("Invalido")
    else:
        print("Uso: IdentifierMain <string>")