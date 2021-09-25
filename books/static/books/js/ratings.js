console.log("hello world");

const oneStar = document.getElementById('oneStar');
const twoStar = document.getElementById('twoStar');
const threeStar = document.getElementById('threeStar');
const fourStar = document.getElementById('fourStar');
const fiveStar = document.getElementById('fiveStar');

const handleSelect = (selection) => {
    switch(selection){
        case 'oneStar': {
            oneStar.classList.add('checked');
            twoStar.classList.remove('checked');
            threeStar.classList.remove('checked');
            fourStar.classList.remove('checked');
            fiveStar.classList.remove('checked');
            return
        }
        case 'twoStar': {
            oneStar.classList.add('checked');
            twoStar.classList.add('checked');
            threeStar.classList.remove('checked');
            fourStar.classList.remove('checked');
            fiveStar.classList.remove('checked');
            return
        }
        case 'threeStar': {
            oneStar.classList.add('checked');
            twoStar.classList.add('checked');
            threeStar.classList.add('checked');
            fourStar.classList.remove('checked');
            fiveStar.classList.remove('checked');
            return
        }
        case 'fourStar': {
            oneStar.classList.add('checked');
            twoStar.classList.add('checked');
            threeStar.classList.add('checked');
            fourStar.classList.add('checked');
            fiveStar.classList.remove('checked');
            return
        }
        case 'fiveStar': {
            oneStar.classList.add('checked');
            twoStar.classList.add('checked');
            threeStar.classList.add('checked');
            fourStar.classList.add('checked');
            fiveStar.classList.add('checked');
            return
        }
    }
}

const ratings = [oneStar, twoStar, threeStar, fourStar, fiveStar];

ratings.forEach(item => item.addEventListener('mouseover', (event)=>{
    handleSelect(event.target.id)
}))