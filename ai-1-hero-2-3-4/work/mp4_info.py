import struct


def read_boxes(f, start, end, depth=0, results=None):
    if results is None:
        results = []
    f.seek(start)
    while f.tell() + 8 <= end:
        pos = f.tell()
        size = struct.unpack(">I", f.read(4))[0]
        box_type = f.read(4).decode("latin1")
        if size == 1:
            size = struct.unpack(">Q", f.read(8))[0]
        elif size == 0:
            size = end - pos
        if size < 8 or pos + size > end:
            break
        if box_type == "mvhd":
            f.seek(pos + 4)
            version = f.read(1)[0]
            if version == 1:
                f.seek(pos + 20)
                timescale = struct.unpack(">I", f.read(4))[0]
                duration = struct.unpack(">Q", f.read(8))[0]
            else:
                f.seek(pos + 12)
                timescale = struct.unpack(">I", f.read(4))[0]
                duration = struct.unpack(">I", f.read(4))[0]
            results.append((pos, timescale, duration, duration / timescale))
        if box_type in ("moov", "trak", "mdia", "minf", "stbl", "edts"):
            read_boxes(f, pos + 8, pos + size, depth + 1, results)
        f.seek(pos + size)
    return results


path = r"outputs\portfolio-site\assets\media\hero.mp4"
with open(path, "rb") as f:
    f.seek(0, 2)
    length = f.tell()
    res = read_boxes(f, 0, length)
print("mvhd entries (offset, timescale, duration, seconds):")
for r in res:
    print(" ", r)
if res:
    print("max duration seconds:", round(max(x[3] for x in res), 2))
