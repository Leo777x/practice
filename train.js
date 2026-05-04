/* ⭐️H-TASK (NodeJS)

shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib, faqat positive qiymatlarni olib string holatda return qilsin
MASALAN: getPositive([1, -4, 2]) return qiladi "12"
*/

// 🌟 MASALANING YECHIMI:
function getPositive(arr) {
    return arr
        .filter(num => num > 0)  
        .join('');                
}
const result = getPositive([1, -4, 2]);
console.log("result:", result)


/*F-TASK (NodeJS)

Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, 
agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
MASALAN: getReverse("hello") return true return qiladi
*/
// 🌟 MASALANING YECHIMI:
// function findDoublers(str) {
//   let seen = {};

//   for (let char of str) {
//     if (seen[char]) {
//       return true;
//     }
//     seen[char] = true;
//   }

//   return false;
// }

// const result = findDoublers("hello"); // true / false
// console.log("result:", result)


/*⭐️ E-TASK (NodeJS)
Shunday function tuzing, u bitta string argumentni qabul qilib
osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"
*/
// 🌟 MASALANING YECHIMI:
// function getReverse(str) {
// let resl = ""
// for (let i = str.length-1; i >= 0; i--) {
// resl  += str[i]
// }
// return resl
// }

// const result = getReverse ("hello")
// console.log("result:", result)





/*⭐️D-TASK (NodeJS)
Shunday function tuzingki unga integerlardan iborat
 array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
*/
// // 🌟 MASALANING YECHIMI:
//  function getHighestIndex(arr) {
//   let max = arr[0];
//   let index = 0;

//   for (let i = 1; i < arr.length; i++) {
//     if (arr[i] > max) {
//       max = arr[i];
//       index = i;
//     }
//   }
//   return index;
// }

// const result = getHighestIndex([5, 21, 12, 21, 8]);
// console.log("result:", result)
 
 /* ⭐️C-TASK (NodeJS)
Shunday function tuzing, u 2ta string parametr ega bolsin,
hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
*/
// 🌟 MASALANING YECHIMI:

// function checkContent(a, b) {
//   if (a.length !== b.length) return false;

//   let count = {};

//   for (let char of a) {
//     count[char] = (count[char] || 0) + 1;
//   }

//   for (let char of b) {
//     if (!count[char]) return false;
//     count[char]--;
//   }

//   return true;
// }

// const result = checkContent("mitgroup", "gmtiprou");
// console.log("result:", result)

/* ⭐️ B-TASK (Nodejs)

Shunday function tuzing, u 1ta string parametrga ega bolsin,
 hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

// 🌟 MASALANING YECHIMI:

// function countDigits(str) {
//   let count = 0;

//   for (let i = 0; i < str.length; i++) {
//     if (str[i] >= '0' && str[i] <= '9') {
//       count++;
//     }
//   }

//   return count;
// }

// const result = countDigits("ad2a54y79wet0sfgb9");
// console.log("result", result)




/* ⭐️ A-TASK (NodeJS)

Shunday 2 parametrli function tuzing, 
hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

// 🌟 MASALANING YECHIMI:

/*
function countLetter(letter, text) {
  let count = 0;

  for (let i = 0; i < text.length; i++) {
    if (text[i] === letter) {
      count++;
    }
  }

  return count;
}
const result = countLetter("e", "engineer");
console.log(result)

*/