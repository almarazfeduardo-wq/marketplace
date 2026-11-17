def cart_context(request):
    """Inyecta cart_count en TODAS las plantillas automáticamente.
    Así no tienes que pasarlo manualmente desde cada vista."""
    cart = request.session.get('cart', {})
    return {
        'cart_count': sum(cart.values()),
    }