// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, sum: i32) -> bool {
        let mut sum1 = sum;
        match root{
            None => return false,
            Some(i) => {
                sum1 -= i.borrow().val ;

                if sum1 == 0 && i.borrow().left.is_none() && i.borrow().right.is_none(){
                    return true;
                }

                Self::has_path_sum(i.borrow().left.clone(), sum1) || Self::has_path_sum(i.borrow().right.clone(), sum1)
            },
        }
    }
}