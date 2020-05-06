use std::collections::HashMap;

fn main() {
    println!("Hello, world!");
    println!("{}", dest_city(vec![vec![String::from("B"), String::from("C")], vec![String::from("C"), String::from("D")]]))
}

fn dest_city(paths: Vec<Vec<String>>) -> String {
    let mut res = HashMap::new();

    for i in 0..paths.len(){
        if res.get(&paths[i][0]) != None{
            res.remove(&paths[i][0]);
        }else{
            res.insert(&paths[i][0], 0);
        }


        if res.get(&paths[i][1]) != None{
            res.remove(&paths[i][1]);
        }else{
            res.insert(&paths[i][1], 1);
        }
    }

    for (key, value) in &res {
        //println!("{}: {}", key, value);
        if *value == 1{
            return key.to_string();
        }
    }

    return String::from("");
}

fn dest_city2(paths: Vec<Vec<String>>) -> String {
    let s: HashSet<String> = paths.iter().map(|v| v[0].clone()).collect();
    let t: HashSet<String> = paths.iter().map(|v| v[1].clone()).collect();
    t.difference(&s).collect::<Vec<&String>>()[0].to_string()
}

fn dest_city2(paths: Vec<Vec<String>>) -> String {
    let sources: std::collections::HashSet<String> = 
    paths
    .iter()
    .map(|path| {
        path[0].clone()
    })
    .collect();
    for path in &paths {
        let dest = path[1].clone();
        if !(sources.contains(&dest)) {
            return dest;
        }
    }
    paths[0][1].clone()
}

fn dest_city3(paths: Vec<Vec<String>>) -> String {
    let mut cities: HashSet<String> = HashSet::new();
    
    for path in paths.iter() {
        cities.insert(path[0].clone());
    }
    
    for path in paths.iter() {
        if !cities.contains(&path[1]) {
            return path[1].clone();
        }
    }
    
    return "".to_string();
}