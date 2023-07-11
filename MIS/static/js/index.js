console.log("Hello")

// #################### Number Counter code start here #############################################

const UpdateSectionCounter = document.querySelector('.Counter-Number');
const workObserver = new IntersectionObserver((entries, observe) => {
    const [entry] = entries;

    if (!entry.isIntersecting) return;
    const counterNumber = document.querySelectorAll(".Counter-Number");

    const speed = 200;

    counterNumber.forEach((curElem) => {
        const updateNumber = () => {
            const targetNumber = parseInt(curElem.dataset.numbers);
            const intialNumber = parseInt(curElem.innerText);


            const incrementNnumber = Math.trunc(targetNumber / speed);
            if (intialNumber < targetNumber) {
                curElem.innerText = `${intialNumber + incrementNnumber}+`;
                setTimeout(updateNumber, 10);
            }
        };

        updateNumber();
    });

}, {
    root: null,
    threshold: 0,
});


workObserver.observe(UpdateSectionCounter);


// haburger start here 

burger = document.querySelector('.burger');
nanItem = document.querySelector('.nav-item');
navbar = document.querySelector('.hidden');

burger.addEventListener('click',()=>{
    navbar.classList.toggle('hidden');
});


