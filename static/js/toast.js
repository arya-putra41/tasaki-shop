function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-sky-50', 'border-blue-500', 'text-blue-900',
        'bg-gray-50', 'border-gray-300', 'text-gray-800'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-sky-50', 'border-blue-500', 'text-blue-900');
        toastComponent.style.border = '2px solid #38bdf8';
        toastIcon.innerText = '✓';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
        toastComponent.style.border = '2px solid #ef4444';
        toastIcon.innerText = '✕';
    } else {
        toastComponent.classList.add('bg-gray-50', 'border-gray-300', 'text-gray-800');
        toastComponent.style.border = '2px solid #71717a';
        toastIcon.innerText = 'ⓘ';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}