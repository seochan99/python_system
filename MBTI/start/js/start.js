const main = document.querySelector("#main");
const qna = document.querySelector("#qna"); 

function addAnswer(answerText, qIdx)
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
    var q = document.querySelector('.qBox');
    q.innerHTML = qnaList[qIdx].q; 
    for(let i in qnaList[qIdx].a)
    {
        addAnswer(qnaList[qIdx].a[i].answer,qIdx);
    }

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