import math

def check_collision(circle, obstacle):
    """
    Return True if the circle (has .x, .y, .radius) collides with the rect obstacle
    (has .x, .y, .width, .height).
    Circle-vs-AABB collision using closest-point test.
    """
    cx, cy = circle.x, circle.y
    r = circle.radius

    rx, ry = obstacle.x, obstacle.y
    rw, rh = obstacle.width, obstacle.height

    closest_x = max(rx, min(cx, rx + rw))
    closest_y = max(ry, min(cy, ry + rh))

    dx = cx - closest_x
    dy = cy - closest_y

    return (dx * dx + dy * dy) <= (r * r)

def resolve_collision(circle, obstacle, restitution=0.9, push_epsilon=0.001):
    """
    If collision, push the circle out of the obstacle along the collision normal
    and reflect the velocity using a restitution coefficient (0..1).

    restitution: fraction of normal speed retained after impact (1.0 = perfectly elastic).
    Returns True if a collision was resolved.
    """
    cx, cy = circle.x, circle.y
    r = circle.radius
    rx, ry = obstacle.x, obstacle.y
    rw, rh = obstacle.width, obstacle.height

    # closest point on rect to circle center
    closest_x = max(rx, min(cx, rx + rw))
    closest_y = max(ry, min(cy, ry + rh))

    nx = cx - closest_x
    ny = cy - closest_y
    dist_sq = nx * nx + ny * ny

    # special case: circle center is inside rectangle (or exactly on edges)
    if dist_sq == 0:
        # push out along the smallest penetration axis
        left = cx - rx
        right = (rx + rw) - cx
        top = cy - ry
        bottom = (ry + rh) - cy

        # find smallest distance to an edge
        min_dist = min(left, right, top, bottom)
        if min_dist == left:
            nx, ny = -1.0, 0.0
            penetration = r - left
        elif min_dist == right:
            nx, ny = 1.0, 0.0
            penetration = r - right
        elif min_dist == top:
            nx, ny = 0.0, -1.0
            penetration = r - top
        else:
            nx, ny = 0.0, 1.0
            penetration = r - bottom

        # normalize normal (already unit in axis cases)
        length = math.hypot(nx, ny)
        if length != 0:
            nx /= length
            ny /= length
    else:
        dist = math.sqrt(dist_sq)
        penetration = r - dist
        if penetration <= 0:
            return False
        nx /= dist
        ny /= dist

    # push circle out of obstacle slightly to avoid repeated penetration
    if penetration > 0:
        circle.x += nx * (penetration + push_epsilon)
        circle.y += ny * (penetration + push_epsilon)

    # reflect velocity across normal with restitution:
    # v' = v - (1 + e) * (v·n) * n
    v_dot_n = circle.vx * nx + circle.vy * ny
    # Only apply if moving toward the obstacle (v_dot_n < 0)
    if v_dot_n < 0:
        factor = (1 + restitution) * v_dot_n
        circle.vx -= factor * nx
        circle.vy -= factor * ny

    return True