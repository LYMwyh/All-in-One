export function getIDsInCurrentPage() {
    return [...document.querySelectorAll('[id]')].map(el => el.id);
}

export function idToName(id) {
    return id.split('-').map(el => el[0].toUpperCase() + el.slice(1)).join(' ');
}