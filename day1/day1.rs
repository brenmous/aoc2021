use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
    let mut lines = read_input();
    let mut shifted = lines.clone();
    shifted.rotate_right(1);
    lines.remove(0);
    shifted.remove(0);
    let count = lines.iter().zip(shifted.iter()).map(|(a, b)| a - b).filter(|x| x.is_positive()).collect::<Vec<i32>>().len();
    println!("{}", count);

    let lines = read_input();
    let mut shifted = lines.clone();
    shifted.rotate_left(3);
    let count = lines.iter().zip(shifted.iter()).map(|(a, b)| b - a).filter(|x| x.is_positive()).collect::<Vec<i32>>().len();
    println!("{}", count);
}

fn read_input() -> Vec<i32> {
    let f = File::open("input.txt").unwrap();
    let reader = BufReader::new(f);
    reader.lines().map(|l| l.unwrap().parse::<i32>().unwrap()).collect()
}
