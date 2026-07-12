#!/usr/bin/env python3
"""本地/局域网预览服务器：禁用 HTML 缓存，改完代码刷新即生效。"""
import http.server
import sys


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # HTML 一律不缓存；图片指纹不变，允许短缓存减少局域网流量
        if self.path.endswith(('.html', '/')) or '.' not in self.path.split('/')[-1].split('#')[0].split('?')[0]:
            self.send_header('Cache-Control', 'no-cache, must-revalidate')
        else:
            self.send_header('Cache-Control', 'max-age=300')
        super().end_headers()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8092
    http.server.ThreadingHTTPServer(('0.0.0.0', port), NoCacheHandler).serve_forever()
