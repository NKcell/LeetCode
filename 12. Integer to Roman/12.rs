impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        let value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

        let mut res = String::from("");
        let mut num1 = num;
        let mut i = 0;

        while num1!=0{
            let tmp = num1/value[i];

            for _j in 0..tmp{
                res.push_str(symbol[i]);
            }

            num1 = num1%value[i];
            i += 1;
        }

        res
    }
}