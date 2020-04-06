fn main() {
    println!("Hello, world!");
    println!("{}", generate_parenthesis(3)[0]);
}

fn generate_parenthesis(n: i32) -> Vec<String> {
    let mut res: Vec<String> = Vec::new();

    if n==0{
        return res;
    }

    let l = n;
    let r = 0;


    dfs(&mut res, l, r, String::from(""));

    res
}

pub fn dfs(res: &mut Vec<String>, l: i32, r: i32, tmp_str: String){
    if l==0 && r==0{
        res.push(tmp_str);
        return
    }

    let tmp_str2 = tmp_str.clone();
    if l != 0{
        dfs(res, l-1, r+1, tmp_str+"(");
    }
    if r != 0{
        dfs(res, l, r-1, tmp_str2+")");
    }
}
