export default function Show({children, when, fallback = null}) {
    if (when) {
        return <>{children}</>;
    } else {
        return <>{fallback}</>;
    }
}