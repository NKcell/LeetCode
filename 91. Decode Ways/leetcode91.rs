impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        if s.len() == 0{
        return 0;
        }
        let s = s.as_bytes();
        let mut w = 1;
        let mut v = 0;
        let mut p = b'0';

        for i in s.iter(){
            let mut tmp = 0;
            if *i != b'0'{
                tmp += w;
            }
            let shi = p-b'0';
            let ge = *i-b'0';
            let value = shi*10 + ge;

            if value>9 && value<27{
                tmp += v;
            }
            v = w;
            w = tmp;
            p = *i;
        }
        w
    }
}