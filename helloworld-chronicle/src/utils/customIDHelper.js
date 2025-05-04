export function sectionIDToName(id) {
    return id.split('-').slice(1).map(el => el[0].toUpperCase() + el.slice(1)).join(' ');
}