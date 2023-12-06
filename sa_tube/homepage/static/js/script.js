window.addEventListener('load', function () {
    loadAllData();
});

const setActiveButton = (activeBtnId) => {
    const buttons = ["allBtn", "comedyBtn", "musicBtn", "drawingBtn"];

    buttons.forEach((btnId) => {
        const btn = document.getElementById(btnId);
        btn.classList.remove("bg-red-600", "text-white");
        btn.classList.add("bg-gray-300", "text-gray-700");
    });

    const activeBtn = document.getElementById(activeBtnId);
    activeBtn.classList.remove("bg-gray-300", "text-gray-700");
    activeBtn.classList.add("bg-red-600", "text-white");
};

const loadAllData = () => {
    fetchData("https://openapi.programming-hero.com/api/videos/category/1000");
    setActiveButton("allBtn");
};

const loadMusicData = () => {
    fetchData("https://openapi.programming-hero.com/api/videos/category/1001");
    setActiveButton("musicBtn");
};

const loadComedyData = () => {
    fetchData("https://openapi.programming-hero.com/api/videos/category/1003");
    setActiveButton("comedyBtn");
};

const loadDrawingData = () => {
    fetchData("https://openapi.programming-hero.com/api/videos/category/1005");
    setActiveButton("drawingBtn");
};

const fetchData = (url) => {
    fetch(url)
        .then((res) => res.json())
        .then((info) => display(info.data))
        .catch((error) => {
            console.error("Error fetching data:", error);
            videos.innerHTML = "<p>Error loading videos. Please try again later.</p>";
        });
};

const sortAndDisplayByViews = () => {
    const videos = document.getElementById("videos");
    const videoElements = Array.from(videos.children);

    const sortedVideos = videoElements.sort((a, b) => {
        const viewsA = parseInt(a.querySelector('.text-xs').textContent.split(' ')[0]);
        const viewsB = parseInt(b.querySelector('.text-xs').textContent.split(' ')[0]);

        return viewsB - viewsA;
    });

    videos.innerHTML = "";
    sortedVideos.forEach(video => {
        videos.appendChild(video);
    });
};

function formatPostedDate(postedDateInSeconds) {
    if (!postedDateInSeconds) {
        return ""; 
    }

    const seconds = parseInt(postedDateInSeconds);

    const days = Math.floor(seconds / (3600 * 24));
    const hours = Math.floor((seconds % (3600 * 24)) / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);

    
    const formattedDate = `${days > 0 ? days + 'd ' : ''}${hours}h ${minutes < 10 ? '0' : ''}${minutes}m ago`;

    return formattedDate;
}

const display = (info) => {
    const videos = document.getElementById("videos");

    videos.innerHTML = "";

    if (info.length === 0) {
        videos.innerHTML = `
        <div class="container max-w-screen-xl mx-auto md:mt-20 mt-8 text-center">
            <img class="mx-auto block" src="images/icon.png" alt="">
            <h1 class="mt-10 text-xl font-bold">Oops!! Sorry, There is no content here</h1>
        </div>
        `;
    } else {
        info.forEach((video) => {
            const card = document.createElement("div");
            card.classList.add("max-w-xl", "w-72", "mx-auto", "bg-white", "rounded-md", "overflow-hidden", "shadow-md", "relative");

            const isVerified = video?.authors[0].verified;

            card.innerHTML = `
            <a href="#">
                <img src="${video.thumbnail}" alt="Video Thumbnail" class="w-full h-40 object-cover">
                
                <div class="p-4">
                    <div class="flex">
                        <img src="${video?.authors[0].profile_picture}" alt="Author" class="w-10 h-10 rounded-full mr-2">
                        <div class="flex-1">
                            <h2 class="text-md mb-1 font-normal text-gray-800">${video?.title}</h2>
                            <p class="text-gray-700 flex text-sm font-thin mb-1">${video?.authors[0].profile_name}<span>${isVerified ? '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#1640D6" class="w-4 h-5"><path d="M8.603 3.799A4.49 4.49 0 0112 2.25c1.357 0 2.573.6 3.397 1.549a4.49 4.49 0 013.498 1.307 4.491 4.491 0 011.307 3.497A4.49 4.49 0 0121.75 12a4.49 4.49 0 01-1.549 3.397 4.491 4.491 0 01-1.307 3.497 4.491 4.491 0 01-3.497 1.307A4.49 4.49 0 0112 21.75a4.49 4.49 0 01-3.397-1.549 4.49 4.49 0 01-3.498-1.306 4.491 4.491 0 01-1.307-3.498A4.49 4.49 0 012.25 12c0-1.357.6-2.573 1.549-3.397a4.49 4.49 0 011.307-3.497 4.49 4.49 0 013.497-1.307zm7.007 6.387a.75.75 0 10-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 00-1.06 1.06l2.25 2.25a.75.75 0 001.14-.094l3.75-5.25z" clip-rule=""/></svg>':''}</span></p>
                            
                            <p class="text-xs font-thin text-gray-700">${video?.others.views} views</p>
                            ${video.others.posted_date ? `<span class="absolute bg-slate-900 font-thin text-sm -mt-28 right-0 text-white rounded px-3 py-[1px]">${formatPostedDate(video.others.posted_date)}</span>` : ''}
                        </div>
                    </div>
                </div>
            </a>
            `;
            videos.appendChild(card);
        });
    }
};