class Calculator:
    def add(self, a, b):
        return a + b

    #ควรแก้เป็น a-b เพราะว่าปกติเอาตัวตั้งขึ้นก่อน????? 
    def subtract(self, a, b):
        return a - b

    #ไม่ควร b+1 เพราะว่าไพท่อนมันเลยให้ ค่าเลยเพิ่มไป 1
    #ต้องแก้ให้รองรับการติดลบ
    def multiply(self, a, b):
        result = 0
        #ดูว่าบวกลบกี่ตัว
        neg_count = 0
        if a < 0:
            neg_count += 1
        if b < 0:
            neg_count += 1
        #จับ abs 
        a = abs(a)
        b = abs(b)
        #ถ้าติดลบตัวเดียว ผลลัพธ์ได้ติดลบ
        if neg_count == 1 :
            for i in range(b):
                result = self.subtract(result, a)
        #จับบวกตามปกติ กรณี
        else:
            for i in range(b):
                result = self.add(result, a)
        return result

    #หารโดน effect จาก subtract 
    #แต่ว่าใช้ while loop เจอ ติดลบ+เจอ divide by zero = แตก
    def divide(self, a, b):
        result = 0
        #กันระเบิด
        if b == 0:
            return "Error: Divide by 0"
        neg_count = 0
        if a < 0:
            neg_count += 1
        if b < 0:
            neg_count += 1
        #จับ abs 
        a = abs(a)
        b = abs(b)
        while a > b:
            a = self.subtract(a, b)
            result += 1
        #*-1 แต่ใช้ฟังก์ชั่นให้เป็นประโยชน์
        if neg_count == 1:
            result = self.multiply(result,-1)
        return result
    
    # mod ลูกศรหัวกลับ ??? 10 mod 3 ควรได้ 1 
    # ต้องรองรับจำนวนลบด้วย
    def modulo(self, a, b):
        #ดัก mod 0
        if b == 0:
            return "Error: mod by 0"
        # -a mod -b
        if (a < 0 and b < 0):
            while a <= b:
                a = a - b
        # -a mod b
        elif (a < 0 and b > 0):
            while (a <= b and a < 0):
                a = a + b
        # a mod b
        elif (a >= 0 and b > 0):
            while (a >= b):
                a = a - b
        # a mod -b
        else:
            while (a >= b and a > 0):
                a = a + b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))