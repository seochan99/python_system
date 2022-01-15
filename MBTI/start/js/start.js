const main = document.querySelector("#main");
const qna = document.querySelector("#qna"); 
const result = document.querySelector("#result"); 
const endPoint = 12; //총 질문 수 
const select=[0,0,0,0,0,0,0,0,0,0,0,0];//어떤거 선택하는지 알아야지..

function calResult()
{
    // var pointArray =[
    //     {name:'mouse', value: 0, key:0},
    //     {name:'cow', value: 0, key:1},
    //     {name:'tiger', value: 0, key:2},
    //     {name:'rabbit', value: 0, key:3},
    //     {name:'dragon', value: 0, key:4},
    //     {name:'snake', value: 0, key:5},
    //     {name:'horse', value: 0, key:6},
    //     {name:'sheep', value: 0, key:7},
    //     {name:'monkey', value: 0, key:8},
    //     {name:'chick', value: 0, key:9},
    //     {name:'dog', value: 0, key:10},
    //     {name:'pig', value: 0, key:11},
    // ]

    // for(let i =0;i<endPoint;i++)
    // {
    //     var target = qnaList[i].a[select[i]]; 
    //     //ans과 type이 담김
    //     for(let j=0;j<target.type.length;j++)
    //     {
    //         for(let k=0;k<pointArray;k++)
    //         {
    //             if(target.target[j]===pointArray[k].name){
    //                 pointArray[k].value+=1; //만약 타겟의 값이 포인트 배열의 이름과 동일하다면 그 배열의 벨류를 증가시킨다. 
    //             }
    //         }
    //     }
    // }

    //value기준 정렬 
    // var resultArray = pointArray.sort(function(a,b) //sort함수 학습
    // {
    //     if(a.value>b.value){
    //         return -1;
    //     }
    //     if(a.value<b.value){
    //         return 1;
    //     }
    //     return 0;
    // })
    var result = select.indexOf(Math.max(...select));
    return result;

    // let resultword = resultArray[0].key; 


    // return resultword;
}

function setResult(){
    let point = calResult();
    const resultName = document.querySelector('.resultname');
    resultName.innerHTML = infoList[point].name;

    var resultImg = document.createElement('img');
    const imgDiv = document.querySelector("#resultImg");
    var imgURL='img/image-'+point+".png";
    resultImg.src = imgURL;
    resultImg.alt = point;

    imgDiv.appendChild(resultImg);
    const resultDesc = document.querySelector('.resultDesc');
    resultDesc.innerHTML = infoList[point].desc; 

}

function goResult()
{
    qna.style.WebkitAnimation = "fadeOut 1s";
    qna.style.animation = "fadeOut 1s";
    setTimeout(()=>{
        result.style.WebkitAnimation = "fadeIn 1s";
        result.style.animation = "fadeIn 1s";
        setTimeout(()=>{
            qna.style.display = "none";
            result.style.display = "block"
        },450)
        let qIdx = 0;
        goNext(qIdx);
    },450); 
    setResult();
    // calResult(); //불러와주기 
}

function addAnswer(answerText, qIdx,idx)
{
    var a = document.querySelector('.answerBox') // a는 질문박스 
    var answer = document.createElement('Button');//버튼만듬 
    answer.classList.add('answerList'); //클래스추가 
    answer.classList.add('my-3'); //클래스추가 마진 패딩 
    answer.classList.add('py-3'); //클래스추가 
    answer.classList.add('mx-auto'); //클래스추가 
    answer.classList.add('fadeIn');

    a.appendChild(answer); //a태그안에 질문 버튼 만듬 
    answer.innerHTML =  answerText;

    //클릭시 사라지게 만듬 
    answer.addEventListener("click",function(){
        var children = document.querySelectorAll('.answerList'); //모든버튼선택
        for(let i =0;i<children.length;i++)
        {
            children[i].disabled = true;
            children[i].style.WebkitAnimation = "fadeOut 0.5s";
            children[i].style.animation = "fadeOut 0.5s";
        }
        setTimeout(()=>{
            var target = qnaList[qIdx].a[idx].type; 
            //ans과 type이 담김
            for(let j=0;j<target.type.length;j++)
            { //수정필요.
                select[target[i]]+=1;
            }
            // select[] = idx; //먗번째 선택했는지 배열에 담김 
            for(let i =0;i<children.length;i++)
            {
                children[i].style.display='none'; //안보이게 만듬 
            }
            goNext(++qIdx);
        },450)
        // 사라지는게 끝나면 다음질문 출력 
        
    })
}

function goNext(qIdx){
    if(qIdx ===endPoint)
    {
        goResult();
    }

    var q = document.querySelector('.qBox');
    q.innerHTML = qnaList[qIdx].q; 
    for(let i in qnaList[qIdx].a)
    {
        addAnswer(qnaList[qIdx].a[i].answer,qIdx,i);
    }
    //상태바 채워나가기 
    var status = document.querySelector('.statusBar');
    status.style.width = (100/endPoint)*(qIdx+1)+'%'

}

function begin(){
    main.style.WebkitAnimation = "fadeOut 1s";
    main.style.animation = "fadeOut 1s";
    setTimeout(()=>{
        qna.style.WebkitAnimation = "fadeIn 1s";
        qna.style.animation = "fadeIn 1s";
        setTimeout(()=>{
            main.style.display = "none";
            qna.style.display = "block"
        },450)
        let qIdx = 0;
        goNext(qIdx);
    },450); 
    
}

ehdwk동자



// function showError(){
//     alert('에러가 발생했습니다.');
// }
// showError();

// function sayhello(name){
//     let msg= `hello`; 
//     if(name){
//         msg = `Hello ${name}`;
//     }
//     console.log(msg);
// }
// sayhello('mike')

function showError(){
    console.log("error");
}


showError();

let showError = function(){
    console.log('error'); 
}
let showError =()=>{
    console.log("error");
}
const sayHello = function(name){
    const msg = `Hello, ${name}`;
    console.log(msg);
};
const sayHello = (name)=>{
    const msg = `Hello, ${name}`;
    console.log(msg);
};

const add = function(num1,num2){
    const result = num1 + num2;
    return result;
};

// 익숙해져야행,, 
const add = (num1,num2)=> num1+num2; 
//return 1줄이면 더 간단히 만든다...! 

//객체 
// const superman = {
//     name : "clark",
//     age : 30,
// }

// superman.hairColor = "black"; //추가 
// superman['hobby']="football"
// delete superman.age; 

// console.log(superman)
// console.log(superman.name)
// console.log(superman['age']) 


// function makeObject(name,age){
//     return{
//         name : name,
//         age : age,
//         hobby : 'football'
//     }
// }
// function makeObject(name,age){
//     return{
//         name,
//         age,
//         hobby : 'football'
//     }
// }

// const Mike = makeObject('Mike',30);
// console.log(Mike);
// console.log('age' in Mike)
// console.log("birthday" in Mike)

// function isAdult(user)
// {
//     if(!('age' in user) || user.age<20){
//         return false;
//     }
//     return true; 
// }

// const Mike = {
//     name : 'Mike',
//     age : 30
// };

// for(x in Mike){
//     console.log(Mike[x]) // Mike['age]
// }

// const Jane = {
//     name : "Jane"
// };

//Method This 
