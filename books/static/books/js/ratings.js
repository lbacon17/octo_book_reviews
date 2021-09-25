const oneStar = document.getElementById('oneStar');
const twoStar = document.getElementById('twoStar');
const threeStar = document.getElementById('threeStar');
const fourStar = document.getElementById('fourStar');
const fiveStar = document.getElementById('fiveStar');

const ratingForm = document.querySelector('.rating-form');
const confirmBox = document.getElementById('confirm-box');
const csrf = document.getElementsByName('csrfmiddlewaretoken');

const handleStarSelect = (size) => {
    const children = ratingForm.children;
    for (let i=0; i < children.length; i++) {
        if (i <= size) {
            children[i].classList.add('checked');
        } else {
            children[i].classList.remove('checked');
        }
    }
}

const handleSelect = (selection) => {
    switch(selection){
        case 'oneStar': {
            handleStarSelect(1);
            return
        }
        case 'twoStar': {
            handleStarSelect(2);
            return
        }
        case 'threeStar': {
            handleStarSelect(3);
            return
        }
        case 'fourStar': {
            handleStarSelect(4);
            return
        }
        case 'fiveStar': {
            handleStarSelect(5);
            return
        }
    }
}

if(oneStar) {
    const ratings = [oneStar, twoStar, threeStar, fourStar, fiveStar];
    
    ratings.forEach(item => item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
    }))
}
