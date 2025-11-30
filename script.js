// PDF data - you can add more PDFs here
const pdfData = [
    {
        id: 1,
        title: "The Land of Pakistan",
        filename: "The Land of Pakistan.pdf",
        description: "Explore the diverse landscapes, rich history, and vibrant culture of Pakistan.",
        preview: "Pakistan is a South Asian country known for its diverse landscapes, rich history, vibrant culture, and iconic landmarks such as the Badshahi Mosque, K2, and the ancient city of Mohenjo-Daro."
    },
    {
        id: 2,
        title: "The World of China",
        filename: "The world of China.pdf",
        description: "Discover China's ancient history, beautiful landscapes, and delicious cuisine.",
        preview: "China spans approximately 5,250 km from east to west and 5,500 km from north to south. With over 4,000 years of recorded history, China is one of the few countries that also flourished economically and culturally during the earliest stages of world civilization."
    },
    {
        id: 3,
        title: "Exploring Kenya",
        filename: "EXPLORING KENYA.pdf",
        description: "Journey through Kenya's wildlife, mountains, and coastal beauty.",
        preview: "Kenya, a land of splendid diversity. A journey through nature, culture, and cities. Home to the 'Big Five' and the magnificent Mount Kenya."
    }
];

// DOM Elements
const pdfGrid = document.getElementById('pdfGrid');
const pdfModal = document.getElementById('pdfModal');
const pdfFrame = document.getElementById('pdfFrame');
const modalTitle = document.getElementById('modalTitle');
const downloadBtn = document.getElementById('downloadBtn');
const closeBtn = document.querySelector('.close');

// Initialize the PDF grid
function initializePDFGrid() {
    pdfGrid.innerHTML = '';
    
    pdfData.forEach(pdf => {
        const pdfCard = document.createElement('div');
        pdfCard.className = 'pdf-card';
        pdfCard.innerHTML = `
            <h3>${pdf.title}</h3>
            <p>${pdf.description}</p>
            <div class="preview">
                <div class="preview-content">${pdf.preview}</div>
            </div>
            <div style="color: #667eea; font-weight: bold;">Click to view</div>
        `;
        
        pdfCard.addEventListener('click', () => openPDF(pdf));
        pdfGrid.appendChild(pdfCard);
    });
}

// Open PDF in modal
function openPDF(pdf) {
    modalTitle.textContent = pdf.title;
    pdfFrame.src = `assets/pdfs/${encodeURIComponent(pdf.filename)}`;
    
    // Set up download button
    downloadBtn.onclick = () => {
        const link = document.createElement('a');
        link.href = `assets/pdfs/${encodeURIComponent(pdf.filename)}`;
        link.download = pdf.filename;
        link.click();
    };
    
    pdfModal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

// Close modal
function closeModal() {
    pdfModal.style.display = 'none';
    pdfFrame.src = '';
    document.body.style.overflow = 'auto';
}

// Event listeners
closeBtn.addEventListener('click', closeModal);

pdfModal.addEventListener('click', (e) => {
    if (e.target === pdfModal) {
        closeModal();
    }
});

// Close modal with Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// Initialize the application
document.addEventListener('DOMContentLoaded', initializePDFGrid);
