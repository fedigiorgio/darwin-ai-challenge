export function format(category: string): string {
    return category.charAt(0).toUpperCase() + category.slice(1).toLowerCase();
}