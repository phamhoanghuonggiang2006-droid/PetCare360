# -*- coding: utf-8 -*-
CUSTOMER_HTML = """
    <!-- ======================================================== -->
    <!-- VIEW 1: GIAO DIỆN KHÁCH HÀNG (CUSTOMER VIEW - MẶC ĐỊNH) -->
    <!-- ======================================================== -->
    <div x-show="currentRole === 'customer'" class="min-h-screen flex flex-col pb-16 md:pb-0" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 scale-98" x-transition:enter-end="opacity-100 scale-100">
        
        <!-- Header Navigation Customer - Sticky On Scroll -->
        <header class="sticky top-0 z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-xs transition-all">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-16 sm:h-20 gap-4">
                    
                    <!-- Cột Trái: Logo Icon Dấu Chân Thú Cưng + Text PetCare360 bọc bằng Link to="/" -->
                    <a href="#/" @click.prevent="activeCustomerTab = 'home'" class="flex items-center gap-3 cursor-pointer group flex-shrink-0" title="PetCare360 - Về Trang Chủ">
                        <div class="w-10 h-10 sm:w-11 sm:h-11 rounded-2xl bg-gradient-to-tr from-[#F97316] to-amber-500 flex items-center justify-center text-white shadow-md shadow-orange-500/25 group-hover:scale-105 group-hover:rotate-6 transition-all duration-300">
                            <i class="fa-solid fa-paw text-xl"></i>
                        </div>
                        <div>
                            <span class="text-xl sm:text-2xl font-black tracking-tight text-slate-900">PetCare<span class="text-[#F97316]">360</span></span>
                            <span class="hidden sm:block text-[9px] font-extrabold text-slate-400 uppercase tracking-widest -mt-1">Pet Care Ecosystem</span>
                        </div>
                    </a>

                    <!-- Cột Giữa (Menu Navigation): "Sản phẩm", "Dịch vụ", "PetShare360", "PetCam360" (Đã xóa Trang chủ theo chuẩn UX) -->
                    <nav class="hidden md:flex items-center gap-1 lg:gap-2">

                        <button @click="activeCustomerTab = 'shop'" :class="activeCustomerTab === 'shop' ? 'text-[#F97316] bg-orange-50 font-bold' : 'text-slate-600 hover:text-[#F97316] hover:bg-slate-50'" class="px-3.5 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-box-open text-xs"></i>Sản phẩm
                        </button>
                        <button @click="activeCustomerTab = 'booking'" :class="activeCustomerTab === 'booking' ? 'text-[#F97316] bg-orange-50 font-bold' : 'text-slate-600 hover:text-[#F97316] hover:bg-slate-50'" class="px-3.5 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-scissors text-xs"></i>Dịch vụ
                        </button>
                        <button @click="activeCustomerTab = 'petshare'" :class="activeCustomerTab === 'petshare' ? 'text-[#F97316] bg-orange-50 font-bold' : 'text-slate-600 hover:text-[#F97316] hover:bg-slate-50'" class="px-3.5 py-2 rounded-xl text-xs lg:text-sm transition flex items-center gap-1.5 relative">
                            <i class="fa-solid fa-newspaper text-xs"></i>PetShare360
                            <span class="text-[9px] bg-rose-500 text-white font-bold px-1.5 py-0.2 rounded-full">Hot</span>
                        </button>
                        <!-- PetCam360: Mở modal nhập mã phòng Hotel để xem camera -->
                        <button @click="openPetCamModal()" class="px-3.5 py-2 rounded-xl text-xs lg:text-sm font-bold text-sky-700 bg-sky-50 hover:bg-sky-100 hover:text-sky-800 transition flex items-center gap-1.5 border border-sky-200 shadow-2xs">
                            <i class="fa-solid fa-video text-rose-500 animate-pulse"></i>PetCam360
                            <span class="text-[9px] bg-rose-600 text-white font-extrabold px-1.5 py-0.2 rounded-full uppercase tracking-tighter">Live 24/7</span>
                        </button>
                    </nav>

                    <!-- Cột Phải (User Actions): Icon "Đơn hàng", Icon "Tài khoản", Icon "Giỏ hàng" (Kèm badge chấm đỏ) -->
                    <div class="flex items-center gap-2 sm:gap-3">
                        <!-- Nút Chuyển sang Giao diện Admin Dashboard -->
                        <button @click="switchToAdmin()" class="hidden xl:flex px-3 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold transition items-center gap-1.5 shadow-sm border border-slate-700 group" title="Chuyển sang Admin Dashboard">
                            <i class="fa-solid fa-chart-pie text-sky-400 group-hover:rotate-12 transition"></i>
                            <span>Admin</span>
                            <span class="text-[9px] bg-sky-500 text-white font-black px-1.5 py-0.2 rounded-full uppercase">SaaS</span>
                        </button>

                        <!-- Nút Chat CSKH trực tiếp -->
                        <button @click="openCustomerSupportChat()" class="relative p-2.5 rounded-xl text-slate-700 hover:text-[#F97316] hover:bg-orange-50 transition border border-slate-200 flex items-center gap-1.5 group" title="Chat hỗ trợ CSKH 24/7">
                            <i class="fa-solid fa-headset text-base text-[#F97316] group-hover:scale-110 transition"></i>
                            <span class="hidden 2xl:inline text-xs font-bold text-slate-700">CSKH</span>
                            <span class="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                        </button>

                        <!-- Icon "Đơn hàng" bọc bằng Link to="/orders" -->
                        <a href="#/orders" @click.prevent="activeCustomerTab = 'orders'" class="relative p-2.5 rounded-xl text-slate-700 hover:text-[#F97316] hover:bg-orange-50 transition border border-slate-200" title="Đơn hàng của bạn (/orders)">
                            <i class="fa-solid fa-receipt text-base"></i>
                            <span class="absolute -top-1 -right-1 px-1.5 py-0.2 text-[9px] bg-amber-500 text-white font-extrabold rounded-full" x-text="customerOrders ? customerOrders.length : 2"></span>
                        </a>

                        <!-- Icon "Tài khoản" -->
                        <button @click="activeCustomerTab = 'account'; accountSubTab = 'info';" class="relative p-2.5 rounded-xl text-slate-700 hover:text-[#F97316] hover:bg-orange-50 transition border border-slate-200" title="Tài khoản cá nhân">
                            <i class="fa-solid fa-circle-user text-base"></i>
                        </button>

                        <!-- Icon "Giỏ hàng" (Kèm badge chấm đỏ đếm số lượng item, liên kết Global State) -->
                        <button @click="activeCustomerTab = 'cart'; cartStep = 1;" class="relative p-2.5 rounded-xl text-slate-700 hover:text-[#F97316] hover:bg-orange-50 transition border border-slate-200" title="Giỏ hàng của bạn">
                            <i class="fa-solid fa-cart-shopping text-base"></i>
                            <span x-show="cartItemsCount > 0" x-text="cartItemsCount" class="absolute -top-1.5 -right-1.5 bg-rose-500 text-white font-bold text-[10px] w-5 h-5 rounded-full flex items-center justify-center shadow-sm ring-2 ring-white animate-pulse"></span>
                        </button>

                        <!-- Khối Đăng Nhập / Thông Tin Avatar -->
                        <div class="pl-1 sm:pl-2 border-l border-slate-200">
                            <template x-if="!isAuth">
                                <button @click="openLoginModal()" class="flex items-center gap-1.5 bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-bold text-xs px-3 py-2 rounded-xl shadow-sm transition transform active:scale-95">
                                    <i class="fa-solid fa-right-to-bracket text-xs"></i>
                                    <span class="hidden sm:inline">Đăng nhập</span>
                                </button>
                            </template>
                            <template x-if="isAuth">
                                <div class="flex items-center gap-2">
                                    <div @click="activeCustomerTab = 'account'; accountSubTab = 'info';" class="flex items-center gap-2 cursor-pointer hover:opacity-85 transition" title="Hồ sơ tài khoản">
                                        <img :src="customerProfile.avatar" :alt="customerProfile.name" class="w-8 h-8 rounded-full object-cover border-2 border-orange-500 shadow-sm">
                                    </div>
                                </div>
                            </template>
                        </div>

                    </div>
                </div>
            </div>
        </header>

        <!-- Main Content Area Customer -->
        <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
            
            <!-- Safe Error Boundary Fallback Alert Component -->
            <template x-if="hasRenderError">
                <div class="mb-6 bg-rose-50 border-2 border-rose-300 rounded-2xl p-4 flex items-center justify-between text-rose-800 shadow-sm animate-fadeIn">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center text-lg flex-shrink-0">
                            <i class="fa-solid fa-shield-halved"></i>
                        </div>
                        <div>
                            <h4 class="font-extrabold text-sm text-rose-900">Chế độ Bảo vệ An toàn Giao diện (Error Boundary)</h4>
                            <p class="text-xs text-rose-700" x-text="renderErrorMessage || 'Hệ thống đã tự động cách ly sự cố hiển thị để các trang khác vẫn hoạt động bình thường.'"></p>
                        </div>
                    </div>
                    <button @click="resetRenderError()" class="px-4 py-2 bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs rounded-xl shadow-xs transition flex items-center gap-1.5 flex-shrink-0">
                        <i class="fa-solid fa-arrow-rotate-right"></i>
                        <span>Khôi phục giao diện</span>
                    </button>
                </div>
            </template>

            <!-- ======================================================== -->
            <!-- TAB 1: TRANG CHỦ (HOME) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'home'" class="space-y-12" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- 1. HERO BANNER: Full-width chứa tiêu đề khuyến mãi lớn, mô tả ngắn, và nút call-to-action "Xem Ngay" -->
                <div class="relative bg-gradient-to-r from-slate-900 via-orange-950 to-slate-900 rounded-3xl p-6 sm:p-10 lg:p-12 text-white shadow-2xl overflow-hidden border border-orange-500/20">
                    <div class="absolute -right-12 -bottom-12 w-96 h-96 bg-orange-500/20 rounded-full blur-3xl pointer-events-none"></div>
                    <div class="absolute -left-12 -top-12 w-80 h-80 bg-amber-500/15 rounded-full blur-3xl pointer-events-none"></div>
                    <div class="relative z-10 max-w-2xl space-y-4">
                        <div class="inline-flex items-center gap-2 bg-gradient-to-r from-orange-500 to-amber-500 text-white text-xs font-black px-3.5 py-1.5 rounded-full uppercase tracking-wider shadow-md">
                            <i class="fa-solid fa-fire text-amber-200 animate-pulse"></i>
                            <span>Đại Tiệc Siêu Sale PetCare360 • Giảm Đến 40%</span>
                        </div>
                        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black leading-tight tracking-tight">
                            Hệ Sinh Thái Chăm Sóc Thú Cưng Đẳng Cấp 5 Sao
                        </h1>
                        <p class="text-slate-300 text-sm sm:text-base leading-relaxed max-w-xl">
                            Điểm tựa yêu thương toàn diện: Sản phẩm dinh dưỡng nhập khẩu chính hãng, dịch vụ Spa & Grooming tạo kiểu Show, cùng hệ thống phòng lưu trú Pet Hotel có Camera Live Stream 24/7 xem tận mắt.
                        </p>
                        <div class="pt-2 flex flex-wrap items-center gap-3">
                            <button @click="activeCustomerTab = 'shop'" class="px-7 py-3.5 bg-gradient-to-r from-[#F97316] to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-extrabold text-sm rounded-2xl shadow-lg shadow-orange-500/30 transition transform hover:-translate-y-0.5 active:scale-95 flex items-center gap-2">
                                <span>Xem Ngay</span>
                                <i class="fa-solid fa-arrow-right text-xs"></i>
                            </button>
                            <button @click="activeCustomerTab = 'booking'" class="px-6 py-3.5 bg-white/10 hover:bg-white/20 text-white font-bold text-sm rounded-2xl backdrop-blur-md border border-white/20 transition flex items-center gap-2">
                                <i class="fa-solid fa-calendar-check text-[#F97316]"></i>
                                <span>Đặt Dịch Vụ</span>
                            </button>
                        </div>
                        <div class="pt-4 flex flex-wrap gap-6 text-xs text-slate-400 border-t border-white/10">
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-truck-fast text-[#F97316]"></i> Giao hỏa tốc 2H</span>
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-shield-check text-emerald-400"></i> 100% Chính hãng</span>
                            <span class="flex items-center gap-1.5"><i class="fa-solid fa-video text-sky-400"></i> Camera Live 24/7</span>
                        </div>
                    </div>
                </div>

                <!-- 2. SẢN PHẨM BÁN CHẠY: Layout 1 hàng ngang. Gọi API lấy đúng 4 sản phẩm (limit=4, sort theo order_count). Mép phải hàng có icon mũi tên để vuốt/click xem tiếp -->
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <div class="flex items-center gap-2">
                                <span class="w-2.5 h-6 bg-[#F97316] rounded-full inline-block"></span>
                                <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Sản Phẩm Bán Chạy</h2>
                                <span class="bg-rose-100 text-rose-700 text-[10px] font-black px-2 py-0.5 rounded-full uppercase">Top Bestseller</span>
                            </div>
                            <p class="text-xs text-slate-500 mt-1 ml-4.5">Được cộng đồng chủ nuôi yêu thích nhất tuần qua (Đúng 4 sản phẩm theo chuẩn E-commerce)</p>
                        </div>
                        
                        <!-- Mép phải hàng có icon mũi tên để vuốt/click xem tiếp (Carousel/Slider Controls) -->
                        <div class="flex items-center gap-2">
                            <button @click="scrollBestSellerLeft()" class="w-9 h-9 rounded-full border border-slate-200 bg-white hover:bg-orange-50 text-slate-600 hover:text-[#F97316] shadow-xs flex items-center justify-center transition active:scale-90" title="Lướt sang trái">
                                <i class="fa-solid fa-chevron-left text-xs"></i>
                            </button>
                            <button @click="scrollBestSellerRight()" class="w-9 h-9 rounded-full border border-slate-200 bg-white hover:bg-orange-50 text-slate-600 hover:text-[#F97316] shadow-xs flex items-center justify-center transition active:scale-90" title="Xem tiếp các sản phẩm (Carousel Next)">
                                <i class="fa-solid fa-chevron-right text-xs"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Layout 1 hàng ngang với 4 sản phẩm (limit=4, sort theo order_count) -->
                    <div id="homepage-bestseller-carousel" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                        <template x-for="prod in homeBestSellers" :key="'bestseller-' + prod.id">
                            <div @click="activeCustomerTab = 'shop'; openProductDetailPage(prod);" class="bg-white rounded-3xl p-3.5 border border-slate-200 shadow-xs hover:shadow-lg hover:border-orange-200 transition-all duration-200 flex flex-col justify-between group cursor-pointer relative overflow-hidden">
                                
                                <!-- Ảnh sản phẩm tỷ lệ chuẩn 1:1 + Badge giảm giá & Giao nhanh 2h -->
                                <div class="relative w-full aspect-square rounded-2xl overflow-hidden bg-slate-50 flex items-center justify-center p-3">
                                    <img :src="prod.image || prod.img" :alt="prod.name" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300">
                                    <span class="absolute top-2.5 left-2.5 bg-rose-600 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-md shadow-xs" x-text="prod.discountPercent || '-20%'"></span>
                                    <template x-if="prod.expressShip">
                                        <span class="absolute top-2.5 right-2.5 bg-amber-400 text-slate-900 font-black text-[9px] px-1.5 py-0.5 rounded-md shadow-xs flex items-center gap-0.5">
                                            <i class="fa-solid fa-bolt text-[8px]"></i> 2H
                                        </span>
                                    </template>
                                </div>

                                <!-- Component Thẻ Sản Phẩm: Tên, Giá, Nút Thêm vào giỏ -->
                                <div class="pt-3 pb-1 space-y-2 flex-1 flex flex-col justify-between">
                                    <div>
                                        <p class="text-[10px] font-bold text-slate-400 uppercase tracking-wider truncate" x-text="prod.brand || prod.category"></p>
                                        <h4 class="text-xs sm:text-sm font-bold text-slate-900 line-clamp-2 leading-snug group-hover:text-[#F97316] transition" x-text="prod.name" :title="prod.name"></h4>
                                    </div>

                                    <div>
                                        <!-- Đánh giá và số lượt mua -->
                                        <div class="flex items-center gap-1.5 text-xs text-slate-500 pt-1">
                                            <div class="flex items-center text-amber-400 text-xs">
                                                <i class="fa-solid fa-star"></i>
                                                <span class="font-bold text-slate-800 ml-1" x-text="prod.rating || 5.0"></span>
                                            </div>
                                            <span class="text-slate-300">•</span>
                                            <span class="text-[11px] text-slate-400" x-text="(prod.sold || prod.order_count || 128) + ' đã bán'"></span>
                                        </div>

                                        <!-- Giá nổi bật + Giá gốc + Nút Thêm vào giỏ -->
                                        <div class="pt-2 flex items-center justify-between border-t border-slate-100 mt-2">
                                            <div>
                                                <div class="text-sm sm:text-base font-black text-[#F97316]" x-text="formatCurrency(prod.price)"></div>
                                                <div class="text-[10px] text-slate-400 line-through font-medium" x-text="formatCurrency(prod.originalPrice || Math.round(prod.price * 1.25))"></div>
                                            </div>
                                            <button @click.stop="addToCart({ id: prod.id, name: prod.name, price: prod.price, image: prod.image || prod.img, weight: '3kg', flavor: 'Vị chuẩn' })" class="w-9 h-9 rounded-2xl bg-orange-50 text-[#F97316] hover:bg-[#F97316] hover:text-white transition flex items-center justify-center shadow-xs transform active:scale-90" title="Thêm vào giỏ hàng">
                                                <i class="fa-solid fa-cart-plus text-xs"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>

                <!-- 3. DỊCH VỤ NỔI BẬT: Layout Grid 3 cột tương ứng 3 thẻ: "Spa", "Grooming", "Hotel". Mỗi thẻ có Icon/Hình minh họa, Tên dịch vụ, Mô tả ngắn (Lưu ý: Không có dịch vụ thú y) -->
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <div class="flex items-center gap-2">
                                <span class="w-2.5 h-6 bg-teal-600 rounded-full inline-block"></span>
                                <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Dịch Vụ Nổi Bật</h2>
                                <span class="bg-teal-100 text-teal-800 text-[10px] font-black px-2 py-0.5 rounded-full uppercase">Chuẩn 5 Sao</span>
                            </div>
                            <p class="text-xs text-slate-500 mt-1 ml-4.5">Trải nghiệm chăm sóc cao cấp, tận tâm như thành viên trong gia đình</p>
                        </div>
                        <button @click="activeCustomerTab = 'booking'" class="text-xs font-bold text-teal-700 hover:underline flex items-center gap-1">
                            <span>Bảng giá chi tiết</span>
                            <i class="fa-solid fa-arrow-right text-[10px]"></i>
                        </button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        
                        <!-- Thẻ 1: "Spa" -->
                        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs hover:shadow-xl hover:border-teal-300 transition-all group flex flex-col justify-between">
                            <div class="space-y-4">
                                <div class="w-full h-44 rounded-2xl overflow-hidden bg-slate-100 relative">
                                    <img src="https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80" alt="Spa Thư Giãn Thú Cưng" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                                    <div class="absolute top-3 left-3 w-10 h-10 rounded-xl bg-white/90 backdrop-blur text-teal-600 flex items-center justify-center text-lg shadow-sm">
                                        <i class="fa-solid fa-bath"></i>
                                    </div>
                                    <span class="absolute top-3 right-3 bg-teal-600 text-white font-extrabold text-[10px] px-2.5 py-1 rounded-full uppercase">Thảo mộc Davis Mỹ</span>
                                </div>
                                <div class="space-y-1.5">
                                    <h3 class="text-lg font-black text-slate-900 group-hover:text-teal-700 transition">Spa Thư Giãn Bọt Khí Nano</h3>
                                    <p class="text-xs text-slate-500 leading-relaxed">
                                        Quy trình sục bọt khí siêu mịn Nano làm sạch sâu nang lông, tẩy sạch tế bào chết, xông tinh dầu thảo mộc hữu cơ phục hồi da lông bóng mượt và giảm căng thẳng cho bé cưng.
                                    </p>
                                </div>
                            </div>
                            <div class="pt-4 mt-2 border-t border-slate-100 flex items-center justify-between">
                                <span class="text-xs font-bold text-teal-700">Chỉ từ 150.000đ</span>
                                <button @click="activeCustomerTab = 'booking'; servicePricingTab = 'grooming';" class="px-4 py-2 bg-teal-50 hover:bg-teal-600 hover:text-white text-teal-700 font-bold text-xs rounded-xl transition flex items-center gap-1.5 shadow-2xs">
                                    <span>Đặt Lịch Spa</span>
                                    <i class="fa-solid fa-arrow-right text-[10px]"></i>
                                </button>
                            </div>
                        </div>

                        <!-- Thẻ 2: "Grooming" -->
                        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs hover:shadow-xl hover:border-orange-300 transition-all group flex flex-col justify-between">
                            <div class="space-y-4">
                                <div class="w-full h-44 rounded-2xl overflow-hidden bg-slate-100 relative">
                                    <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=600&q=80" alt="Grooming Cắt Tỉa Thú Cưng" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                                    <div class="absolute top-3 left-3 w-10 h-10 rounded-xl bg-white/90 backdrop-blur text-[#F97316] flex items-center justify-center text-lg shadow-sm">
                                        <i class="fa-solid fa-scissors"></i>
                                    </div>
                                    <span class="absolute top-3 right-3 bg-[#F97316] text-white font-extrabold text-[10px] px-2.5 py-1 rounded-full uppercase">Master Stylist</span>
                                </div>
                                <div class="space-y-1.5">
                                    <h3 class="text-lg font-black text-slate-900 group-hover:text-[#F97316] transition">Grooming Cắt Tỉa Stylist 5 Sao</h3>
                                    <p class="text-xs text-slate-500 leading-relaxed">
                                        Đội ngũ chuyên gia trên 8 năm kinh nghiệm tạo kiểu form chuẩn show (gấu bông, cừu non, sư tử), cạo vệ sinh móng tai, vắt tuyến hôi và khử khuẩn toàn diện tỉ mỉ từng chi tiết.
                                    </p>
                                </div>
                            </div>
                            <div class="pt-4 mt-2 border-t border-slate-100 flex items-center justify-between">
                                <span class="text-xs font-bold text-[#F97316]">Chỉ từ 220.000đ</span>
                                <button @click="activeCustomerTab = 'booking'; servicePricingTab = 'grooming';" class="px-4 py-2 bg-orange-50 hover:bg-[#F97316] hover:text-white text-[#F97316] font-bold text-xs rounded-xl transition flex items-center gap-1.5 shadow-2xs">
                                    <span>Đặt Lịch Grooming</span>
                                    <i class="fa-solid fa-arrow-right text-[10px]"></i>
                                </button>
                            </div>
                        </div>

                        <!-- Thẻ 3: "Hotel" -->
                        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs hover:shadow-xl hover:border-indigo-300 transition-all group flex flex-col justify-between">
                            <div class="space-y-4">
                                <div class="w-full h-44 rounded-2xl overflow-hidden bg-slate-100 relative">
                                    <img src="https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=600&q=80" alt="Khách Sạn Thú Cưng Pet Hotel 5 Sao" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                                    <div class="absolute top-3 left-3 w-10 h-10 rounded-xl bg-white/90 backdrop-blur text-indigo-600 flex items-center justify-center text-lg shadow-sm">
                                        <i class="fa-solid fa-hotel"></i>
                                    </div>
                                    <span class="absolute top-3 right-3 bg-indigo-600 text-white font-extrabold text-[10px] px-2.5 py-1 rounded-full uppercase">Camera Live 24/7</span>
                                </div>
                                <div class="space-y-1.5">
                                    <h3 class="text-lg font-black text-slate-900 group-hover:text-indigo-700 transition">Khách Sạn Thú Cưng Pet Hotel 5 Sao</h3>
                                    <p class="text-xs text-slate-500 leading-relaxed">
                                        Phòng lưu trú riêng biệt cách âm điều hòa 2 chiều 24/7, tiêu âm chống ồn, lọc không khí ion âm diệt khuẩn. Khách hàng được cấp mã xem Camera trực tuyến live stream mọi lúc.
                                    </p>
                                </div>
                            </div>
                            <div class="pt-4 mt-2 border-t border-slate-100 flex items-center justify-between">
                                <span class="text-xs font-bold text-indigo-700">Chỉ từ 180.000đ/ngày</span>
                                <button @click="activeCustomerTab = 'booking'; servicePricingTab = 'hotel';" class="px-4 py-2 bg-indigo-50 hover:bg-indigo-600 hover:text-white text-indigo-700 font-bold text-xs rounded-xl transition flex items-center gap-1.5 shadow-2xs">
                                    <span>Đặt Phòng Hotel</span>
                                    <i class="fa-solid fa-arrow-right text-[10px]"></i>
                                </button>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- 4. TOP BÀI VIẾT PETSHARE360: Layout Grid 4 cột. Gọi API lấy 4 bài viết (limit=4, sort theo view). Cấu trúc thẻ: Ảnh bìa (tỷ lệ 16:9), Ngày tháng, Tên bài (text-truncate 2 dòng max), Tóm tắt ngắn, Text link "Đọc tiếp ->" -->
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <div class="flex items-center gap-2">
                                <span class="w-2.5 h-6 bg-rose-500 rounded-full inline-block"></span>
                                <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Top Bài Viết PetShare360</h2>
                                <span class="bg-rose-100 text-rose-700 text-[10px] font-black px-2 py-0.5 rounded-full uppercase">Cẩm Nang Tri Thức</span>
                            </div>
                            <p class="text-xs text-slate-500 mt-1 ml-4.5">Được đọc và chia sẻ nhiều nhất từ các chuyên gia chăm sóc thú cưng</p>
                        </div>
                        <button @click="activeCustomerTab = 'petshare'" class="text-xs font-bold text-rose-600 hover:underline flex items-center gap-1">
                            <span>Vào PetShare360</span>
                            <i class="fa-solid fa-arrow-right text-[10px]"></i>
                        </button>
                    </div>

                    <!-- Layout Grid 4 cột: Đúng 4 bài viết (limit=4, sort theo view) -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                        <template x-for="art in topPetShareArticles" :key="'home-article-' + art.id">
                            <div @click="openArticleDetail(art)" class="bg-white rounded-3xl p-4 border border-slate-200 shadow-xs hover:shadow-lg hover:border-rose-200 transition-all flex flex-col justify-between group cursor-pointer">
                                <div class="space-y-3">
                                    <!-- Ảnh bìa tỷ lệ 16:9 -->
                                    <div class="w-full aspect-video rounded-2xl overflow-hidden bg-slate-100 relative">
                                        <img :src="art.image" :alt="art.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                                        <span class="absolute bottom-2 right-2 bg-black/60 backdrop-blur-xs text-white text-[10px] font-semibold px-2 py-0.5 rounded-md flex items-center gap-1">
                                            <i class="fa-solid fa-eye text-[9px]"></i>
                                            <span x-text="art.views || 1200"></span>
                                        </span>
                                    </div>

                                    <!-- Ngày tháng & Tên bài (text-truncate 2 dòng max) & Tóm tắt ngắn -->
                                    <div class="space-y-1.5">
                                        <div class="flex items-center gap-2 text-[11px] text-slate-400">
                                            <span class="text-rose-600 font-bold" x-text="art.category || 'Mẹo chăm sóc'"></span>
                                            <span>•</span>
                                            <span x-text="art.date"></span>
                                        </div>
                                        <h3 class="font-extrabold text-xs sm:text-sm text-slate-900 group-hover:text-rose-600 transition line-clamp-2 leading-snug" x-text="art.title" :title="art.title"></h3>
                                        <p class="text-[11px] text-slate-500 line-clamp-2 leading-relaxed" x-text="art.summary"></p>
                                    </div>
                                </div>

                                <!-- Text link "Đọc tiếp ->" -->
                                <div class="pt-3 border-t border-slate-100 mt-2">
                                    <span class="text-xs font-black text-rose-600 group-hover:text-rose-700 flex items-center gap-1">
                                        <span>Đọc tiếp</span>
                                        <i class="fa-solid fa-arrow-right text-[10px] transform group-hover:translate-x-1 transition-transform"></i>
                                    </span>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>

                <!-- 5. FAQ (CÂU HỎI THƯỜNG GẶP): Dạng Accordion gồm 5 chủ đề quan trọng về mua sắm, giao hàng, đổi trả (Loại bỏ các câu hỏi về y tế/khám bệnh) -->
                <div class="bg-white rounded-3xl p-6 sm:p-10 border border-slate-200 shadow-sm space-y-6">
                    <div class="text-center max-w-2xl mx-auto space-y-2">
                        <span class="bg-orange-100 text-[#F97316] text-[11px] font-black px-3 py-1 rounded-full uppercase tracking-wider">Hỗ Trợ Khách Hàng</span>
                        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">Câu Hỏi Thường Gặp (FAQ)</h2>
                        <p class="text-xs sm:text-sm text-slate-500">Giải đáp các thắc mắc phổ biến nhất về quy trình mua sắm, giao nhận hỏa tốc, tích lũy điểm và chính sách hoàn tiền tại PetCare360</p>
                    </div>

                    <!-- Accordion 5 chủ đề quan trọng -->
                    <div class="max-w-3xl mx-auto divide-y divide-slate-200 border-y border-slate-200">
                        <template x-for="(item, idx) in faqs" :key="'faq-' + idx">
                            <div class="py-4">
                                <button @click="toggleHomeFaq(idx)" class="w-full flex items-center justify-between text-left gap-4 group focus:outline-none">
                                    <span class="font-extrabold text-xs sm:text-sm text-slate-800 group-hover:text-[#F97316] transition flex items-center gap-2.5">
                                        <span class="w-6 h-6 rounded-full bg-orange-100 text-[#F97316] text-xs font-black flex items-center justify-center flex-shrink-0" x-text="idx + 1"></span>
                                        <span x-text="item.q || item.question"></span>
                                    </span>
                                    <div class="w-7 h-7 rounded-full bg-slate-100 group-hover:bg-orange-100 text-slate-500 group-hover:text-[#F97316] flex items-center justify-center transition flex-shrink-0">
                                        <i class="fa-solid fa-chevron-down text-xs transition-transform duration-200" :class="homeFaqActiveIndex === idx ? 'rotate-180 text-[#F97316]' : ''"></i>
                                    </div>
                                </button>
                                <div x-show="homeFaqActiveIndex === idx" x-cloak x-collapse class="pt-3 pl-8.5 pr-4 text-xs text-slate-600 leading-relaxed">
                                    <div class="p-3.5 bg-slate-50 rounded-2xl border border-slate-100" x-text="item.a || item.answer"></div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>

            </div>

            <!-- ======================================================== -->
            <!-- TAB 2: SẢN PHẨM (CHUẨN E-COMMERCE CHUYÊN NGHIỆP THEO YÊU CẦU) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'shop'" class="space-y-8" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- ======================================================== -->
                <!-- CHẾ ĐỘ 1: GIAO DIỆN SHOP - TRANG DANH SÁCH SẢN PHẨM (SHOP CATALOG PAGE) -->
                <!-- ======================================================== -->
                <div x-show="shopViewMode === 'catalog'" class="space-y-8 animate-fadeIn">
                    
                    <!-- BANNER KHUYẾN MÃI NGANG (HERO PROMO BANNER) -->
                    <!-- Hình ảnh ưu đãi hạt và phụ kiện giảm 30%, tiêu đề nổi bật, nút "Mua Ngay" -->
                    <div class="relative bg-gradient-to-r from-orange-600 via-amber-500 to-rose-600 rounded-3xl p-6 sm:p-10 text-white shadow-xl overflow-hidden">
                        <div class="absolute -right-10 -bottom-10 w-96 h-96 bg-white/10 rounded-full blur-3xl pointer-events-none"></div>
                        <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-6">
                            <div class="space-y-3 max-w-xl text-center md:text-left">
                                <div class="inline-flex items-center gap-2 bg-white/20 backdrop-blur-md px-3.5 py-1 rounded-full text-xs font-black tracking-wider uppercase shadow-sm">
                                    <i class="fa-solid fa-fire text-amber-300 animate-pulse"></i>
                                    <span>Ưu Đãi Lớn Tháng 10 • Giảm Đến 30% Hạt & Phụ Kiện</span>
                                </div>
                                <h2 class="text-2xl sm:text-3xl lg:text-4xl font-black tracking-tight leading-tight">
                                    Đại Tiệc Hạt Dinh Dưỡng & Phụ Kiện Thú Cưng 5 Sao
                                </h2>
                                <p class="text-xs sm:text-sm text-white/95 leading-relaxed">
                                    Ưu đãi độc quyền cho Boss cưng: Giảm 30% toàn bộ hạt Royal Canin, Orijen, Pate Monge cao cấp và phụ kiện thú cưng nhập khẩu. Cam kết 100% chính hãng, tích điểm VIP và giao hàng nhanh PetShip360 chỉ 2 giờ!
                                </p>
                                <div class="pt-2 flex flex-wrap items-center justify-center md:justify-start gap-4">
                                    <button @click="scrollToCatalogGrid()" class="px-7 py-3.5 bg-white text-orange-600 hover:bg-orange-50 font-extrabold text-sm rounded-2xl shadow-xl transition transform active:scale-95 flex items-center gap-2">
                                        <span>MUA NGAY</span>
                                        <i class="fa-solid fa-arrow-right"></i>
                                    </button>
                                    <div class="flex items-center gap-3 text-xs text-white font-medium">
                                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-bolt text-amber-300"></i> Giao hỏa tốc 2H</span>
                                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-shield-check text-emerald-300"></i> Đổi trả 3 ngày</span>
                                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-circle-check text-blue-200"></i> 100% Chính hãng</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Hình ảnh ưu đãi hạt & phụ kiện -->
                            <div class="relative flex-shrink-0">
                                <div class="w-64 h-48 sm:w-80 sm:h-56 relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white/25 bg-white/10 backdrop-blur-sm flex items-center justify-center group">
                                    <img src="https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=600&q=80" alt="Ưu đãi hạt và phụ kiện giảm 30%" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                                    <div class="absolute top-3 right-3 bg-rose-600 text-white font-black text-xs sm:text-sm px-3 py-1 rounded-xl shadow-lg animate-bounce">
                                        GIẢM 30%
                                    </div>
                                    <div class="absolute bottom-3 left-3 bg-slate-900/80 backdrop-blur-md text-white text-[10px] font-bold px-2.5 py-1 rounded-lg">
                                        Hạt & Phụ kiện chính hãng
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- BỐ CỤC 2 CỘT BÊN DƯỚI: Sidebar Filter (280px) + Product Grid (1100px) -->
                    <div id="shopCatalogSection" class="flex flex-col lg:flex-row gap-8 items-start">
                        
                        <!-- CỘT BÊN TRÁI: SIDEBAR FILTER (RỘNG 280PX) -->
                        <aside class="w-full lg:w-[280px] flex-shrink-0 bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-6">
                            <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                <div class="flex items-center gap-2 font-bold text-sm text-[#1E293B]">
                                    <i class="fa-solid fa-sliders text-[#F97316]"></i>
                                    <span>Bộ Lọc Sản Phẩm</span>
                                </div>
                                <button @click="resetShopFilters()" class="text-[11px] text-slate-400 hover:text-orange-600 font-medium transition flex items-center gap-1">
                                    <i class="fa-solid fa-rotate-left text-[10px]"></i> Đặt lại
                                </button>
                            </div>

                            <!-- Nhóm 1: Loài thú cưng (Chó, Mèo, Thỏ) -->
                            <div class="space-y-2.5">
                                <label class="block text-xs font-bold text-[#1E293B] uppercase tracking-wider">Loài Thú Cưng</label>
                                <div class="flex flex-wrap gap-1.5">
                                    <button @click="shopSpecies = ''" :class="shopSpecies === '' ? 'bg-[#F97316] text-white font-bold shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'" class="px-3 py-1.5 rounded-xl text-xs transition">
                                        Tất cả
                                    </button>
                                    <button @click="shopSpecies = 'Chó'" :class="shopSpecies === 'Chó' ? 'bg-[#F97316] text-white font-bold shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'" class="px-3 py-1.5 rounded-xl text-xs transition flex items-center gap-1">
                                        <i class="fa-solid fa-dog text-[11px]"></i> Chó
                                    </button>
                                    <button @click="shopSpecies = 'Mèo'" :class="shopSpecies === 'Mèo' ? 'bg-[#F97316] text-white font-bold shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'" class="px-3 py-1.5 rounded-xl text-xs transition flex items-center gap-1">
                                        <i class="fa-solid fa-cat text-[11px]"></i> Mèo
                                    </button>
                                    <button @click="shopSpecies = 'Thỏ'" :class="shopSpecies === 'Thỏ' ? 'bg-[#F97316] text-white font-bold shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'" class="px-3 py-1.5 rounded-xl text-xs transition">
                                        Thỏ
                                    </button>
                                </div>
                            </div>

                            <!-- Nhóm 2: Loại sản phẩm (Thức ăn hạt, Pate, Cát vệ sinh, Phụ kiện & Đồ chơi, Thuốc thú y) -->
                            <div class="space-y-2.5 pt-3 border-t border-slate-100">
                                <label class="block text-xs font-bold text-[#1E293B] uppercase tracking-wider">Loại Sản Phẩm</label>
                                <div class="space-y-1.5 text-xs">
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === '' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Tất cả phân loại</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Thức ăn hạt" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Thức ăn hạt' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Thức ăn hạt</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Pate" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Pate' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Pate</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Cát vệ sinh" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Cát vệ sinh' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Cát vệ sinh</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Phụ kiện & Đồ chơi" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Phụ kiện & Đồ chơi' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Phụ kiện & Đồ chơi</span>
                                    </label>
                                    <label class="flex items-center gap-2 p-1.5 rounded-xl hover:bg-slate-50 cursor-pointer transition">
                                        <input type="radio" name="prodType" value="Thuốc thú y" x-model="shopProductType" class="text-orange-500 focus:ring-orange-400">
                                        <span :class="shopProductType === 'Thuốc thú y' ? 'font-bold text-[#F97316]' : 'text-slate-700'">Thuốc thú y</span>
                                    </label>
                                </div>
                            </div>

                            <!-- Nhóm 3: Thương hiệu -->
                            <div class="space-y-2.5 pt-3 border-t border-slate-100">
                                <label class="block text-xs font-bold text-[#1E293B] uppercase tracking-wider">Thương Hiệu</label>
                                <select x-model="shopBrand" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-400">
                                    <option value="">Tất cả thương hiệu</option>
                                    <option value="Royal Canin">Royal Canin (Pháp)</option>
                                    <option value="Orijen">Orijen (Canada)</option>
                                    <option value="Monge">Monge (Ý)</option>
                                    <option value="Ciao Churu">Ciao Churu (Nhật)</option>
                                    <option value="Cature">Cature (Mỹ)</option>
                                    <option value="Davis">Davis (Mỹ)</option>
                                    <option value="Virbac">Virbac (Pháp)</option>
                                    <option value="Boehringer Ingelheim">Boehringer Ingelheim</option>
                                    <option value="Zoetis">Zoetis (Mỹ)</option>
                                </select>
                            </div>

                            <!-- Nhóm 4: Mức giá (Slider) -->
                            <div class="space-y-2.5 pt-3 border-t border-slate-100">
                                <div class="flex items-center justify-between text-xs">
                                    <label class="font-bold text-[#1E293B] uppercase tracking-wider">Mức Giá Tối Đa</label>
                                    <span class="font-extrabold text-[#F97316]" x-text="formatCurrency(shopMaxPrice)"></span>
                                </div>
                                <input type="range" min="100000" max="1500000" step="50000" x-model.number="shopMaxPrice" class="w-full accent-[#F97316] cursor-pointer">
                                <div class="flex justify-between text-[10px] text-slate-400">
                                    <span>100.000đ</span>
                                    <span>1.500.000đ</span>
                                </div>
                            </div>

                            <!-- Nhóm 5: Checkbox "Giao hỏa tốc PetShip360" -->
                            <div class="pt-3 border-t border-slate-100">
                                <label class="flex items-center gap-2.5 p-3 rounded-2xl bg-orange-50/70 border border-orange-200 hover:bg-orange-100/60 cursor-pointer transition">
                                    <input type="checkbox" x-model="shopExpressShip" class="rounded text-[#F97316] focus:ring-orange-400 w-4 h-4">
                                    <div class="text-xs">
                                        <span class="font-extrabold text-slate-800 flex items-center gap-1">
                                            <i class="fa-solid fa-bolt text-[#F97316]"></i>
                                            <span>Giao hỏa tốc PetShip360</span>
                                        </span>
                                        <span class="text-[10px] text-orange-700 block mt-0.5">Nhận hàng trong 2 Giờ tại nội thành</span>
                                    </div>
                                </label>
                            </div>
                        </aside>

                        <!-- CỘT BÊN PHẢI: PRODUCT GRID (RỘNG 1100PX) -->
                        <div class="flex-1 w-full space-y-6">
                            
                            <!-- Thanh Sắp Xếp Phía Trên -->
                            <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                <div class="flex items-center gap-2 text-xs sm:text-sm">
                                    <span class="font-bold text-[#1E293B]">Hiển thị:</span>
                                    <span class="text-[#F97316] font-extrabold" x-text="filteredCatalogProducts.length + ' sản phẩm'"></span>
                                    <span class="text-slate-400 hidden sm:inline">• Nền trắng #FFFFFF, Màu nhấn Cam #F97316</span>
                                </div>

                                <!-- "Xếp theo: Mới nhất | Bán chạy | Giá tăng/giảm" -->
                                <div class="flex items-center gap-2 text-xs">
                                    <span class="text-slate-500 font-medium">Xếp theo:</span>
                                    <div class="flex items-center gap-1 bg-slate-100 p-1 rounded-xl">
                                        <button @click="shopSortBy = 'newest'" :class="shopSortBy === 'newest' ? 'bg-white text-[#F97316] font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition">
                                            Mới nhất
                                        </button>
                                        <button @click="shopSortBy = 'bestseller'" :class="shopSortBy === 'bestseller' ? 'bg-white text-[#F97316] font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition">
                                            Bán chạy
                                        </button>
                                        <button @click="shopSortBy = 'price_asc'" :class="shopSortBy === 'price_asc' ? 'bg-white text-[#F97316] font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition flex items-center gap-1">
                                            Giá <i class="fa-solid fa-arrow-up text-[10px]"></i>
                                        </button>
                                        <button @click="shopSortBy = 'price_desc'" :class="shopSortBy === 'price_desc' ? 'bg-white text-[#F97316] font-bold shadow-sm' : 'text-slate-600 hover:text-slate-900'" class="px-3 py-1.5 rounded-lg transition flex items-center gap-1">
                                            Giá <i class="fa-solid fa-arrow-down text-[10px]"></i>
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- LƯỚI SẢN PHẨM: 4 CỘT X 3 HÀNG (12 SẢN PHẨM) -->
                            <!-- Card sản phẩm: Tỷ lệ ảnh 1:1, Badge giảm giá đỏ góc trên, Tên thương hiệu nhạt, Tên sản phẩm (tối đa 2 dòng), Số sao đánh giá (4.9★ - 128 đã bán), Giá bán in đậm đỏ/cam + Giá gốc gạch ngang, Nút tròn icon Giỏ hàng góc dưới -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-4">
                                <template x-for="prod in paginatedCatalogProducts" :key="prod.id">
                                    <div @click="openProductDetailPage(prod)" class="bg-white rounded-2xl p-3 border border-slate-200 shadow-sm hover:shadow-lg transition-all duration-200 flex flex-col justify-between group cursor-pointer relative overflow-hidden">
                                        
                                        <!-- Ảnh 1:1 + Badge giảm giá đỏ góc trên -->
                                        <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-50 flex items-center justify-center p-2">
                                            <img :src="prod.image || prod.img" :alt="prod.name" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300">
                                            
                                            <!-- Badge giảm giá đỏ góc trên -->
                                            <span class="absolute top-2 left-2 bg-rose-600 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-md shadow-sm" x-text="prod.discountPercent || '-20%'"></span>

                                            <!-- Badge Giao hỏa tốc nếu có -->
                                            <template x-if="prod.expressShip">
                                                <span class="absolute top-2 right-2 bg-amber-400 text-slate-900 font-black text-[9px] px-1.5 py-0.5 rounded-md shadow-sm flex items-center gap-0.5" title="Giao hỏa tốc PetShip360 trong 2h">
                                                    <i class="fa-solid fa-bolt text-[8px]"></i> 2H
                                                </span>
                                            </template>
                                        </div>

                                        <!-- Thông tin sản phẩm -->
                                        <div class="pt-3 pb-1 space-y-1.5 flex-1 flex flex-col justify-between">
                                            <div>
                                                <!-- Tên thương hiệu nhạt -->
                                                <p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider truncate" x-text="prod.brand"></p>
                                                
                                                <!-- Tên sản phẩm (tối đa 2 dòng) -->
                                                <h4 class="text-xs sm:text-sm font-bold text-[#1E293B] line-clamp-2 leading-snug group-hover:text-[#F97316] transition" x-text="prod.name" :title="prod.name"></h4>
                                            </div>

                                            <div>
                                                <!-- Số sao đánh giá (ví dụ: 4.9★ - 128 đã bán) -->
                                                <div class="flex items-center gap-1.5 text-xs text-slate-500 pt-1">
                                                    <div class="flex items-center text-amber-400 text-xs">
                                                        <i class="fa-solid fa-star"></i>
                                                        <span class="font-bold text-slate-800 ml-1" x-text="prod.rating"></span>
                                                    </div>
                                                    <span class="text-slate-300">•</span>
                                                    <span class="text-[11px] text-slate-400" x-text="(prod.sold || 128) + ' đã bán'"></span>
                                                </div>

                                                <!-- Giá bán in đậm đỏ/cam + Giá gốc gạch ngang + Nút tròn icon Giỏ hàng góc dưới -->
                                                <div class="pt-2 flex items-center justify-between border-t border-slate-100 mt-2">
                                                    <div>
                                                        <div class="text-sm sm:text-base font-extrabold text-[#F97316]" x-text="formatCurrency(prod.price)"></div>
                                                        <div class="text-[10px] text-slate-400 line-through font-medium" x-text="formatCurrency(prod.originalPrice || Math.round(prod.price * 1.25))"></div>
                                                    </div>

                                                    <!-- Nút tròn icon Giỏ hàng góc dưới -->
                                                    <button @click.stop="addToCart({ id: prod.id, name: prod.name, price: prod.price, image: prod.image || prod.img, weight: '3kg', flavor: 'Vị chuẩn' })" class="w-9 h-9 rounded-full bg-orange-50 text-[#F97316] hover:bg-[#F97316] hover:text-white transition flex items-center justify-center shadow-sm transform active:scale-90" title="Thêm vào giỏ hàng">
                                                        <i class="fa-solid fa-cart-plus text-xs"></i>
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </template>
                            </div>

                            <!-- Phân trang (Pagination) chuẩn ở cuối trang -->
                            <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-sm flex items-center justify-between">
                                <span class="text-xs text-slate-500 hidden sm:inline" x-text="'Trang ' + shopCurrentPage + ' / ' + shopTotalPages + ' (Tổng ' + filteredCatalogProducts.length + ' sản phẩm)'"></span>
                                <div class="flex items-center gap-1.5 mx-auto sm:mx-0">
                                    <button @click="if(shopCurrentPage > 1) shopCurrentPage--" :disabled="shopCurrentPage === 1" class="px-3 py-1.5 rounded-xl border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed transition flex items-center gap-1">
                                        <i class="fa-solid fa-chevron-left text-[10px]"></i>
                                        <span>Trang trước</span>
                                    </button>
                                    <template x-for="p in shopTotalPages" :key="p">
                                        <button @click="shopCurrentPage = p" :class="shopCurrentPage === p ? 'bg-[#F97316] text-white font-bold' : 'bg-white border border-slate-200 text-slate-700 hover:bg-slate-50'" class="w-8 h-8 rounded-xl text-xs transition font-semibold" x-text="p"></button>
                                    </template>
                                    <button @click="if(shopCurrentPage < shopTotalPages) shopCurrentPage++" :disabled="shopCurrentPage === shopTotalPages" class="px-3 py-1.5 rounded-xl border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed transition flex items-center gap-1">
                                        <span>Trang sau</span>
                                        <i class="fa-solid fa-chevron-right text-[10px]"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ======================================================== -->
                <!-- CHẾ ĐỘ 2: TRANG CHI TIẾT SẢN PHẨM (PRODUCT DETAIL PAGE) -->
                <!-- ======================================================== -->
                <div x-show="shopViewMode === 'detail'" class="space-y-8 animate-fadeIn">
                    <nav class="flex items-center gap-2 text-xs sm:text-sm text-slate-500 py-2 border-b border-slate-100">
                    <a href="#" @click.prevent="activeCustomerTab = 'home'" class="hover:text-brand-600 transition flex items-center gap-1">
                        <i class="fa-solid fa-house text-xs"></i>Trang chủ
                    </a>
                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
                    <a href="#" @click.prevent="backToShopCatalog()" class="hover:text-orange-600 font-bold text-slate-700 transition flex items-center gap-1"><i class="fa-solid fa-box-open text-xs"></i>Sản phẩm (Cửa hàng)</a>
                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
                    <span class="text-slate-600 font-medium">Thức ăn thú cưng</span>
                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
                    <span class="text-slate-900 font-bold truncate max-w-xs" x-text="currentProductDetail.name"></span>
                </nav>

                <!-- BỐ CỤC CHÍNH 2 CỘT (THẺ SẢN PHẨM CHÍNH) -->
                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm">
                    <div class="flex flex-col lg:flex-row gap-8 lg:gap-12 items-start justify-center">
                        
                        <!-- CỘT TRÁI (GALLERY ẢNH - 500PX) -->
                        <div class="w-full lg:w-[500px] flex-shrink-0 space-y-4">
                            <!-- Ảnh lớn trung tâm -->
                            <div class="relative w-full h-[360px] sm:h-[420px] rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 group flex items-center justify-center p-4">
                                <img :src="mainProductImage" :alt="currentProductDetail.name" class="w-full h-full object-contain transform group-hover:scale-105 transition duration-300">
                                <div class="absolute top-3 left-3 bg-rose-500 text-white text-xs font-black px-2.5 py-1 rounded-lg uppercase tracking-wider shadow">
                                    -18% GIẢM
                                </div>
                                <div class="absolute top-3 right-3 bg-white/90 backdrop-blur text-slate-600 p-2 rounded-xl shadow hover:text-rose-500 cursor-pointer transition">
                                    <i class="fa-regular fa-heart text-base"></i>
                                </div>
                            </div>

                            <!-- Dãy 4 ảnh nhỏ thumbnail ở bên dưới để click chuyển ảnh -->
                            <div class="grid grid-cols-4 gap-3">
                                <template x-for="(thumb, index) in productThumbnails" :key="index">
                                    <button @click="mainProductImage = thumb" :class="mainProductImage === thumb ? 'border-2 border-orange-500 ring-2 ring-orange-200 shadow' : 'border border-slate-200 hover:border-slate-300 opacity-75 hover:opacity-100'" class="h-20 sm:h-24 rounded-xl overflow-hidden bg-slate-50 p-1 transition flex items-center justify-center">
                                        <img :src="thumb" class="w-full h-full object-cover rounded-lg">
                                    </button>
                                </template>
                            </div>
                        </div>

                        <!-- CỘT PHẢI (THÔNG TIN MUA HÀNG - 600PX) -->
                        <div class="w-full lg:w-[600px] flex-shrink-0 space-y-5">
                            
                            <!-- Tên sản phẩm to rõ (Font 24px, Bold) -->
                            <h1 class="text-2xl sm:text-[24px] font-bold text-slate-900 leading-snug tracking-tight" x-text="currentProductDetail.name"></h1>

                            <!-- Khối Đánh giá (4.8/5 sao - 86 nhận xét) + Mã SKU + Tình trạng -->
                            <div class="flex flex-wrap items-center gap-3 text-xs sm:text-sm text-slate-500 pb-3 border-b border-slate-100">
                                <div class="flex items-center gap-1.5 text-amber-500">
                                    <div class="flex text-sm">
                                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i>
                                    </div>
                                    <span class="font-bold text-slate-800">4.8 / 5</span>
                                    <span class="text-slate-400">(86 nhận xét)</span>
                                </div>
                                <span class="text-slate-300">|</span>
                                <div class="font-mono text-slate-600">
                                    SKU: <span class="font-semibold text-slate-800">PC360-RC-MA01</span>
                                </div>
                                <span class="text-slate-300">|</span>
                                <div class="inline-flex items-center gap-1.5 text-emerald-600 font-semibold bg-emerald-50 px-2.5 py-0.5 rounded-full text-xs">
                                    <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                                    <span>Còn hàng (24 bao trong kho)</span>
                                </div>
                            </div>

                            <!-- Khối Bảng Giá: Giá khuyến mãi to nổi bật (màu Cam), Giá niêm yết gạch ngang (Dynamic Realtime Price) -->
                            <div class="bg-orange-50/60 rounded-2xl p-4 sm:p-5 border border-orange-100 flex items-baseline gap-4">
                                <div class="text-3xl sm:text-4xl font-extrabold text-orange-600 tracking-tight" x-text="formatCurrency(currentProductDetailTotalPrice)"></div>
                                <div class="text-base sm:text-lg text-slate-400 line-through font-medium" x-text="formatCurrency(currentProductOriginalPrice * (productDetailQty || 1))"></div>
                                <span class="bg-orange-500 text-white text-xs font-bold px-2 py-0.5 rounded-md shadow-sm">Tiết kiệm 75.000đ</span>
                            </div>

                            <!-- Bộ chọn Biến thể (Variants selector có Conditional Rendering theo variantConfig) -->
                            <div class="space-y-4 pt-1">
                                <!-- Khối chọn Trọng lượng (Chỉ render nếu variantConfig có weights) -->
                                <template x-if="currentProductDetail.variantConfig && currentProductDetail.variantConfig.weights && currentProductDetail.variantConfig.weights.length > 0">
                                    <div>
                                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">Chọn Trọng Lượng:</label>
                                        <div class="flex flex-wrap gap-2.5">
                                            <template x-for="w in currentProductDetail.variantConfig.weights" :key="w.label">
                                                <button type="button" @click="selectProductWeight(w)" :class="selectedWeight === w.label ? 'border-2 border-orange-500 bg-orange-50 text-orange-700 font-bold shadow-sm' : 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300'" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm transition flex items-center gap-1.5">
                                                    <span x-text="w.label + (w.sub ? (' (' + w.sub + ')') : '')"></span>
                                                    <template x-if="w.tag">
                                                        <span class="text-[9px] bg-orange-500 text-white font-bold px-1.5 py-0.2 rounded-full" x-text="w.tag"></span>
                                                    </template>
                                                </button>
                                            </template>
                                        </div>
                                    </div>
                                </template>

                                <!-- Khối chọn Hương vị (Chỉ render nếu variantConfig có flavors) -->
                                <template x-if="currentProductDetail.variantConfig && currentProductDetail.variantConfig.flavors && currentProductDetail.variantConfig.flavors.length > 0">
                                    <div>
                                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">Chọn Hương Vị:</label>
                                        <div class="flex flex-wrap gap-2.5">
                                            <template x-for="fl in currentProductDetail.variantConfig.flavors" :key="fl.id">
                                                <button type="button" @click="selectedFlavor = fl.id" :class="selectedFlavor === fl.id ? 'border-2 border-orange-500 bg-orange-50 text-orange-700 font-bold shadow-sm' : 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300'" class="px-4 py-2.5 rounded-xl text-xs sm:text-sm transition flex items-center gap-2">
                                                    <i class="fa-solid fa-bone text-brand-600"></i>
                                                    <span x-text="fl.label"></span>
                                                </button>
                                            </template>
                                        </div>
                                    </div>
                                </template>

                                <!-- Bộ chọn Số lượng (Nút - 1 +) -->
                                <div class="pt-2 flex items-center gap-4">
                                    <label class="text-xs font-bold text-slate-700 uppercase tracking-wider">Số lượng:</label>
                                    <div class="flex items-center border border-slate-300 rounded-xl overflow-hidden bg-white shadow-sm">
                                        <button @click="if (productDetailQty > 1) productDetailQty--" class="w-10 h-10 flex items-center justify-center text-slate-600 hover:bg-slate-100 transition font-bold text-base select-none">−</button>
                                        <input type="number" min="1" max="99" x-model.number="productDetailQty" class="w-14 h-10 text-center font-bold text-slate-800 text-sm focus:outline-none border-x border-slate-200">
                                        <button @click="productDetailQty++" class="w-10 h-10 flex items-center justify-center text-slate-600 hover:bg-slate-100 transition font-bold text-base select-none">+</button>
                                    </div>
                                    <span class="text-xs text-slate-400">Kho sẵn sàng giao trong 2h</span>
                                </div>
                            </div>

                            <!-- Khối Nút Thao Tác: Thêm Vào Giỏ (Viền cam) & MUA NGAY (Nền cam chữ trắng to) -->
                            <div class="pt-4 flex flex-col sm:flex-row gap-3">
                                <button @click="addProductDetailToCart()" class="flex-1 py-3.5 px-6 rounded-2xl border-2 border-orange-500 text-orange-600 hover:bg-orange-50 font-bold text-sm sm:text-base transition flex items-center justify-center gap-2 shadow-sm">
                                    <i class="fa-solid fa-cart-plus text-base"></i>
                                    <span>Thêm Vào Giỏ Hàng</span>
                                </button>
                                <button @click="buyNowProductDetail()" class="flex-1 py-3.5 px-6 rounded-2xl bg-orange-500 hover:bg-orange-600 text-white font-extrabold text-sm sm:text-base transition shadow-lg shadow-orange-500/30 flex items-center justify-center gap-2 transform active:scale-98">
                                    <i class="fa-solid fa-bolt text-base"></i>
                                    <span>MUA NGAY</span>
                                </button>
                            </div>

                            <!-- Khối Badge Cam Kết -->
                            <div class="pt-4 border-t border-slate-100 grid grid-cols-3 gap-3 text-center">
                                <div class="p-3 bg-slate-50 rounded-2xl border border-slate-100 space-y-1">
                                    <i class="fa-solid fa-shield-halved text-brand-600 text-lg"></i>
                                    <p class="text-xs font-bold text-slate-800">Chính hãng 100%</p>
                                    <p class="text-[10px] text-slate-400">Đầy đủ tem phụ & Hóa đơn</p>
                                </div>
                                <div class="p-3 bg-slate-50 rounded-2xl border border-slate-100 space-y-1">
                                    <i class="fa-solid fa-rotate-left text-teal-600 text-lg"></i>
                                    <p class="text-xs font-bold text-slate-800">Đổi trả 3 ngày</p>
                                    <p class="text-[10px] text-slate-400">Nếu bé dị ứng hạt</p>
                                </div>
                                <div class="p-3 bg-slate-50 rounded-2xl border border-slate-100 space-y-1">
                                    <i class="fa-solid fa-truck-fast text-orange-600 text-lg"></i>
                                    <p class="text-xs font-bold text-slate-800">Giao PetShip 2H</p>
                                    <p class="text-[10px] text-slate-400">Hỏa tốc nội thành</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- PHẦN BÊN DƯỚI (TABS THÔNG TIN CHI TIẾT) -->
                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                    <!-- Tab Headers -->
                    <div class="flex border-b border-slate-200 gap-6 sm:gap-8 overflow-x-auto text-sm sm:text-base font-bold">
                        <button @click="productDetailTab = 'desc'" :class="productDetailTab === 'desc' ? 'text-orange-600 border-b-2 border-orange-500 pb-3' : 'text-slate-500 hover:text-slate-800 pb-3'" class="transition whitespace-nowrap">
                            <i class="fa-solid fa-circle-info mr-1.5"></i>Mô Tả & Thành Phần Dinh Dưỡng
                        </button>
                        <button @click="productDetailTab = 'guide'" :class="productDetailTab === 'guide' ? 'text-orange-600 border-b-2 border-orange-500 pb-3' : 'text-slate-500 hover:text-slate-800 pb-3'" class="transition whitespace-nowrap">
                            <i class="fa-solid fa-scale-balanced mr-1.5"></i>Hướng Dẫn Cho Ăn Theo Cân Nặng
                        </button>
                        <button @click="productDetailTab = 'reviews'" :class="productDetailTab === 'reviews' ? 'text-orange-600 border-b-2 border-orange-500 pb-3' : 'text-slate-500 hover:text-slate-800 pb-3'" class="transition whitespace-nowrap flex items-center gap-1.5">
                            <i class="fa-solid fa-comments mr-1"></i>Đánh Giá Từ Khách Hàng
                            <span class="bg-orange-100 text-orange-700 text-xs px-2 py-0.5 rounded-full font-bold">86</span>
                        </button>
                    </div>

                    <!-- TAB 1: Mô tả chi tiết sản phẩm & Thành phần dinh dưỡng -->
                    <div x-show="productDetailTab === 'desc'" class="space-y-6 text-sm text-slate-700 leading-relaxed animate-fadeIn">
                        <div>
                            <h4 class="font-bold text-base text-slate-900 mb-2">Đặc điểm nổi bật của dòng sản phẩm:</h4>
                            <p>Sản phẩm thức ăn hạt Royal Canin Mini Adult được thiết kế chuyên biệt đáp ứng nhu cầu năng lượng cao của các giống chó nhỏ (cân nặng khi trưởng thành dưới 10kg). Chứa hàm lượng L-Carnitine tối ưu giúp kích thích chuyển hóa chất béo, duy trì khối lượng cơ nạc và vóc dáng thon gọn.</p>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
                            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-100 space-y-2">
                                <h5 class="font-bold text-sm text-slate-800 flex items-center gap-2">
                                    <i class="fa-solid fa-dna text-brand-600"></i>Thành phần nguyên liệu chính
                                </h5>
                                <p class="text-xs text-slate-600 leading-normal">Protein gia cầm sấy khô, bắp, bột bắp, mỡ động vật, gluten bắp, protein thực vật cô lập (L.I.P.), lúa mì, protein động vật thủy phân, gạo, củ cải đường, khoáng chất, dầu cá, dầu đậu nành, men nấm, fructo-oligo-sacarit.</p>
                            </div>
                            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-100 space-y-2">
                                <h5 class="font-bold text-sm text-slate-800 flex items-center gap-2">
                                    <i class="fa-solid fa-chart-pie text-orange-600"></i>Chỉ tiêu phân tích dinh dưỡng
                                </h5>
                                <div class="grid grid-cols-2 gap-2 text-xs">
                                    <div>Protein thô: <span class="font-bold text-slate-800">27.0%</span></div>
                                    <div>Chất béo thô: <span class="font-bold text-slate-800">16.0%</span></div>
                                    <div>Xơ thô: <span class="font-bold text-slate-800">1.3%</span></div>
                                    <div>Tro thô: <span class="font-bold text-slate-800">4.9%</span></div>
                                    <div>EPA/DHA: <span class="font-bold text-slate-800">0.25%</span></div>
                                    <div>Canxi & Photpho: <span class="font-bold text-slate-800">Cân đối 1.2:1</span></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- TAB 2: Hướng dẫn cho ăn theo cân nặng của Pet -->
                    <div x-show="productDetailTab === 'guide'" class="space-y-6 text-sm text-slate-700 animate-fadeIn">
                        <p class="text-xs sm:text-sm text-slate-600">Khẩu phần ăn hàng ngày được tính toán chuẩn theo cân nặng thực tế và mức độ vận động của thú cưng. Luôn chuẩn bị sẵn nước uống sạch cho bé.</p>
                        <div class="overflow-x-auto border border-slate-200 rounded-2xl shadow-sm">
                            <table class="w-full text-left text-xs sm:text-sm border-collapse">
                                <thead>
                                    <tr class="bg-slate-50 text-slate-800 border-b border-slate-200 font-bold">
                                        <th class="py-3 px-4">Cân Nặng Của Pet (kg)</th>
                                        <th class="py-3 px-4">Vận động ít (< 1h/ngày)</th>
                                        <th class="py-3 px-4">Vận động bình thường</th>
                                        <th class="py-3 px-4">Vận động nhiều (> 2h/ngày)</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-100">
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">2 kg (Chihuahua, Teacup)</td>
                                        <td class="py-3 px-4">40g (khoảng 3/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">47g (khoảng 4/8 cốc)</td>
                                        <td class="py-3 px-4">53g (khoảng 5/8 cốc)</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">4 kg (Poodle Tiny, Phốc Sóc)</td>
                                        <td class="py-3 px-4">68g (khoảng 6/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">79g (khoảng 1 cốc)</td>
                                        <td class="py-3 px-4">89g (khoảng 1 + 1/8 cốc)</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">6 kg (Corgi nhỏ, Pug nhỏ)</td>
                                        <td class="py-3 px-4">92g (khoảng 1 + 1/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">107g (khoảng 1 + 2/8 cốc)</td>
                                        <td class="py-3 px-4">121g (khoảng 1 + 4/8 cốc)</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">8 kg (Poodle Standard, Corgi)</td>
                                        <td class="py-3 px-4">114g (khoảng 1 + 3/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">132g (khoảng 1 + 5/8 cốc)</td>
                                        <td class="py-3 px-4">150g (khoảng 1 + 7/8 cốc)</td>
                                    </tr>
                                    <tr class="hover:bg-slate-50/60">
                                        <td class="py-3 px-4 font-bold text-slate-800">10 kg (Pháp, Beagle nhỏ)</td>
                                        <td class="py-3 px-4">135g (khoảng 1 + 5/8 cốc)</td>
                                        <td class="py-3 px-4 font-semibold text-orange-600">156g (khoảng 1 + 7/8 cốc)</td>
                                        <td class="py-3 px-4">177g (khoảng 2 + 1/8 cốc)</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- TAB 3: Đánh giá từ khách hàng -->
                    <div x-show="productDetailTab === 'reviews'" class="space-y-6 animate-fadeIn">
                        <!-- Khối Tổng Điểm & Bộ Lọc -->
                        <div class="bg-slate-50 rounded-2xl p-5 border border-slate-100 flex flex-col md:flex-row items-center justify-between gap-6">
                            <div class="flex items-center gap-5">
                                <div class="text-center">
                                    <div class="text-4xl sm:text-5xl font-black text-slate-900">4.8</div>
                                    <div class="flex text-amber-400 text-sm mt-1">
                                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i>
                                    </div>
                                    <span class="text-xs text-slate-400 mt-1 block">86 đánh giá</span>
                                </div>
                                <div class="space-y-1 text-xs text-slate-500 w-48 sm:w-60">
                                    <div class="flex items-center gap-2">
                                        <span>5★</span>
                                        <div class="flex-1 bg-slate-200 h-2 rounded-full overflow-hidden">
                                            <div class="bg-amber-400 h-full w-[88%]"></div>
                                        </div>
                                        <span>88%</span>
                                    </div>
                                    <div class="flex items-center gap-2">
                                        <span>4★</span>
                                        <div class="flex-1 bg-slate-200 h-2 rounded-full overflow-hidden">
                                            <div class="bg-amber-400 h-full w-[10%]"></div>
                                        </div>
                                        <span>10%</span>
                                    </div>
                                    <div class="flex items-center gap-2">
                                        <span>3★</span>
                                        <div class="flex-1 bg-slate-200 h-2 rounded-full overflow-hidden">
                                            <div class="bg-amber-400 h-full w-[2%]"></div>
                                        </div>
                                        <span>2%</span>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-col sm:flex-row items-center gap-3">
                                <button type="button" @click="openReviewPhotosLightbox()" class="px-4 py-2.5 rounded-xl text-xs bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 transition shadow-sm flex items-center gap-2">
                                    <i class="fa-solid fa-camera text-orange-500"></i>
                                    <span>Xem ảnh thực tế (<span x-text="productReviewsList.reduce((acc, r) => acc + (r.photos ? r.photos.length : (r.photo ? 1 : 0)), 0)"></span>)</span>
                                </button>
                                <button type="button" @click="openProductReviewModal()" class="bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs px-5 py-2.5 rounded-xl transition shadow flex items-center gap-2">
                                    <i class="fa-solid fa-pen-to-square"></i>
                                    <span>Viết Đánh Giá</span>
                                </button>
                            </div>
                        </div>

                        <!-- Danh sách đánh giá -->
                        <div class="space-y-4">
                            <template x-for="(rev, idx) in productReviewsList" :key="idx">
                                <div class="p-4 sm:p-5 rounded-2xl border border-slate-100 hover:border-slate-200 transition bg-white space-y-3">
                                    <div class="flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <img :src="rev.avatar" class="w-10 h-10 rounded-full object-cover border border-slate-200">
                                            <div>
                                                <h5 class="font-bold text-xs sm:text-sm text-slate-800 flex items-center gap-2">
                                                    <span x-text="rev.author"></span>
                                                    <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.2 rounded-full">Đã mua tại PetCare360</span>
                                                </h5>
                                                <div class="flex items-center gap-2 mt-0.5">
                                                    <div class="flex text-amber-400 text-xs">
                                                        <template x-for="s in rev.stars" :key="s">
                                                            <i class="fa-solid fa-star"></i>
                                                        </template>
                                                    </div>
                                                    <span class="text-[11px] text-slate-400" x-text="rev.date"></span>
                                                </div>
                                            </div>
                                        </div>
                                        <span class="text-xs text-slate-400 font-mono hidden sm:inline" x-text="rev.variant"></span>
                                    </div>
                                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed" x-text="rev.comment"></p>
                                    <template x-if="rev.photos && rev.photos.length > 0">
                                        <div class="flex gap-2 pt-1">
                                            <template x-for="(p, pidx) in rev.photos" :key="pidx">
                                                <img :src="p" @click="openSingleReviewLightbox(rev.photos, pidx)" class="w-16 h-16 sm:w-20 sm:h-20 rounded-xl object-cover border border-slate-200 shadow-sm hover:scale-105 transition cursor-pointer">
                                            </template>
                                        </div>
                                    </template>

                                    <!-- Thanh tương tác: Hữu ích / Thích & Trả lời -->
                                    <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
                                        <div class="flex items-center gap-4">
                                            <button type="button" @click="toggleReviewLike(rev)" class="flex items-center gap-1.5 transition font-semibold" :class="rev.isLiked ? 'text-orange-600' : 'text-slate-500 hover:text-slate-800'">
                                                <i :class="rev.isLiked ? 'fa-solid fa-thumbs-up' : 'fa-regular fa-thumbs-up'"></i>
                                                <span>Hữu ích (<span x-text="rev.likes || 0"></span>)</span>
                                            </button>
                                            <button type="button" @click="rev.showReplyInput = !rev.showReplyInput" class="flex items-center gap-1.5 text-slate-500 hover:text-slate-800 transition font-semibold">
                                                <i class="fa-regular fa-comment-dots"></i>
                                                <span>Trả lời</span>
                                            </button>
                                        </div>
                                    </div>

                                    <!-- Khung nhập trả lời phản hồi -->
                                    <template x-if="rev.showReplyInput">
                                        <div class="pt-2 flex gap-2">
                                            <input type="text" x-model="rev.newReplyText" @keydown.enter="addReviewReply(rev)" placeholder="Nhập phản hồi cho đánh giá này..." class="flex-1 px-3.5 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs focus:outline-none focus:bg-white focus:border-brand-500">
                                            <button type="button" @click="addReviewReply(rev)" class="px-4 py-2 bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs rounded-xl shadow-sm">Gửi</button>
                                        </div>
                                    </template>

                                    <!-- Danh sách các phản hồi (Threaded Nested Replies) -->
                                    <template x-if="rev.replies && rev.replies.length > 0">
                                        <div class="mt-2.5 pl-4 border-l-2 border-orange-200 space-y-2">
                                            <template x-for="(rep, repIdx) in rev.replies" :key="repIdx">
                                                <div class="p-3 bg-slate-50/80 rounded-xl text-xs space-y-1">
                                                    <div class="flex items-center gap-2">
                                                        <span class="font-bold text-slate-900" x-text="rep.author"></span>
                                                        <template x-if="rep.isAdmin">
                                                            <span class="px-2 py-0.2 bg-teal-100 text-teal-800 font-bold rounded text-[10px]">Đội Ngũ Bác Sĩ CSKH</span>
                                                        </template>
                                                        <span class="text-[10px] text-slate-400" x-text="rep.date"></span>
                                                    </div>
                                                    <p class="text-slate-700 leading-relaxed" x-text="rep.content"></p>
                                                </div>
                                            </template>
                                        </div>
                                    </template>
                                </div>
                            </template>
                        </div>
                    </div>
                </div>

                <!-- ======================================================== -->
                <!-- SECTION: SẢN PHẨM TƯƠNG TỰ BẠN CÓ THỂ THÍCH (RESTORED 4-CARD HORIZONTAL CAROUSEL) -->
                <!-- ======================================================== -->
                <div class="space-y-4 pt-4 border-t border-slate-200">
                    <div class="flex items-center justify-between">
                        <div>
                            <h3 class="text-lg sm:text-xl font-bold text-slate-900">Sản phẩm tương tự bạn có thể thích</h3>
                            <p class="text-xs text-slate-500">Gợi ý từ các bác sĩ dinh dưỡng PetCare360</p>
                        </div>
                        <!-- Điều hướng: Xem tất cả 12 sản phẩm + Nút mũi tên điều hướng Trái/Phải -->
                        <div class="flex items-center gap-2">
                            <span class="text-xs text-[#F97316] font-bold hover:underline cursor-pointer mr-1 hidden sm:inline" @click="backToShopCatalog()">Xem tất cả 12 sản phẩm</span>
                            <div class="flex items-center gap-1.5">
                                <button @click="scrollSimilarLeft()" class="w-8 h-8 rounded-full border border-slate-200 bg-white hover:bg-orange-50 text-slate-600 hover:text-orange-600 shadow-sm flex items-center justify-center transition active:scale-90" title="Trượt sang trái">
                                    <i class="fa-solid fa-chevron-left text-xs"></i>
                                </button>
                                <button @click="scrollSimilarRight()" class="w-8 h-8 rounded-full border border-slate-200 bg-white hover:bg-orange-50 text-slate-600 hover:text-orange-600 shadow-sm flex items-center justify-center transition active:scale-90" title="Trượt xem tiếp sản phẩm">
                                    <i class="fa-solid fa-chevron-right text-xs"></i>
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Product Carousel: Set thuộc tính hiển thị chính xác 4 thẻ sản phẩm (Product Card) nằm ngang trên cùng một hàng (desktop), kích hoạt trượt ngang (Horizontal scroll/Swipe) -->
                    <div id="product-detail-similar-carousel" class="flex gap-4 overflow-x-auto scroll-smooth snap-x pb-3 pt-1 no-scrollbar hide-scrollbar">
                        <template x-for="sim in similarProductsList" :key="'sim-' + sim.id">
                            <div @click="openProductDetailPage(sim)" class="snap-start flex-shrink-0 w-[260px] sm:w-[calc(50%-8px)] md:w-[calc(33.333%-11px)] lg:w-[calc(25%-12px)] bg-white rounded-2xl p-3 border border-slate-200 shadow-sm hover:shadow-lg transition-all duration-200 flex flex-col justify-between group cursor-pointer relative overflow-hidden">
                                
                                <!-- Ảnh thumbnail sản phẩm (bo góc, tỷ lệ 1:1) + Badge giảm giá & Giao nhanh 2h -->
                                <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-50 flex items-center justify-center p-2">
                                    <img :src="sim.image || sim.img" :alt="sim.name" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300">
                                    <span class="absolute top-2 left-2 bg-rose-600 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-md shadow-sm" x-text="sim.discountPercent || '-15%'"></span>
                                    <template x-if="sim.expressShip">
                                        <span class="absolute top-2 right-2 bg-amber-400 text-slate-900 font-black text-[9px] px-1.5 py-0.5 rounded-md shadow-sm flex items-center gap-0.5">
                                            <i class="fa-solid fa-bolt text-[8px]"></i> 2H
                                        </span>
                                    </template>
                                </div>

                                <!-- Cấu trúc Thẻ sản phẩm chuẩn: Tên sản phẩm tối đa 2 dòng (...), Số sao & Lượt mua, Giá khuyến mãi + gốc gạch ngang, Nút giỏ hàng -->
                                <div class="pt-3 pb-1 space-y-1.5 flex-1 flex flex-col justify-between">
                                    <div>
                                        <p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider truncate" x-text="sim.brand || sim.category"></p>
                                        <h4 class="text-xs sm:text-sm font-bold text-[#1E293B] line-clamp-2 leading-snug group-hover:text-[#F97316] transition" x-text="sim.name" :title="sim.name"></h4>
                                    </div>

                                    <div>
                                        <!-- Số sao đánh giá và lượt mua -->
                                        <div class="flex items-center gap-1.5 text-xs text-slate-500 pt-1">
                                            <div class="flex items-center text-amber-400 text-xs">
                                                <i class="fa-solid fa-star"></i>
                                                <span class="font-bold text-slate-800 ml-1" x-text="sim.rating || 5.0"></span>
                                            </div>
                                            <span class="text-slate-300">•</span>
                                            <span class="text-[11px] text-slate-400" x-text="(sim.sold || 96) + ' đã bán'"></span>
                                        </div>

                                        <!-- Giá bán khuyến mãi (nổi bật, màu cam/đỏ) + Giá gốc gạch ngang + Nút Icon Giỏ hàng thao tác nhanh -->
                                        <div class="pt-2 flex items-center justify-between border-t border-slate-100 mt-2">
                                            <div>
                                                <div class="text-sm sm:text-base font-extrabold text-[#F97316]" x-text="formatCurrency(sim.price)"></div>
                                                <div class="text-[10px] text-slate-400 line-through font-medium" x-text="formatCurrency(sim.originalPrice || Math.round(sim.price * 1.25))"></div>
                                            </div>
                                            <button @click.stop="addToCart({ id: sim.id, name: sim.name, price: sim.price, image: sim.image || sim.img, weight: '3kg', flavor: 'Vị chuẩn' })" class="w-9 h-9 rounded-full bg-orange-50 text-[#F97316] hover:bg-[#F97316] hover:text-white transition flex items-center justify-center shadow-sm transform active:scale-90" title="Thêm vào giỏ hàng">
                                                <i class="fa-solid fa-cart-plus text-xs"></i>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
                </div>
            </div>

            <!-- TAB 3: DỊCH VỤ (CHĂM SÓC & Y TẾ 5 SAO THEO YÊU CẦU) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'booking'" class="space-y-8" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- 1. Header Dịch vụ & Nút Text Link Nhỏ Gọn "Xem bảng giá chi tiết" (Progressive Disclosure) -->
                <div class="bg-gradient-to-r from-teal-800 via-[#F97316]/90 to-slate-900 rounded-3xl p-6 sm:p-8 text-white shadow-xl relative overflow-hidden">
                    <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div class="space-y-2 max-w-2xl">
                            <div class="flex items-center gap-2">
                                <span class="bg-amber-400 text-slate-900 text-xs font-black px-3 py-1 rounded-full uppercase tracking-wider">Tiêu chuẩn quốc tế 5 sao</span>
                                <span class="bg-white/20 text-white text-xs font-semibold px-2.5 py-0.5 rounded-full">Chăm sóc chu đáo & tận tâm</span>
                            </div>
                            <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight">Dịch Vụ Chăm Sóc Thú Cưng Chuyên Nghiệp</h2>
                            <p class="text-orange-100 text-xs sm:text-sm leading-relaxed">Quy trình đặt lịch 3 bước nhanh chóng, tự động tính giá chính xác theo size và cân nặng bé cưng.</p>
                        </div>
                        
                        <!-- Nút Text Link nhỏ gọn: "Xem bảng giá chi tiết" (Mở Modal Pop-up Bảng Giá) -->
                        <div class="self-start md:self-center flex-shrink-0">
                            <button type="button" @click="showPriceMatrixModal = true" class="px-4 py-2.5 rounded-2xl bg-white/15 hover:bg-white/25 text-white border border-white/30 text-xs sm:text-sm font-bold backdrop-blur-md transition flex items-center gap-2 shadow-sm hover:scale-105 active:scale-95 cursor-pointer">
                                <i class="fa-solid fa-table-list text-amber-300"></i>
                                <span>Xem bảng giá chi tiết</span>
                                <i class="fa-solid fa-arrow-up-right-from-square text-[10px] text-amber-200"></i>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Chuyển đổi giữa 2 nhóm dịch vụ: Grooming & Spa vs Pet Hotel 5 Sao -->
                <div class="bg-white rounded-2xl p-2 border border-slate-200 shadow-sm grid grid-cols-2 gap-2">
                    <button type="button" @click="servicePricingTab = 'grooming'; selectGroomingPackage('spa')" :class="(servicePricingTab === 'grooming' || servicePricingTab === 'spa') ? 'bg-[#F97316] text-white font-bold shadow-md shadow-orange-500/20' : 'text-slate-600 hover:bg-slate-100'" class="w-full py-3 px-4 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-2 cursor-pointer">
                        <i class="fa-solid fa-scissors"></i>
                        <span>Grooming & Spa</span>
                    </button>
                    <button type="button" @click="servicePricingTab = 'hotel'; selectHotelPackage('overnight')" :class="servicePricingTab === 'hotel' ? 'bg-[#F97316] text-white font-bold shadow-md shadow-orange-500/20' : 'text-slate-600 hover:bg-slate-100'" class="w-full py-3 px-4 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-2 cursor-pointer">
                        <i class="fa-solid fa-hotel"></i>
                        <span>Pet Hotel 5 Sao</span>
                    </button>
                </div>

                <!-- 2. THANH TIẾN TRÌNH STEPPER (3 BƯỚC TIẾN TRÌNH NGANG) -->
                <div class="bg-white rounded-3xl p-5 sm:p-6 border border-slate-200 shadow-sm">
                    <div class="max-w-3xl mx-auto flex items-center justify-between relative">
                        <!-- Line nền xám -->
                        <div class="absolute left-10 right-10 top-1/2 -translate-y-1/2 h-1 bg-slate-200 -z-0"></div>
                        <!-- Line active cam chuyển động mượt mà -->
                        <div class="absolute left-10 top-1/2 -translate-y-1/2 h-1 bg-gradient-to-r from-orange-500 to-amber-500 transition-all duration-300 -z-0"
                             :style="'width: ' + ((bookingWizardStep - 1) * 50) + '%'"></div>

                        <!-- Bước 1 Stepper -->
                        <button type="button" @click="bookingWizardStep = 1" class="relative z-10 flex flex-col items-center gap-1.5 group cursor-pointer">
                            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-2xl flex items-center justify-center font-black text-sm transition-all duration-200"
                                 :class="bookingWizardStep === 1 ? 'bg-[#F97316] text-white shadow-lg shadow-orange-500/30 ring-4 ring-orange-100 scale-105' : (bookingWizardStep > 1 ? 'bg-emerald-500 text-white' : 'bg-slate-200 text-slate-500')">
                                <span x-show="bookingWizardStep <= 1">1</span>
                                <i x-show="bookingWizardStep > 1" class="fa-solid fa-check"></i>
                            </div>
                            <span class="text-[11px] sm:text-xs font-bold"
                                  :class="bookingWizardStep === 1 ? 'text-[#F97316]' : (bookingWizardStep > 1 ? 'text-emerald-700' : 'text-slate-400')">
                                1. Pet & Dịch Vụ
                            </span>
                        </button>

                        <!-- Bước 2 Stepper -->
                        <button type="button" @click="bookingWizardStep = 2" class="relative z-10 flex flex-col items-center gap-1.5 group cursor-pointer">
                            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-2xl flex items-center justify-center font-black text-sm transition-all duration-200"
                                 :class="bookingWizardStep === 2 ? 'bg-[#F97316] text-white shadow-lg shadow-orange-500/30 ring-4 ring-orange-100 scale-105' : (bookingWizardStep > 2 ? 'bg-emerald-500 text-white' : 'bg-slate-200 text-slate-500')">
                                <span x-show="bookingWizardStep <= 2">2</span>
                                <i x-show="bookingWizardStep > 2" class="fa-solid fa-check"></i>
                            </div>
                            <span class="text-[11px] sm:text-xs font-bold"
                                  :class="bookingWizardStep === 2 ? 'text-[#F97316]' : (bookingWizardStep > 2 ? 'text-emerald-700' : 'text-slate-400')">
                                2. Thời Gian & Tiện Ích
                            </span>
                        </button>

                        <!-- Bước 3 Stepper -->
                        <button type="button" @click="bookingWizardStep = 3" class="relative z-10 flex flex-col items-center gap-1.5 group cursor-pointer">
                            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-2xl flex items-center justify-center font-black text-sm transition-all duration-200"
                                 :class="bookingWizardStep === 3 ? 'bg-[#F97316] text-white shadow-lg shadow-orange-500/30 ring-4 ring-orange-100 scale-105' : 'bg-slate-200 text-slate-500'">
                                <span>3</span>
                            </div>
                            <span class="text-[11px] sm:text-xs font-bold"
                                  :class="bookingWizardStep === 3 ? 'text-[#F97316]' : 'text-slate-400'">
                                3. Ghi Chú & Xác Nhận
                            </span>
                        </button>
                    </div>
                </div>

                <!-- KHUNG FORM WIZARD CHÍNH -->
                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                    
                    <!-- ==================================================== -->
                    <!-- BƯỚC 1: CHỌN THÚ CƯNG & DỊCH VỤ CHÍNH (AUTO-PRICING) -->
                    <!-- ==================================================== -->
                    <div x-show="bookingWizardStep === 1" class="space-y-6 animate-fadeIn" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                        
                        <div class="pb-3 border-b border-slate-100">
                            <h3 class="text-base sm:text-lg font-black text-slate-900 flex items-center gap-2">
                                <span class="w-7 h-7 rounded-full bg-[#F97316] text-white flex items-center justify-center text-xs font-black">1</span>
                                <span>Chọn Thú Cưng & Cấu Trúc Gói Dịch Vụ</span>
                            </h3>
                            <p class="text-xs text-slate-500 mt-1">Hệ thống tự động map cân nặng của bé để tính chính xác mức giá sàn và chênh lệch nâng cấp</p>
                        </div>

                        <!-- 1. TỰ ĐỘNG BÁO GIÁ: DROPDOWN CHỌN THÚ CƯNG TỪ HỒ SƠ LÊN ĐẦU -->
                        <div class="bg-gradient-to-br from-orange-50/90 to-amber-50/70 p-5 rounded-3xl border border-orange-200/90 space-y-4">
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                                <div>
                                    <label class="block text-xs font-black text-slate-900 uppercase tracking-wider flex items-center gap-1.5">
                                        <i class="fa-solid fa-paw text-[#F97316]"></i>
                                        <span>Chọn Thú Cưng Từ Hồ Sơ:</span>
                                    </label>
                                    <p class="text-[11px] text-slate-500 mt-0.5">Giá dịch vụ sẽ tự động điều chỉnh theo đúng cân nặng bé cưng</p>
                                </div>
                                
                                <div class="w-full sm:w-72">
                                    <select x-model="serviceBookingForm.petId" 
                                            @change="syncPetBookingDetails(serviceBookingForm.petId)"
                                            class="w-full bg-white border-2 border-orange-300 rounded-2xl px-4 py-2.5 text-xs sm:text-sm font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500 shadow-sm cursor-pointer">
                                        <template x-for="p in pets" :key="'wizard-pet-' + p.id">
                                            <option :value="p.id" x-text="p.name + ' (' + p.breed + ' - ' + p.weight + 'kg)'"></option>
                                        </template>
                                    </select>
                                </div>
                            </div>

                            <!-- Thẻ Tóm Tắt Bé Đang Được Chọn & Phân Hạng Cân Nặng Tự Động -->
                            <div class="bg-white/95 backdrop-blur-sm rounded-2xl p-4 border border-orange-200/80 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-2xs">
                                <div class="flex items-center gap-3">
                                    <img :src="petBookingDetail.vaccinePhoto || petBookingDetail.avatar || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=150&q=80'" 
                                         @error="$event.target.src='https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=150&q=80'"
                                         class="w-14 h-14 rounded-2xl object-cover border-2 border-orange-200 shadow-sm flex-shrink-0">
                                    <div>
                                        <div class="flex items-center gap-2 flex-wrap">
                                            <h5 class="font-black text-slate-900 text-sm sm:text-base" x-text="petBookingDetail.name"></h5>
                                            <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full flex items-center gap-1">
                                                <i class="fa-solid fa-circle-check text-[9px]"></i>Đã tiêm vắc-xin
                                            </span>
                                        </div>
                                        <p class="text-xs text-slate-500 mt-0.5">
                                            Giống: <strong class="text-slate-700" x-text="petBookingDetail.breed"></strong> • 
                                            Cân nặng: <strong class="text-[#F97316] font-black" x-text="petBookingDetail.weight + ' kg'"></strong>
                                        </p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-2 self-start sm:self-auto">
                                    <div class="text-left sm:text-right">
                                        <div class="text-[10px] text-slate-400 font-bold uppercase tracking-wider">Hạng Size Áp Dụng</div>
                                        <div class="text-xs font-black text-orange-700 bg-orange-100/90 px-3 py-1 rounded-xl border border-orange-200" x-text="servicePricingTab === 'hotel' ? currentPetHotelTier : currentPetGroomingTier"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 2. CẤU TRÚC GÓI DỊCH VỤ (TAB GROOMING & SPA): GÓI CƠ BẢN VÀ GÓI NÂNG CẤP -->
                        <div x-show="servicePricingTab === 'grooming' || servicePricingTab === 'spa'" class="space-y-4">
                            
                            <!-- GÓI CƠ BẢN: SPA TẮM SẤY THẢO MỘC (MẶC ĐỊNH LUÔN ĐƯỢC CHỌN - HIỂN THỊ GIÁ SÀN) -->
                            <div class="p-5 rounded-3xl border-2 border-[#F97316] bg-orange-50/50 shadow-md ring-2 ring-orange-200/70 relative transition duration-200">
                                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                    <div class="flex items-start gap-4">
                                        <div class="w-12 h-12 rounded-2xl bg-[#F97316] text-white flex items-center justify-center text-xl shadow-md shadow-orange-500/30 flex-shrink-0">
                                            <i class="fa-solid fa-shower"></i>
                                        </div>
                                        <div class="space-y-1">
                                            <div class="flex items-center gap-2 flex-wrap">
                                                <span class="text-[10px] font-black uppercase tracking-wider bg-[#F97316] text-white px-2.5 py-0.5 rounded-full shadow-2xs">Gói Cơ Bản Bắt Buộc</span>
                                                <span class="text-[10px] font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full flex items-center gap-1">
                                                    <i class="fa-solid fa-circle-check text-[9px]"></i> Mặc định đã chọn
                                                </span>
                                            </div>
                                            <h4 class="font-black text-base sm:text-lg text-slate-900">Gói Cơ Bản: Spa Tắm Sấy Thảo Mộc</h4>
                                            <p class="text-xs text-slate-600 leading-relaxed max-w-xl">
                                                Quy trình nền tảng 7 bước: Tắm sữa tắm thảo mộc dưỡng ẩm, vệ sinh tai 2 lớp chuyên sâu, cắt & mài móng, vắt tuyến hôi, sấy phồng lông và xịt tinh dầu lưu hương.
                                            </p>
                                        </div>
                                    </div>
                                    
                                    <!-- Cột giá sàn & checkbox cố định -->
                                    <div class="flex sm:flex-col items-center sm:items-end justify-between sm:justify-center pt-3 sm:pt-0 border-t sm:border-t-0 border-orange-200/60 flex-shrink-0">
                                        <span class="text-[11px] text-slate-500 font-semibold uppercase tracking-wider">Giá Sàn Áp Dụng:</span>
                                        <span class="text-xl sm:text-2xl font-black text-[#F97316]" x-text="formatCurrency(getGroomingSpaPrice())"></span>
                                        <div class="mt-1 flex items-center gap-1.5 text-xs text-emerald-700 font-extrabold bg-emerald-50 px-2.5 py-1 rounded-xl border border-emerald-200">
                                            <i class="fa-solid fa-square-check text-emerald-600 text-sm"></i>
                                            <span>Đã Chọn</span>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- BÊN DƯỚI: 2 CARD TÙY CHỌN NÂNG CẤP (RADIO BUTTONS) -->
                            <div class="space-y-2 pt-2">
                                <div class="flex items-center justify-between">
                                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                        Chọn Gói Nâng Cấp (Tùy Chọn - Cộng Thêm Chênh Lệch):
                                    </label>
                                    <button type="button" @click="setGroomingCutType('none')" x-show="groomingCutType !== 'none'" class="text-xs text-[#F97316] hover:underline font-bold">
                                        Bỏ chọn nâng cấp (Chỉ dùng Spa cơ bản)
                                    </button>
                                </div>

                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    
                                    <!-- Card Nâng Cấp 1: Cắt Tỉa Tạo Kiểu (Grooming) -->
                                    <div @click="setGroomingCutType(groomingCutType === 'grooming' ? 'none' : 'grooming')"
                                         :class="groomingCutType === 'grooming' ? 'border-2 border-[#F97316] bg-orange-50/70 shadow-md ring-2 ring-orange-200' : 'border border-slate-200 bg-white hover:border-orange-300 hover:shadow-sm'"
                                         class="p-5 rounded-3xl transition duration-200 cursor-pointer flex flex-col justify-between space-y-4 group">
                                        <div class="space-y-3">
                                            <div class="flex items-center justify-between">
                                                <div class="flex items-center gap-3">
                                                    <div class="w-10 h-10 rounded-2xl bg-amber-100 text-amber-700 flex items-center justify-center text-lg group-hover:scale-105 transition">
                                                        <i class="fa-solid fa-scissors"></i>
                                                    </div>
                                                    <div>
                                                        <span class="text-[10px] font-extrabold bg-amber-500 text-white px-2 py-0.5 rounded-full uppercase">Hot Style</span>
                                                        <h5 class="font-black text-sm sm:text-base text-slate-900 group-hover:text-[#F97316] transition">Nâng cấp: + Cắt Tỉa Tạo Kiểu (Grooming)</h5>
                                                    </div>
                                                </div>
                                                <!-- Radio Indicator -->
                                                <div class="w-6 h-6 rounded-full flex items-center justify-center border transition"
                                                     :class="groomingCutType === 'grooming' ? 'border-[#F97316] bg-white ring-2 ring-orange-400' : 'border-slate-300 bg-white'">
                                                    <div class="w-3 h-3 rounded-full bg-[#F97316]" x-show="groomingCutType === 'grooming'"></div>
                                                </div>
                                            </div>
                                            <p class="text-xs text-slate-500 leading-relaxed">
                                                Cắt tỉa tạo dáng theo yêu cầu (Teddy Bear, Corgi mông tròn, Boo style, phom sư tử) bởi Master Groomer tay nghề cao.
                                            </p>
                                        </div>
                                        <div class="pt-3 border-t border-slate-100 flex items-baseline justify-between">
                                            <span class="text-xs text-slate-400 font-semibold">Phí chênh lệch cộng thêm:</span>
                                            <div class="text-right">
                                                <span class="text-base font-black text-[#F97316]" x-text="'+' + formatCurrency(Math.max(0, getGroomingCutPrice() - getGroomingSpaPrice()))"></span>
                                                <div class="text-[10px] text-slate-400" x-text="'(Tổng gói: ' + formatCurrency(getGroomingCutPrice()) + ')'"></div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Card Nâng Cấp 2: Cạo Lông Vệ Sinh (Shave) -->
                                    <div @click="setGroomingCutType(groomingCutType === 'shave' ? 'none' : 'shave')"
                                         :class="groomingCutType === 'shave' ? 'border-2 border-[#F97316] bg-orange-50/70 shadow-md ring-2 ring-orange-200' : 'border border-slate-200 bg-white hover:border-orange-300 hover:shadow-sm'"
                                         class="p-5 rounded-3xl transition duration-200 cursor-pointer flex flex-col justify-between space-y-4 group">
                                        <div class="space-y-3">
                                            <div class="flex items-center justify-between">
                                                <div class="flex items-center gap-3">
                                                    <div class="w-10 h-10 rounded-2xl bg-emerald-100 text-emerald-700 flex items-center justify-center text-lg group-hover:scale-105 transition">
                                                        <i class="fa-solid fa-wand-magic-sparkles"></i>
                                                    </div>
                                                    <div>
                                                        <span class="text-[10px] font-extrabold bg-emerald-500 text-white px-2 py-0.5 rounded-full uppercase">Mát Mẻ & Sạch Sẽ</span>
                                                        <h5 class="font-black text-sm sm:text-base text-slate-900 group-hover:text-[#F97316] transition">Nâng cấp: + Cạo Lông Vệ Sinh (Shave)</h5>
                                                    </div>
                                                </div>
                                                <!-- Radio Indicator -->
                                                <div class="w-6 h-6 rounded-full flex items-center justify-center border transition"
                                                     :class="groomingCutType === 'shave' ? 'border-[#F97316] bg-white ring-2 ring-orange-400' : 'border-slate-300 bg-white'">
                                                    <div class="w-3 h-3 rounded-full bg-[#F97316]" x-show="groomingCutType === 'shave'"></div>
                                                </div>
                                            </div>
                                            <p class="text-xs text-slate-500 leading-relaxed">
                                                Cạo phom lông sát da an toàn (độ dài 3mm - 6mm) giúp hạ nhiệt mùa nóng, điều trị nấm ve rận, đồng thời vệ sinh gọn gàng đệm chân và hậu môn.
                                            </p>
                                        </div>
                                        <div class="pt-3 border-t border-slate-100 flex items-baseline justify-between">
                                            <span class="text-xs text-slate-400 font-semibold">Phí chênh lệch cộng thêm:</span>
                                            <div class="text-right">
                                                <span class="text-base font-black text-[#F97316]" x-text="'+' + formatCurrency(Math.max(0, getGroomingShavePrice() - getGroomingSpaPrice()))"></span>
                                                <div class="text-[10px] text-slate-400" x-text="'(Tổng gói: ' + formatCurrency(getGroomingShavePrice()) + ')'"></div>
                                            </div>
                                        </div>
                                    </div>

                                </div>
                            </div>
                        </div>

                        <!-- CẤU TRÚC GÓI HOTEL 5 SAO (KHI CHỌN TAB HOTEL) -->
                        <div x-show="servicePricingTab === 'hotel'" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <!-- Card Hotel 1: Lưu Trú Qua Đêm 5 Sao -->
                            <div @click="selectHotelPackage('overnight')"
                                 :class="hotelServiceType === 'overnight' ? 'border-2 border-[#F97316] bg-orange-50/60 shadow-md ring-2 ring-orange-200' : 'border border-slate-200 bg-white hover:border-orange-300 hover:shadow-sm'"
                                 class="p-5 rounded-3xl transition duration-200 cursor-pointer flex flex-col justify-between space-y-4 group">
                                <div class="space-y-3">
                                    <div class="flex items-center justify-between">
                                        <div class="w-12 h-12 rounded-2xl bg-amber-100 text-amber-600 flex items-center justify-center text-xl group-hover:scale-105 transition">
                                            <i class="fa-solid fa-moon"></i>
                                        </div>
                                        <span class="text-[10px] font-extrabold bg-[#F97316] text-white px-2 py-0.5 rounded-full uppercase">Lưu Trú 24/7</span>
                                    </div>
                                    <div>
                                        <h4 class="font-black text-base text-slate-900 group-hover:text-[#F97316] transition">Lưu Trú Qua Đêm 5 Sao (24 Giờ)</h4>
                                        <p class="text-xs text-slate-500 mt-1 leading-relaxed">Phòng điều hòa riêng biệt 24/24, đệm êm, 3 bữa hạt và pate cao cấp, dắt đi dạo sân cỏ 2 lần/ngày kèm Camera PetCam xem trực tiếp.</p>
                                    </div>
                                </div>
                                <div class="pt-3 border-t border-slate-100 flex items-baseline justify-between">
                                    <span class="text-[11px] text-slate-400 font-semibold">Giá 1 đêm:</span>
                                    <span class="text-lg font-black text-[#F97316]" x-text="formatCurrency(getPetHotelPriceByWeight(petBookingDetail.weight || 5)) + '/đêm'"></span>
                                </div>
                            </div>

                            <!-- Card Hotel 2: Gửi Bán Trú Daycare Trong Ngày -->
                            <div @click="selectHotelPackage('daycare')"
                                 :class="hotelServiceType === 'daycare' ? 'border-2 border-[#F97316] bg-orange-50/60 shadow-md ring-2 ring-orange-200' : 'border border-slate-200 bg-white hover:border-orange-300 hover:shadow-sm'"
                                 class="p-5 rounded-3xl transition duration-200 cursor-pointer flex flex-col justify-between space-y-4 group">
                                <div class="space-y-3">
                                    <div class="flex items-center justify-between">
                                        <div class="w-12 h-12 rounded-2xl bg-sky-100 text-sky-600 flex items-center justify-center text-xl group-hover:scale-105 transition">
                                            <i class="fa-solid fa-sun"></i>
                                        </div>
                                        <span class="text-[10px] font-extrabold bg-sky-500 text-white px-2 py-0.5 rounded-full uppercase">Trong Ngày</span>
                                    </div>
                                    <div>
                                        <h4 class="font-black text-base text-slate-900 group-hover:text-[#F97316] transition">Gửi Bán Trú Daycare (08:00 - 18:00)</h4>
                                        <p class="text-xs text-slate-500 mt-1 leading-relaxed">Giải pháp hoàn hảo cho chủ bận đi làm ban ngày. Bé được vui chơi với bạn cùng size, ăn trưa dinh dưỡng và ngủ trưa máy lạnh an toàn.</p>
                                    </div>
                                </div>
                                <div class="pt-3 border-t border-slate-100 flex items-baseline justify-between">
                                    <span class="text-[11px] text-slate-400 font-semibold">Giá trọn ngày:</span>
                                    <span class="text-lg font-black text-[#F97316]" x-text="formatCurrency(Math.round(getPetHotelPriceByWeight(petBookingDetail.weight || 5) * 0.6)) + '/ngày'"></span>
                                </div>
                            </div>
                        </div>

                        <!-- NÚT TIẾP TỤC SANG BƯỚC 2 -->
                        <div class="pt-4 border-t border-slate-100 flex justify-end">
                            <button type="button" @click="bookingWizardStep = 2" class="px-6 py-3.5 bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-bold text-xs sm:text-sm rounded-2xl shadow-md shadow-orange-500/25 transition flex items-center gap-2 cursor-pointer active:scale-95">
                                <span>Tiếp tục: Chọn Thời Gian & Logistics</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>

                    <!-- ==================================================== -->
                    <!-- BƯỚC 2: CHI TIẾT THỜI GIAN, TIỆN ÍCH & LOGISTICS PETSHIP -->
                    <!-- ==================================================== -->
                    <div x-show="bookingWizardStep === 2" class="space-y-6 animate-fadeIn" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                        
                        <div class="pb-3 border-b border-slate-100">
                            <h3 class="text-base sm:text-lg font-black text-slate-900 flex items-center gap-2">
                                <span class="w-7 h-7 rounded-full bg-[#F97316] text-white flex items-center justify-center text-xs font-black">2</span>
                                <span>Chi Tiết Thời Gian, Tiện Ích & Logistics PetShip</span>
                            </h3>
                            <p class="text-xs text-slate-500 mt-1">Lựa chọn khung giờ thuận tiện và các dịch vụ bổ sung để bé cưng được chăm sóc chu đáo nhất</p>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <!-- CHỌN THỜI GIAN DÀNH CHO GROOMING / SPA -->
                            <div x-show="servicePricingTab !== 'hotel'" class="space-y-3">
                                <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                    <i class="fa-solid fa-calendar-day text-[#F97316] mr-1"></i> Ngày Hẹn Làm Dịch Vụ:
                                </label>
                                <input type="date" x-model="serviceBookingForm.date" class="w-full bg-slate-50 border border-slate-300 rounded-2xl px-4 py-3 text-xs sm:text-sm font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                
                                <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider pt-2">
                                    <i class="fa-solid fa-clock text-[#F97316] mr-1"></i> Khung Giờ Bắt Đầu:
                                </label>
                                <div class="grid grid-cols-3 gap-2">
                                    <template x-for="slot in ['08:30', '10:00', '13:30', '15:00', '16:30', '18:00']" :key="slot">
                                        <button type="button" @click="serviceBookingForm.timeSlot = slot"
                                                :class="serviceBookingForm.timeSlot === slot ? 'bg-[#F97316] text-white font-bold shadow-xs' : 'bg-slate-50 text-slate-700 border border-slate-200 hover:bg-slate-100'"
                                                class="py-2.5 px-3 rounded-xl text-xs transition font-semibold" x-text="slot"></button>
                                    </template>
                                </div>

                                <!-- TEXT TỰ ĐỘNG TÍNH THỜI GIAN DỰ KIẾN HOÀN THÀNH (YÊU CẦU 2) -->
                                <div class="p-3 bg-amber-50 rounded-2xl border border-amber-200 text-xs text-amber-900 font-bold flex items-center gap-2">
                                    <i class="fa-solid fa-stopwatch text-[#F97316] text-sm"></i>
                                    <span>Thời gian dự kiến hoàn thành: <strong>90 - 120 phút</strong></span>
                                </div>
                            </div>

                            <!-- CHỌN THỜI GIAN DÀNH CHO HOTEL 5 SAO: ĐẦY ĐỦ NGÀY VÀ GIỜ CHECK-IN CÙNG NGÀY VÀ GIỜ CHECK-OUT -->
                            <div x-show="servicePricingTab === 'hotel'" class="space-y-4 md:col-span-2">
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                    <div class="space-y-2 bg-slate-50 p-4 rounded-2xl border border-slate-200">
                                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                            <i class="fa-solid fa-calendar-check text-[#F97316] mr-1"></i> Ngày & Giờ Check-in (Nhận phòng):
                                        </label>
                                        <div class="grid grid-cols-2 gap-2">
                                            <div>
                                                <span class="text-[10px] text-slate-400 font-bold block mb-1">Ngày nhận:</span>
                                                <input type="date" x-model="hotelCheckInDate" @change="recalculateHotelFee()" class="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                            </div>
                                            <div>
                                                <span class="text-[10px] text-slate-400 font-bold block mb-1">Giờ nhận:</span>
                                                <input type="time" x-model="serviceBookingForm.hotelCheckInTime" class="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="space-y-2 bg-slate-50 p-4 rounded-2xl border border-slate-200">
                                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                            <i class="fa-solid fa-calendar-xmark text-[#F97316] mr-1"></i> Ngày & Giờ Check-out (Trả phòng):
                                        </label>
                                        <div class="grid grid-cols-2 gap-2">
                                            <div>
                                                <span class="text-[10px] text-slate-400 font-bold block mb-1">Ngày trả:</span>
                                                <input type="date" x-model="hotelCheckOutDate" @change="recalculateHotelFee()" class="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                            </div>
                                            <div>
                                                <span class="text-[10px] text-slate-400 font-bold block mb-1">Giờ trả:</span>
                                                <input type="time" x-model="serviceBookingForm.hotelCheckOutTime" class="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-orange-500">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <p class="text-[11px] text-orange-700 font-semibold bg-orange-50 p-2.5 rounded-xl border border-orange-200 flex items-center justify-between flex-wrap gap-1">
                                    <span class="flex items-center gap-1.5">
                                        <i class="fa-solid fa-calendar-days text-[#F97316]"></i>
                                        <span>Thời gian lưu trú: <strong x-text="hotelNights"></strong> đêm (<strong x-text="formatCurrency(hotelFee)"></strong>)</span>
                                    </span>
                                    <span class="text-[10px] text-slate-500 italic">* Tính phụ phí nếu check-out trễ sau 12:00 trưa</span>
                                </p>
                            </div>

                            <!-- CHI NHÁNH CỐ ĐỊNH -->
                            <div class="space-y-3" x-show="servicePricingTab !== 'hotel'">
                                <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                    Địa Điểm Thực Hiện:
                                </label>
                                <div class="p-3.5 bg-slate-50 rounded-2xl border border-slate-200 space-y-1">
                                    <div class="flex items-center gap-1.5 text-xs font-bold text-slate-800">
                                        <i class="fa-solid fa-location-dot text-[#F97316]"></i>
                                        <span>Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Quận 1, TP.HCM</span>
                                    </div>
                                    <p class="text-[11px] text-slate-500 leading-relaxed">Khu phức hợp PetCare360 tiêu chuẩn 5 sao với bãi đỗ xe ô tô và sân cỏ ngoài trời biệt lập.</p>
                                </div>
                            </div>
                        </div>

                        <!-- DỊCH VỤ CỘNG THÊM (ADD-ONS) -->
                        <div class="space-y-3 pt-2">
                            <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                Dịch Vụ Cộng Thêm (Add-ons Tùy Chọn):
                            </label>
                            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                                <template x-for="addon in availableAddons" :key="addon.id">
                                    <div @click="toggleServiceAddon(addon.id)"
                                         :class="serviceBookingForm.addons.includes(addon.id) ? 'bg-orange-50 border-[#F97316] text-orange-900 shadow-2xs' : 'bg-slate-50 border-slate-200 text-slate-700 hover:bg-slate-100'"
                                         class="p-3.5 rounded-2xl border transition cursor-pointer flex items-center justify-between gap-3">
                                        <div class="flex items-center gap-2.5 min-w-0">
                                            <div class="w-5 h-5 rounded-md flex items-center justify-center border transition"
                                                 :class="serviceBookingForm.addons.includes(addon.id) ? 'bg-[#F97316] border-[#F97316] text-white' : 'border-slate-300 bg-white'">
                                                <i class="fa-solid fa-check text-[9px]" x-show="serviceBookingForm.addons.includes(addon.id)"></i>
                                            </div>
                                            <span class="text-xs font-bold truncate" x-text="addon.name"></span>
                                        </div>
                                        <span class="text-xs font-extrabold text-[#F97316] whitespace-nowrap" x-text="'+' + formatCurrency(addon.price)"></span>
                                    </div>
                                </template>
                            </div>
                        </div>

                        <!-- ĐƯA ĐÓN PETSHIP (ĐIỀU PHỐI XE): LẬP TỨC MỞ RỘNG (EXPAND) CÁC TRƯỜNG KHI TICK CHỌN -->
                        <div class="p-5 bg-orange-50/80 rounded-3xl border border-orange-200/90 space-y-4">
                            <label class="flex items-start gap-3 cursor-pointer">
                                <input type="checkbox" x-model="serviceBookingForm.petShip" class="w-5 h-5 rounded text-[#F97316] focus:ring-orange-500 border-slate-300 mt-0.5">
                                <div class="flex-1">
                                    <div class="flex items-center justify-between flex-wrap gap-1">
                                        <h5 class="font-bold text-sm text-slate-900 flex items-center gap-2">
                                            <i class="fa-solid fa-van-shuttle text-[#F97316]"></i>
                                            <span>Đăng ký dịch vụ đưa đón PetShip</span>
                                        </h5>
                                        <span class="text-xs font-extrabold text-[#F97316] bg-white px-2.5 py-1 rounded-xl shadow-2xs border border-orange-200">+60.000đ (2 chiều)</span>
                                    </div>
                                    <p class="text-xs text-slate-500 mt-1">Xe chuyên dụng điều hòa mát lạnh, lồng thoáng khí riêng biệt, tài xế có bảo hiểm và chứng chỉ an toàn thú cưng.</p>
                                </div>
                            </label>

                            <!-- FORM LẬP TỨC MỞ RỘNG (EXPAND) THÊM CÁC TRƯỜNG THEO YÊU CẦU -->
                            <div x-show="serviceBookingForm.petShip" x-collapse x-transition class="pt-3 border-t border-orange-200/60 space-y-3">
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                                    <div>
                                        <label class="block font-bold text-slate-700 mb-1">
                                            <i class="fa-solid fa-clock text-[#F97316] mr-1"></i> Khung giờ tài xế đón bé tại nhà:
                                        </label>
                                        <select x-model="serviceBookingForm.petShipPickupTime" class="w-full bg-white border border-slate-300 rounded-xl px-3 py-2.5 text-slate-800 font-semibold focus:outline-none focus:ring-2 focus:ring-orange-500">
                                            <option value="08:00 - 09:00">08:00 - 09:00 (Sáng sớm)</option>
                                            <option value="08:30 - 09:30">08:30 - 09:30 (Đầu giờ sáng)</option>
                                            <option value="09:30 - 10:30">09:30 - 10:30 (Giữa buổi sáng)</option>
                                            <option value="13:30 - 14:30">13:30 - 14:30 (Đầu giờ chiều)</option>
                                            <option value="15:00 - 16:00">15:00 - 16:00 (Chiều mát)</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block font-bold text-slate-700 mb-1">
                                            <i class="fa-solid fa-house-chimney-user text-emerald-600 mr-1"></i> Khung giờ tài xế trả bé về nhà:
                                        </label>
                                        <select x-model="serviceBookingForm.petShipDropoffTime" class="w-full bg-white border border-slate-300 rounded-xl px-3 py-2.5 text-slate-800 font-semibold focus:outline-none focus:ring-2 focus:ring-orange-500">
                                            <option value="16:00 - 17:00">16:00 - 17:00 (Cuối buổi chiều)</option>
                                            <option value="16:30 - 17:30">16:30 - 17:30 (Tan tầm)</option>
                                            <option value="17:30 - 18:30">17:30 - 18:30 (Đầu giờ tối)</option>
                                            <option value="18:30 - 19:30">18:30 - 19:30 (Buổi tối)</option>
                                        </select>
                                    </div>
                                </div>

                                <!-- CHECKBOX BẮT BUỘC -->
                                <label class="flex items-start gap-2.5 p-3 rounded-2xl bg-white border border-orange-300 cursor-pointer text-xs">
                                    <input type="checkbox" x-model="serviceBookingForm.petShipCommitment" required class="w-4 h-4 rounded text-[#F97316] focus:ring-orange-500 border-slate-300 mt-0.5">
                                    <span class="text-slate-800 font-bold leading-relaxed">
                                        Tôi cam kết sẽ có mặt tại nhà vào các khung giờ trên để bàn giao/nhận lại bé. <span class="text-rose-500 font-extrabold">* (Bắt buộc)</span>
                                    </span>
                                </label>
                            </div>
                        </div>

                        <!-- NÚT ĐIỀU HƯỚNG BƯỚC 2: QUAY LẠI & TIẾP TỤC -->
                        <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                            <button type="button" @click="bookingWizardStep = 1" class="px-5 py-3 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs sm:text-sm transition flex items-center gap-2 cursor-pointer">
                                <i class="fa-solid fa-arrow-left"></i>
                                <span>Quay lại Bước 1</span>
                            </button>
                            <button type="button" @click="bookingWizardStep = 3" class="px-6 py-3.5 bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-bold text-xs sm:text-sm rounded-2xl shadow-md shadow-orange-500/25 transition flex items-center gap-2 cursor-pointer active:scale-95">
                                <span>Tiếp tục: Ghi Chú & Xác Nhận</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </button>
                        </div>
                    </div>

                    <!-- ==================================================== -->
                    <!-- BƯỚC 3: GHI CHÚ Y TẾ & TÓM TẮT THANH TOÁN -->
                    <!-- ==================================================== -->
                    <div x-show="bookingWizardStep === 3" class="space-y-6 animate-fadeIn" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                        
                        <div class="pb-3 border-b border-slate-100">
                            <h3 class="text-base sm:text-lg font-black text-slate-900 flex items-center gap-2">
                                <span class="w-7 h-7 rounded-full bg-[#F97316] text-white flex items-center justify-center text-xs font-black">3</span>
                                <span>Ghi Chú Y Tế & Tóm Tắt Thanh Toán</span>
                            </h3>
                            <p class="text-xs text-slate-500 mt-1">Kiểm tra thông tin chi phí minh bạch và xác nhận đặt lịch</p>
                        </div>

                        <!-- 1. TEXTAREA GHI CHÚ ĐẶC NHIỆM -->
                        <div class="space-y-2">
                            <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                                <i class="fa-solid fa-notes-medical text-[#F97316] mr-1"></i> Ghi chú đặc nhiệm (Dị ứng, Tính cách...):
                            </label>
                            <textarea x-model="serviceBookingForm.notes" rows="3"
                                      placeholder="VD: Bé sợ tiếng máy sấy to, dị ứng xà phòng bạc hà, da mẫn cảm hoặc đang có vết xước nhẹ..."
                                      class="w-full bg-slate-50 border border-slate-300 rounded-2xl p-4 text-xs sm:text-sm text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:bg-white resize-none shadow-2xs"></textarea>
                        </div>

                        <!-- 2. KHỐI TÓM TẮT CHI PHÍ (ORDER SUMMARY): BÓC TÁCH RÕ RÀNG 4 KHOẢN THEO YÊU CẦU -->
                        <div class="bg-slate-50 rounded-3xl p-5 sm:p-6 border border-slate-200 space-y-4">
                            <h4 class="font-black text-sm uppercase tracking-wider text-slate-800 flex items-center justify-between pb-2 border-b border-slate-200">
                                <span>Tóm Tắt Chi Phí Lịch Hẹn (Order Summary)</span>
                                <span class="text-xs text-[#F97316] font-extrabold" x-text="petBookingDetail.name + ' (' + petBookingDetail.weight + ' kg)'"></span>
                            </h4>

                            <div class="space-y-3 text-xs sm:text-sm">
                                <!-- Khoản 1: Giá Spa Cơ Bản -->
                                <div class="flex items-center justify-between text-slate-700">
                                    <span class="flex items-center gap-2">
                                        <i class="fa-solid fa-shower text-cyan-600 text-xs"></i>
                                        <span>[Giá Spa Cơ Bản] Spa Tắm Sấy Thảo Mộc:</span>
                                    </span>
                                    <span class="font-bold text-slate-900" x-text="formatCurrency(servicePricingTab === 'hotel' ? hotelFee : getGroomingSpaPrice())"></span>
                                </div>

                                <!-- Khoản 2: Phí Nâng Cấp Groom/Shave -->
                                <div class="flex items-center justify-between text-slate-700" x-show="servicePricingTab !== 'hotel'">
                                    <span class="flex items-center gap-2">
                                        <i class="fa-solid fa-scissors text-amber-600 text-xs"></i>
                                        <span>[Phí Nâng Cấp Groom/Shave] <span x-text="groomingCutType === 'grooming' ? 'Cắt Tỉa Tạo Kiểu (Grooming)' : (groomingCutType === 'shave' ? 'Cạo Lông Vệ Sinh (Shave)' : 'Không nâng cấp')"></span>:</span>
                                    </span>
                                    <span class="font-bold text-slate-900" x-text="getGroomingUpgradeDiff() > 0 ? ('+' + formatCurrency(getGroomingUpgradeDiff())) : '0 đ'"></span>
                                </div>

                                <!-- Khoản 3: Phí Add-ons -->
                                <div class="flex items-center justify-between text-slate-700">
                                    <span class="flex items-center gap-2">
                                        <i class="fa-solid fa-plus-circle text-purple-600 text-xs"></i>
                                        <span>[Phí Add-ons] Dịch vụ cộng thêm (<span x-text="serviceBookingForm.addons ? serviceBookingForm.addons.length : 0"></span> mục):</span>
                                    </span>
                                    <span class="font-bold text-slate-900" x-text="totalAddonsCost > 0 ? ('+' + formatCurrency(totalAddonsCost)) : '0 đ'"></span>
                                </div>

                                <!-- Khoản 4: Phí PetShip -->
                                <div class="flex items-center justify-between text-slate-700">
                                    <span class="flex items-center gap-2">
                                        <i class="fa-solid fa-van-shuttle text-[#F97316] text-xs"></i>
                                        <span>[Phí PetShip] Đưa đón tận nơi (2 chiều):</span>
                                    </span>
                                    <span class="font-bold text-slate-900" x-text="serviceBookingForm.petShip ? ('+' + formatCurrency(60000)) : '0 đ'"></span>
                                </div>

                                <!-- Dòng tổng chi phí -->
                                <div class="pt-3 border-t border-slate-200 flex items-center justify-between">
                                    <span class="text-sm sm:text-base font-extrabold text-slate-900">Tổng Chi Phí Dự Kiến:</span>
                                    <span class="text-xl sm:text-2xl font-black text-[#F97316]" x-text="formatCurrency(totalServiceCost)"></span>
                                </div>

                                <!-- Tiền cọc 50% nếu là Pet Hotel -->
                                <template x-if="servicePricingTab === 'hotel'">
                                    <div class="mt-3 p-3 bg-amber-50 rounded-2xl border border-amber-200 text-xs space-y-1">
                                        <div class="flex justify-between font-bold text-amber-900">
                                            <span>Tiền cọc giữ phòng (50%):</span>
                                            <span class="text-base text-orange-600 font-black" x-text="formatCurrency(depositAmount)"></span>
                                        </div>
                                        <div class="flex justify-between text-slate-500 italic text-[11px]">
                                            <span>Số tiền còn lại (thanh toán khi trả bé):</span>
                                            <span class="font-semibold text-slate-700" x-text="formatCurrency(remainingAmount)"></span>
                                        </div>
                                    </div>
                                </template>
                            </div>
                        </div>

                        <!-- 3. NÚT HÀNH ĐỘNG (FOOTER FORM) -->
                        <div class="pt-4 border-t border-slate-100 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4">
                            <!-- Nút Quay lại -->
                            <button type="button" @click="bookingWizardStep = 2" class="px-5 py-3 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs sm:text-sm transition flex items-center justify-center gap-2 cursor-pointer">
                                <i class="fa-solid fa-arrow-left"></i>
                                <span>Quay lại</span>
                            </button>

                            <!-- Hai Nút Hành Động: Thêm vào giỏ hàng (Secondary) & Thanh toán ngay (Primary) -->
                            <div class="flex flex-col sm:flex-row items-stretch gap-3">
                                <!-- Nút Secondary: Thêm vào giỏ hàng -->
                                <button type="button" @click="submitServiceBooking(false)"
                                        class="border-2 border-[#F97316] bg-white text-[#F97316] hover:bg-orange-50 font-black text-xs sm:text-sm px-6 py-3.5 rounded-2xl transition flex items-center justify-center gap-2 cursor-pointer active:scale-95 shadow-2xs">
                                    <i class="fa-solid fa-cart-plus"></i>
                                    <span>Thêm vào giỏ hàng</span>
                                </button>

                                <!-- Nút Primary: Thanh toán ngay & Đặt lịch -->
                                <button type="button" @click="submitServiceBooking(true)"
                                        class="bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-black text-xs sm:text-sm px-8 py-3.5 rounded-2xl shadow-lg shadow-orange-500/30 transition transform flex items-center justify-center gap-2 cursor-pointer active:scale-95">
                                    <i class="fa-solid fa-calendar-check"></i>
                                    <span x-text="servicePricingTab === 'hotel' ? 'Thanh toán cọc 50% & Đặt lịch' : 'Thanh toán ngay & Đặt lịch'"></span>
                                    <i class="fa-solid fa-arrow-right text-xs"></i>
                                </button>
                            </div>
                        </div>
                    </div>

</div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 4: PETSHARE360 (MẠNG XÃ HỘI HIỆN ĐẠI 1440PX - 3 CỘT) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'petshare'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- BỐ CỤC 3 CỘT (SOCIAL FEED LAYOUT 1440PX) -->
                <div class="flex flex-col lg:flex-row gap-6 justify-center items-start">
                    
                    <!-- CỘT TRÁI (SIDEBAR TRÁI - 280PX) -->
                    <div class="w-full lg:w-[280px] flex-shrink-0 space-y-4">
                        
                        <!-- Thẻ Hồ Sơ Chủ & Pet -->
                        <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm text-center relative overflow-hidden">
                            <div class="h-16 bg-gradient-to-r from-brand-600 to-teal-500 -mx-5 -mt-5 mb-4"></div>
                            <img :src="customerProfile.avatar" class="w-16 h-16 rounded-full object-cover border-4 border-white shadow-md mx-auto -mt-12 relative z-10">
                            <h4 class="font-bold text-base text-slate-800 mt-2" x-text="customerProfile.name"></h4>
                            <p class="text-xs text-brand-600 font-semibold" x-text="'Bé yêu: ' + customerProfile.pets[0].name + ' (Corgi)'"></p>
                            
                            <div class="grid grid-cols-2 gap-2 mt-4 pt-3 border-t border-slate-100 text-center">
                                <div>
                                    <span class="text-xs text-slate-400 block">Bài viết</span>
                                    <span class="font-extrabold text-slate-800 text-sm">18</span>
                                </div>
                                <div>
                                    <span class="text-xs text-slate-400 block">Thành viên</span>
                                    <span class="text-xs font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded-full inline-block mt-0.5">VIP Gold</span>
                                </div>
                            </div>
                        </div>

                        <!-- Menu Nhanh (Interactive Navigation) -->
                        <div class="bg-white rounded-3xl p-4 border border-slate-200/90 shadow-sm space-y-1.5 text-xs sm:text-sm font-semibold">
                            <!-- 1. Bảng tin chung -->
                            <button type="button" @click="activeMenuTab = 'general_feed'" 
                                    :class="activeMenuTab === 'general_feed' ? 'bg-[#f0fdf9] text-[#0f766e] font-bold shadow-2xs' : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900 font-medium'"
                                    class="w-full py-2.5 px-3.5 rounded-2xl flex items-center gap-3 text-left transition duration-200 group">
                                <i class="fa-solid fa-newspaper text-base transition-colors" :class="activeMenuTab === 'general_feed' ? 'text-[#0f766e]' : 'text-slate-400 group-hover:text-slate-600'"></i>
                                <span>Bảng tin chung</span>
                            </button>

                            <!-- 2. Bài viết của tôi -->
                            <button type="button" @click="activeMenuTab = 'my_posts'" 
                                    :class="activeMenuTab === 'my_posts' ? 'bg-[#f0fdf9] text-[#0f766e] font-bold shadow-2xs' : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900 font-medium'"
                                    class="w-full py-2.5 px-3.5 rounded-2xl flex items-center gap-3 text-left transition duration-200 group">
                                <i class="fa-solid fa-user-pen text-base transition-colors" :class="activeMenuTab === 'my_posts' ? 'text-[#0f766e]' : 'text-slate-400 group-hover:text-slate-600'"></i>
                                <span>Bài viết của tôi</span>
                            </button>

                            <!-- 3. Mẹo chăm sóc từ Bác sĩ Thú y -->
                            <button type="button" @click="activeMenuTab = 'vet_tips'" 
                                    :class="activeMenuTab === 'vet_tips' ? 'bg-[#f0fdf9] text-[#0f766e] font-bold shadow-2xs' : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900 font-medium'"
                                    class="w-full py-2.5 px-3.5 rounded-2xl flex items-center gap-3 text-left transition duration-200 group">
                                <i class="fa-solid fa-stethoscope text-base transition-colors" :class="activeMenuTab === 'vet_tips' ? 'text-[#0f766e]' : 'text-teal-500 group-hover:text-teal-600'"></i>
                                <span>Mẹo chăm sóc từ Bác sĩ Thú y</span>
                            </button>

                            <!-- 4. Chuỗi Streak chăm sóc Pet -->
                            <button type="button" @click="activeMenuTab = 'pet_streak'" 
                                    :class="activeMenuTab === 'pet_streak' ? 'bg-[#f0fdf9] text-[#0f766e] font-bold shadow-2xs' : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900 font-medium'"
                                    class="w-full py-2.5 px-3.5 rounded-2xl flex items-center gap-3 text-left transition duration-200 group">
                                <i class="fa-solid fa-fire text-base transition-colors" :class="activeMenuTab === 'pet_streak' ? 'text-[#0f766e]' : 'text-amber-500 group-hover:text-amber-600'"></i>
                                <span>Chuỗi Streak chăm sóc Pet</span>
                            </button>
                        </div>

                        <!-- Khối Hashtag Hot -->
                        <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm space-y-3">
                            <h5 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                                <i class="fa-solid fa-hashtag text-brand-600"></i>Hashtag Đang Hot
                            </h5>
                            <div class="flex flex-wrap gap-1.5">
                                <span class="text-xs bg-slate-100 hover:bg-brand-50 hover:text-brand-600 text-slate-600 font-medium px-2.5 py-1 rounded-lg cursor-pointer transition">#PoodleSàiGòn</span>
                                <span class="text-xs bg-slate-100 hover:bg-brand-50 hover:text-brand-600 text-slate-600 font-medium px-2.5 py-1 rounded-lg cursor-pointer transition">#MèoAnhLôngNgắn</span>
                                <span class="text-xs bg-slate-100 hover:bg-brand-50 hover:text-brand-600 text-slate-600 font-medium px-2.5 py-1 rounded-lg cursor-pointer transition">#KinhNghiệmTắmPet</span>
                                <span class="text-xs bg-slate-100 hover:bg-brand-50 hover:text-brand-600 text-slate-600 font-medium px-2.5 py-1 rounded-lg cursor-pointer transition">#PetCare360Spa</span>
                            </div>
                        </div>
                    </div>

                    <!-- CỘT GIỮA (MAIN FEED - 600PX) -->
                    <div class="w-full lg:w-[600px] flex-shrink-0 space-y-5" @scroll.window.debounce.150ms="handleFeedScroll()">
                        
                        <style>
                        @keyframes heartPop {
                            0% { transform: scale(1); }
                            40% { transform: scale(1.4); }
                            70% { transform: scale(0.9); }
                            100% { transform: scale(1); }
                        }
                        .animate-heart-pop {
                            animation: heartPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                        }
                        </style>

                        <!-- ==================== TRƯỜNG HỢP 1: TAB CHUỖI STREAK CHĂM SÓC PET ==================== -->
                        <template x-if="activeMenuTab === 'pet_streak'">
                            <div class="space-y-5 animate-fadeIn">
                                <!-- 1. Hero Streak Banner -->
                                <div class="bg-gradient-to-br from-amber-500 via-orange-500 to-rose-500 text-white rounded-3xl p-6 shadow-xl relative overflow-hidden">
                                    <div class="relative z-10 space-y-4">
                                        <div class="flex items-center justify-between">
                                            <span class="inline-flex items-center gap-1.5 bg-white/20 px-3 py-1 rounded-full text-xs font-extrabold backdrop-blur-md">
                                                <i class="fa-solid fa-fire text-amber-200 animate-bounce"></i> Chuỗi Chăm Sóc Liên Tục
                                            </span>
                                            <span class="text-xs bg-black/20 px-2.5 py-1 rounded-full font-bold backdrop-blur-sm">
                                                Top 5% Sen Chuyên Cần 🏅
                                            </span>
                                        </div>

                                        <div class="space-y-1">
                                            <div class="flex items-baseline gap-2">
                                                <h3 class="text-3xl sm:text-4xl font-black tracking-tight" x-text="streakDays + ' Ngày'"></h3>
                                                <span class="text-xl sm:text-2xl font-black text-amber-200">🔥</span>
                                            </div>
                                            <p class="text-xs sm:text-sm text-orange-100 font-medium">Bé cưng đang nhận được sự chăm sóc tận tâm nhất mỗi ngày từ bạn!</p>
                                        </div>

                                        <!-- Thanh Tiến Trình Milestone -->
                                        <div class="bg-black/20 rounded-2xl p-3.5 backdrop-blur-md space-y-2">
                                            <div class="flex items-center justify-between text-xs font-bold">
                                                <span>Mục tiêu mốc tiếp theo: 14 ngày</span>
                                                <span class="text-amber-200">12/14 ngày (85%)</span>
                                            </div>
                                            <div class="w-full h-3 bg-white/20 rounded-full overflow-hidden p-0.5">
                                                <div class="h-full bg-gradient-to-r from-amber-200 to-white rounded-full transition-all duration-500 shadow-sm" style="width: 85.7%"></div>
                                            </div>
                                            <div class="flex items-center justify-between text-[11px] text-orange-100">
                                                <span>Phần thưởng mốc: Voucher 50% Spa & Huy hiệu Bạc</span>
                                                <span class="font-bold underline cursor-pointer" @click="showToast('Bạn chỉ cần check-in thêm 2 ngày nữa để mở khóa voucher 50%!')">Chi tiết</span>
                                            </div>
                                        </div>

                                        <!-- 3 Chỉ Số Nhanh -->
                                        <div class="grid grid-cols-3 gap-2.5 pt-1">
                                            <div class="bg-white/10 rounded-2xl p-2.5 text-center backdrop-blur-sm">
                                                <div class="text-lg font-black">96%</div>
                                                <div class="text-[10px] text-orange-100 font-medium">Mục tiêu đạt</div>
                                            </div>
                                            <div class="bg-white/10 rounded-2xl p-2.5 text-center backdrop-blur-sm">
                                                <div class="text-lg font-black">48</div>
                                                <div class="text-[10px] text-orange-100 font-medium">Lượt check-in</div>
                                            </div>
                                            <div class="bg-white/10 rounded-2xl p-2.5 text-center backdrop-blur-sm">
                                                <div class="text-lg font-black">1,250</div>
                                                <div class="text-[10px] text-orange-100 font-medium">PetPoints</div>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <!-- Background decorative shapes -->
                                    <div class="absolute -right-8 -bottom-8 w-44 h-44 bg-white/10 rounded-full blur-2xl pointer-events-none"></div>
                                    <div class="absolute right-12 top-6 w-24 h-24 bg-amber-400/20 rounded-full blur-xl pointer-events-none"></div>
                                </div>

                                <!-- 2. Lịch Check-in Tuần Này -->
                                <div class="bg-white rounded-3xl p-5 border border-slate-200/90 shadow-sm space-y-3">
                                    <div class="flex items-center justify-between">
                                        <h4 class="font-extrabold text-xs sm:text-sm text-slate-800 flex items-center gap-2">
                                            <i class="fa-regular fa-calendar-check text-brand-600"></i>
                                            <span>Lịch Check-in Tuần Này (21/10 - 27/10)</span>
                                        </h4>
                                        <span class="text-xs font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">
                                            6/7 ngày hoàn thành
                                        </span>
                                    </div>

                                    <div class="grid grid-cols-7 gap-2 text-center pt-1">
                                        <template x-for="item in streakDaysOfWeek" :key="item.day">
                                            <div class="space-y-1.5">
                                                <div class="text-[11px] font-bold text-slate-400" x-text="item.day"></div>
                                                <div :class="item.today ? 'bg-orange-500 text-white shadow-md shadow-orange-500/30 ring-2 ring-orange-300' : (item.done ? 'bg-emerald-500 text-white' : 'bg-slate-100 text-slate-400')" class="w-10 h-10 sm:w-11 sm:h-11 mx-auto rounded-2xl flex items-center justify-center font-bold text-xs transition duration-200">
                                                    <template x-if="item.today">
                                                        <i class="fa-solid fa-fire text-base"></i>
                                                    </template>
                                                    <template x-if="!item.today && item.done">
                                                        <i class="fa-solid fa-check text-sm"></i>
                                                    </template>
                                                    <template x-if="!item.today && !item.done">
                                                        <i class="fa-regular fa-clock text-xs"></i>
                                                    </template>
                                                </div>
                                                <div class="text-[10px] text-slate-500" x-text="item.date"></div>
                                            </div>
                                        </template>
                                    </div>
                                </div>

                                <!-- 3. Nhiệm Vụ Chăm Sóc Hôm Nay (Interactive Checklist) -->
                                <div class="bg-white rounded-3xl p-5 border border-slate-200/90 shadow-sm space-y-3">
                                    <div class="flex items-center justify-between">
                                        <div>
                                            <h4 class="font-extrabold text-xs sm:text-sm text-slate-800 flex items-center gap-2">
                                                <i class="fa-solid fa-list-check text-orange-500"></i>
                                                <span>Nhiệm Vụ Chăm Sóc Hôm Nay</span>
                                            </h4>
                                            <p class="text-[11px] text-slate-400 mt-0.5">Check-in để duy trì chuỗi Streak & tích lũy PetPoints</p>
                                        </div>
                                        <span class="text-xs font-bold text-orange-600 bg-orange-50 px-2 py-0.5 rounded-full" x-text="streakChecklist.filter(t => t.completed).length + '/' + streakChecklist.length + ' xong'"></span>
                                    </div>

                                    <div class="space-y-2 pt-1">
                                        <template x-for="task in streakChecklist" :key="task.id">
                                            <div @click="toggleStreakCheckItem(task)" :class="task.completed ? 'bg-emerald-50/60 border-emerald-200/80' : 'bg-slate-50/80 hover:bg-slate-100 border-slate-200/70'" class="p-3.5 rounded-2xl border flex items-center justify-between gap-3 cursor-pointer transition group">
                                                <div class="flex items-center gap-3 min-w-0">
                                                    <div :class="task.completed ? 'bg-emerald-500 text-white' : 'bg-white border-2 border-slate-300 text-transparent group-hover:border-orange-500'" class="w-6 h-6 rounded-full flex items-center justify-center text-xs flex-shrink-0 transition">
                                                        <i class="fa-solid fa-check text-[10px]"></i>
                                                    </div>
                                                    <div class="min-w-0">
                                                        <div :class="task.completed ? 'line-through text-slate-500' : 'text-slate-800 font-bold'" class="text-xs sm:text-sm truncate" x-text="task.title"></div>
                                                        <div class="text-[11px] text-slate-400 flex items-center gap-2 mt-0.5">
                                                            <span x-text="task.time"></span>
                                                            <span>•</span>
                                                            <span class="text-amber-600 font-semibold" x-text="'+' + task.points + ' PetPoints'"></span>
                                                        </div>
                                                    </div>
                                                </div>
                                                <button type="button" :class="task.completed ? 'bg-emerald-100 text-emerald-800' : 'bg-orange-500 text-white hover:bg-orange-600 shadow-xs'" class="px-3 py-1.5 rounded-xl text-xs font-bold transition flex-shrink-0">
                                                    <span x-text="task.completed ? 'Đã xong' : 'Check-in'"></span>
                                                </button>
                                            </div>
                                        </template>
                                    </div>
                                </div>

                                <!-- 4. Bộ Sưu Tập Huy Hiệu (Care Badges) -->
                                <div class="bg-white rounded-3xl p-5 border border-slate-200/90 shadow-sm space-y-3">
                                    <div class="flex items-center justify-between">
                                        <h4 class="font-extrabold text-xs sm:text-sm text-slate-800 flex items-center gap-2">
                                            <i class="fa-solid fa-award text-amber-500"></i>
                                            <span>Huy Hiệu Chăm Sóc Đã Đạt</span>
                                        </h4>
                                        <span class="text-xs font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded-full">
                                            3/4 Huy hiệu
                                        </span>
                                    </div>

                                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
                                        <template x-for="badge in streakBadges" :key="badge.id">
                                            <div :class="badge.unlocked ? 'bg-gradient-to-br from-amber-50/70 to-orange-50/40 border-amber-200/80' : 'bg-slate-50 border-slate-200/60 opacity-60'" class="p-3.5 rounded-2xl border flex items-center gap-3.5 transition hover:shadow-xs">
                                                <div :class="'bg-gradient-to-br ' + badge.color" class="w-12 h-12 rounded-2xl text-white flex items-center justify-center text-xl shadow-md flex-shrink-0">
                                                    <i :class="'fa-solid ' + badge.icon"></i>
                                                </div>
                                                <div class="min-w-0 flex-1">
                                                    <div class="flex items-center justify-between gap-1">
                                                        <h5 class="font-extrabold text-xs sm:text-sm text-slate-900 truncate" x-text="badge.name"></h5>
                                                        <template x-if="badge.unlocked">
                                                            <span class="text-[9px] bg-emerald-500 text-white font-black px-1.5 py-0.2 rounded-md">ĐẠT</span>
                                                        </template>
                                                    </div>
                                                    <p class="text-[11px] text-slate-500 mt-0.5 line-clamp-1" x-text="badge.desc"></p>
                                                    <template x-if="!badge.unlocked">
                                                        <div class="text-[10px] text-orange-600 font-bold mt-1" x-text="'Tiến độ: ' + badge.progress"></div>
                                                    </template>
                                                </div>
                                            </div>
                                        </template>
                                    </div>
                                </div>

                                <!-- 5. Đổi Quà Tích Lũy Từ Streak -->
                                <div class="bg-white rounded-3xl p-5 border border-slate-200/90 shadow-sm space-y-3">
                                    <div class="flex items-center justify-between">
                                        <h4 class="font-extrabold text-xs sm:text-sm text-slate-800 flex items-center gap-2">
                                            <i class="fa-solid fa-gift text-rose-500"></i>
                                            <span>Đổi Quà Tích Lũy Từ Điểm Streak</span>
                                        </h4>
                                        <div class="text-xs font-bold text-slate-600 flex items-center gap-1">
                                            <span>Số dư:</span>
                                            <span class="text-amber-600 font-extrabold">1,250 PetPoints</span>
                                        </div>
                                    </div>

                                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-1">
                                        <div class="bg-slate-50 border border-slate-200 rounded-2xl p-3 text-center space-y-2 flex flex-col justify-between">
                                            <div class="space-y-1">
                                                <div class="w-10 h-10 rounded-full bg-rose-100 text-rose-600 flex items-center justify-center mx-auto text-base">
                                                    <i class="fa-solid fa-scissors"></i>
                                                </div>
                                                <div class="font-bold text-xs text-slate-800">Voucher 50% Grooming</div>
                                                <div class="text-[10px] text-slate-400">Áp dụng cho mọi gói Spa</div>
                                            </div>
                                            <button type="button" @click="redeemStreakReward('Voucher 50% Grooming', 800)" class="w-full py-1.5 bg-orange-500 hover:bg-orange-600 text-white font-bold text-xs rounded-xl shadow-xs transition">
                                                800 Điểm
                                            </button>
                                        </div>

                                        <div class="bg-slate-50 border border-slate-200 rounded-2xl p-3 text-center space-y-2 flex flex-col justify-between">
                                            <div class="space-y-1">
                                                <div class="w-10 h-10 rounded-full bg-amber-100 text-amber-600 flex items-center justify-center mx-auto text-base">
                                                    <i class="fa-solid fa-bone"></i>
                                                </div>
                                                <div class="font-bold text-xs text-slate-800">Snack Bánh Thưởng</div>
                                                <div class="text-[10px] text-slate-400">Pate sấy thăng hoa 100g</div>
                                            </div>
                                            <button type="button" @click="redeemStreakReward('Snack Bánh Thưởng Freeze-Dried', 500)" class="w-full py-1.5 bg-orange-500 hover:bg-orange-600 text-white font-bold text-xs rounded-xl shadow-xs transition">
                                                500 Điểm
                                            </button>
                                        </div>

                                        <div class="bg-slate-50 border border-slate-200 rounded-2xl p-3 text-center space-y-2 flex flex-col justify-between">
                                            <div class="space-y-1">
                                                <div class="w-10 h-10 rounded-full bg-teal-100 text-teal-600 flex items-center justify-center mx-auto text-base">
                                                    <i class="fa-solid fa-stethoscope"></i>
                                                </div>
                                                <div class="font-bold text-xs text-slate-800">Khám Răng Miễn Phí</div>
                                                <div class="text-[10px] text-slate-400">Bác sĩ kiểm tra & lấy cao</div>
                                            </div>
                                            <button type="button" @click="showToast('Bạn cần thêm 250 PetPoints để đổi ưu đãi này! Hãy duy trì chuỗi Streak nhé.')" class="w-full py-1.5 bg-slate-200 text-slate-500 font-bold text-xs rounded-xl cursor-not-allowed">
                                                1,500 Điểm
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </template>

                        <!-- ==================== TRƯỜNG HỢP 2: CÁC TAB BẢNG TIN (FEED VIEWS) ==================== -->
                        <template x-if="activeMenuTab !== 'pet_streak'">
                            <div class="space-y-5 animate-fadeIn">
                                
                                <!-- Header Banner: Bài Viết Của Tôi -->
                                <template x-if="activeMenuTab === 'my_posts'">
                                    <div class="bg-white rounded-3xl p-4 sm:p-5 border border-slate-200/90 shadow-sm flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <div class="w-11 h-11 rounded-2xl bg-[#f0fdf9] text-[#0f766e] flex items-center justify-center text-lg flex-shrink-0">
                                                <i class="fa-solid fa-user-pen"></i>
                                            </div>
                                            <div>
                                                <div class="flex items-center gap-2">
                                                    <h4 class="font-black text-sm sm:text-base text-slate-800">Bài Viết Của Tôi</h4>
                                                    <span class="text-xs bg-[#f0fdf9] text-[#0f766e] font-extrabold px-2.5 py-0.5 rounded-full" x-text="visibleSocialPosts.length + ' bài viết'"></span>
                                                </div>
                                                <p class="text-xs text-slate-500 mt-0.5">Nhật ký khoảnh khắc và kỷ niệm do chính bạn chia sẻ</p>
                                            </div>
                                        </div>
                                        <button type="button" @click="activeMenuTab = 'general_feed'" class="text-xs text-slate-500 hover:text-brand-700 font-bold px-3 py-1.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition">
                                            <i class="fa-solid fa-arrow-left mr-1"></i> Bảng tin chung
                                        </button>
                                    </div>
                                </template>

                                <!-- Header Banner: Mẹo Chăm Sóc từ Bác Sĩ Thú Y -->
                                <template x-if="activeMenuTab === 'vet_tips'">
                                    <div class="bg-gradient-to-r from-teal-800 via-teal-700 to-emerald-800 rounded-3xl p-5 text-white shadow-md space-y-3 relative overflow-hidden">
                                        <div class="relative z-10 space-y-1.5">
                                            <div class="inline-flex items-center gap-1.5 bg-white/15 px-3 py-1 rounded-full text-[11px] font-bold text-teal-200 backdrop-blur-md">
                                                <i class="fa-solid fa-stethoscope"></i> Chuyên Mục Bác Sĩ Thú Y PetCare360
                                            </div>
                                            <h4 class="font-black text-base sm:text-lg">Mẹo Chăm Sóc & Y Khoa Thú Cưng Chuẩn Bác Sĩ</h4>
                                            <p class="text-xs text-teal-100 leading-relaxed">Tổng hợp kiến thức dinh dưỡng, phòng ngừa dịch bệnh, hướng dẫn dùng thuốc và sơ cứu tại nhà từ các Bác sĩ Thú y đầu ngành.</p>
                                        </div>
                                        <div class="flex items-center gap-2 pt-1 flex-wrap relative z-10 text-[11px] font-semibold text-teal-100">
                                            <span class="bg-white/10 hover:bg-white/20 px-2.5 py-1 rounded-xl transition cursor-pointer">#DinhDưỡng</span>
                                            <span class="bg-white/10 hover:bg-white/20 px-2.5 py-1 rounded-xl transition cursor-pointer">#TiêmChủngVaccine</span>
                                            <span class="bg-white/10 hover:bg-white/20 px-2.5 py-1 rounded-xl transition cursor-pointer">#DaLiễu & KýSinhTrùng</span>
                                            <span class="bg-white/10 hover:bg-white/20 px-2.5 py-1 rounded-xl transition cursor-pointer">#SơCứuKhẩnCấp</span>
                                        </div>
                                    </div>
                                </template>

                                <!-- Widget "Tạo Bài Viết Mới" (Hiện khi Bảng tin chung hoặc Bài viết của tôi) -->
                                <template x-if="activeMenuTab === 'general_feed' || activeMenuTab === 'my_posts'">
                                    <div class="bg-white rounded-3xl p-5 border border-slate-200/90 shadow-sm space-y-4 transition hover:shadow-md">
                                        <!-- User info & Textarea -->
                                        <div class="flex items-start gap-3">
                                            <img :src="customerProfile.avatar" class="w-10 h-10 rounded-full object-cover border border-slate-200 ring-2 ring-brand-100 flex-shrink-0">
                                            <div class="flex-1 space-y-2">
                                                <textarea x-model="newPostText" rows="2" placeholder="Hôm nay bé cưng của bạn thế nào? Chia sẻ khoảnh khắc đáng yêu ngay..." class="w-full bg-slate-50 border border-slate-200 rounded-2xl px-4 py-3 text-xs sm:text-sm text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:bg-white resize-none transition"></textarea>
                                                
                                                <!-- Tagged Pet Badge -->
                                                <template x-if="selectedTaggedPet">
                                                    <div class="inline-flex items-center gap-2 bg-gradient-to-r from-orange-50 to-amber-50 border border-orange-200/80 text-orange-800 px-3 py-1.5 rounded-full text-xs font-bold shadow-xs">
                                                        <img :src="selectedTaggedPet.avatar || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=150&q=80'" class="w-4 h-4 rounded-full object-cover ring-1 ring-orange-300">
                                                        <span x-text="'Bé: ' + selectedTaggedPet.name + ' (' + selectedTaggedPet.breed + ')'"></span>
                                                        <button type="button" @click="selectedTaggedPet = null; newPostPetId = null" class="w-4 h-4 rounded-full bg-orange-200/80 hover:bg-orange-300 text-orange-900 inline-flex items-center justify-center text-[10px] transition ml-0.5" title="Gỡ gắn thẻ">
                                                            <i class="fa-solid fa-xmark"></i>
                                                        </button>
                                                    </div>
                                                </template>
                                            </div>
                                        </div>

                                        <!-- Thumbnail Preview Grid (Ảnh/Video đã chọn) -->
                                        <template x-if="newPostMediaList && newPostMediaList.length > 0">
                                            <div class="space-y-2 pt-2 border-t border-slate-100">
                                                <div class="flex items-center justify-between text-xs font-semibold text-slate-600 px-1">
                                                    <span class="flex items-center gap-1.5 text-brand-700 font-bold">
                                                        <i class="fa-solid fa-photo-film"></i>
                                                        <span x-text="'Đã chọn ' + newPostMediaList.length + ' tệp đính kèm'"></span>
                                                    </span>
                                                    <button type="button" @click="newPostMediaList = []; newPostMedia = ''; if($refs.postFileInput) $refs.postFileInput.value=''" class="text-rose-500 hover:text-rose-700 text-xs flex items-center gap-1 transition">
                                                        <i class="fa-regular fa-trash-can"></i> Xóa tất cả
                                                    </button>
                                                </div>
                                                
                                                <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                                                    <template x-for="(media, mIdx) in newPostMediaList" :key="mIdx">
                                                        <div class="relative group rounded-2xl overflow-hidden border border-slate-200 bg-slate-900 aspect-square shadow-sm">
                                                            <template x-if="media.type === 'image'">
                                                                <img :src="media.url" class="w-full h-full object-cover group-hover:scale-105 transition duration-300">
                                                            </template>
                                                            <template x-if="media.type === 'video'">
                                                                <div class="w-full h-full relative">
                                                                    <video :src="media.url" class="w-full h-full object-cover"></video>
                                                                    <div class="absolute inset-0 bg-black/40 flex items-center justify-center">
                                                                        <div class="w-8 h-8 rounded-full bg-white/80 text-brand-700 flex items-center justify-center shadow">
                                                                            <i class="fa-solid fa-play text-xs ml-0.5"></i>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </template>
                                                            
                                                            <button type="button" @click.stop="removePostMedia(mIdx)" class="absolute top-1.5 right-1.5 w-6 h-6 rounded-full bg-black/60 hover:bg-rose-600 text-white flex items-center justify-center text-xs transition shadow-md" title="Xóa file này">
                                                                <i class="fa-solid fa-xmark"></i>
                                                            </button>
                                                        </div>
                                                    </template>
                                                </div>
                                            </div>
                                        </template>

                                        <!-- Toolbar: Ảnh/Video, Gắn thẻ Pet, Cảm xúc, Đăng bài -->
                                        <div class="flex items-center justify-between pt-2.5 border-t border-slate-100 relative">
                                            <div class="flex items-center gap-1 sm:gap-2 text-slate-500 text-xs">
                                                <input type="file" x-ref="postFileInput" accept="image/*,video/*" multiple class="hidden" @change="handlePostMediaSelect($event)">
                                                
                                                <button type="button" @click="$refs.postFileInput.click()" class="p-2 sm:px-3 sm:py-2 rounded-xl hover:bg-emerald-50 transition flex items-center gap-1.5 text-emerald-600 font-semibold active:scale-95" title="Tải ảnh / Video">
                                                    <i class="fa-solid fa-image text-sm"></i>
                                                    <span class="hidden sm:inline">Ảnh/Video</span>
                                                </button>
                                                
                                                <!-- Gắn thẻ Pet Popover -->
                                                <div class="relative">
                                                    <button type="button" @click="tagPetPopoverOpen = !tagPetPopoverOpen; emojiPickerOpen = false" class="p-2 sm:px-3 sm:py-2 rounded-xl hover:bg-brand-50 transition flex items-center gap-1.5 text-brand-600 font-semibold active:scale-95" title="Gắn thẻ Hồ sơ Pet">
                                                        <i class="fa-solid fa-paw text-sm"></i>
                                                        <span class="hidden sm:inline">Gắn thẻ Pet</span>
                                                        <i class="fa-solid fa-chevron-down text-[10px] ml-0.5 opacity-70"></i>
                                                    </button>
                                                    
                                                    <div x-show="tagPetPopoverOpen" @click.outside="tagPetPopoverOpen = false" x-transition.origin.top.left class="absolute left-0 top-full mt-2 z-40 w-72 bg-white rounded-2xl shadow-2xl border border-slate-200 p-3 space-y-2.5">
                                                        <div class="flex items-center justify-between pb-1.5 border-b border-slate-100">
                                                            <span class="font-bold text-xs text-slate-800 flex items-center gap-1.5">
                                                                <i class="fa-solid fa-paw text-brand-600"></i> Gắn thẻ thú cưng
                                                            </span>
                                                            <button type="button" @click="tagPetPopoverOpen = false" class="text-slate-400 hover:text-slate-600 text-xs">
                                                                <i class="fa-solid fa-xmark"></i>
                                                            </button>
                                                        </div>
                                                        
                                                        <div class="max-h-52 overflow-y-auto space-y-1.5 pr-1">
                                                            <template x-for="p in userPets" :key="p.id">
                                                                <button type="button" @click="selectTaggedPet(p); tagPetPopoverOpen = false" :class="selectedTaggedPet && selectedTaggedPet.id === p.id ? 'bg-orange-50 border-orange-200 ring-1 ring-orange-400' : 'hover:bg-slate-50 border-slate-100'" class="w-full flex items-center gap-3 p-2 rounded-xl border text-left transition group">
                                                                    <img :src="p.avatar || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=150&q=80'" class="w-9 h-9 rounded-full object-cover border border-slate-200 ring-1 ring-brand-100 flex-shrink-0">
                                                                    <div class="flex-1 min-w-0">
                                                                        <div class="font-bold text-xs text-slate-800 truncate" x-text="p.name"></div>
                                                                        <div class="text-[11px] text-slate-500 truncate" x-text="p.breed + ' • ' + p.weight + 'kg'"></div>
                                                                    </div>
                                                                    <template x-if="selectedTaggedPet && selectedTaggedPet.id === p.id">
                                                                        <i class="fa-solid fa-check text-orange-500 text-xs"></i>
                                                                    </template>
                                                                </button>
                                                            </template>
                                                        </div>

                                                        <template x-if="selectedTaggedPet">
                                                            <button type="button" @click="selectedTaggedPet = null; newPostPetId = null; tagPetPopoverOpen = false" class="w-full text-center py-1.5 text-xs text-rose-500 hover:text-rose-700 font-semibold border-t border-slate-100 transition">
                                                                Hủy gắn thẻ bé
                                                            </button>
                                                        </template>
                                                    </div>
                                                </div>
                                                
                                                <!-- Cảm xúc (Emoji Picker) Popover -->
                                                <div class="relative">
                                                    <button type="button" @click="emojiPickerOpen = !emojiPickerOpen; tagPetPopoverOpen = false" class="p-2 sm:px-3 sm:py-2 rounded-xl hover:bg-amber-50 transition flex items-center gap-1.5 text-amber-500 font-semibold active:scale-95" title="Chọn biểu tượng cảm xúc">
                                                        <i class="fa-solid fa-face-smile text-sm"></i>
                                                        <span class="hidden sm:inline">Cảm xúc</span>
                                                        <i class="fa-solid fa-chevron-down text-[10px] ml-0.5 opacity-70"></i>
                                                    </button>
                                                    
                                                    <div x-show="emojiPickerOpen" @click.outside="emojiPickerOpen = false" x-transition.origin.top.left class="absolute left-0 sm:left-auto sm:right-0 top-full mt-2 z-40 w-72 sm:w-80 bg-white rounded-2xl shadow-2xl border border-slate-200 p-3 space-y-3">
                                                        <div class="flex items-center justify-between pb-1.5 border-b border-slate-100">
                                                            <span class="font-bold text-xs text-slate-800 flex items-center gap-1.5">
                                                                <i class="fa-regular fa-face-smile text-amber-500"></i> Biểu tượng cảm xúc
                                                            </span>
                                                            <button type="button" @click="emojiPickerOpen = false" class="text-slate-400 hover:text-slate-600 text-xs">
                                                                <i class="fa-solid fa-xmark"></i>
                                                            </button>
                                                        </div>
                                                        
                                                        <div class="space-y-1">
                                                            <div class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Thú Cưng & Đáng Yêu</div>
                                                            <div class="grid grid-cols-8 gap-1 text-base text-center">
                                                                <template x-for="emo in ['🐶','🐱','🐾','🦴','🐕','🐈','🐩','🐹','🐰','🦊','🦁','🐼','🐨','🐟','🦜','🐢']" :key="emo">
                                                                    <button type="button" @click="insertEmoji(emo)" class="p-1 rounded-lg hover:bg-amber-50 hover:scale-125 transition transform" x-text="emo"></button>
                                                                </template>
                                                            </div>
                                                        </div>

                                                        <div class="space-y-1">
                                                            <div class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Yêu Thương & Trái Tim</div>
                                                            <div class="grid grid-cols-8 gap-1 text-base text-center">
                                                                <template x-for="emo in ['❤️','🧡','💛','💖','💕','🥰','😍','😻','😘','💓','💗','🔥','✨','🎉','🌟','💯']" :key="emo">
                                                                    <button type="button" @click="insertEmoji(emo)" class="p-1 rounded-lg hover:bg-rose-50 hover:scale-125 transition transform" x-text="emo"></button>
                                                                </template>
                                                            </div>
                                                        </div>

                                                        <div class="space-y-1">
                                                            <div class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Biểu Cảm Hài Hước</div>
                                                            <div class="grid grid-cols-8 gap-1 text-base text-center">
                                                                <template x-for="emo in ['😂','🤣','🥳','😋','😎','🤩','😜','😇','😸','😺','👏','🙌','👍','✌️','👌','🙏']" :key="emo">
                                                                    <button type="button" @click="insertEmoji(emo)" class="p-1 rounded-lg hover:bg-slate-100 hover:scale-125 transition transform" x-text="emo"></button>
                                                                </template>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            
                                            <button type="button" @click="createSocialPost()" class="bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-bold text-xs sm:text-sm px-5 py-2.5 rounded-xl shadow-md shadow-orange-500/25 transition active:scale-95 flex items-center gap-1.5">
                                                <i class="fa-solid fa-paper-plane text-xs"></i>
                                                <span>Đăng bài</span>
                                            </button>
                                        </div>
                                    </div>
                                </template>

                                <!-- DANH SÁCH BÀI ĐĂNG (FEED POST CARDS) -->
                                <div class="space-y-5">
                                    <template x-for="post in visibleSocialPosts" :key="post.id">
                                        <div class="bg-white rounded-3xl p-5 border border-slate-200/90 shadow-sm space-y-4 hover:shadow-md transition">
                                            
                                            <!-- Header Post -->
                                            <div class="flex items-center justify-between relative">
                                                <div class="flex items-center gap-3">
                                                    <img :src="post.avatar" class="w-10 h-10 rounded-full object-cover border border-slate-200 ring-2 ring-brand-100">
                                                    <div>
                                                        <div class="flex items-center gap-2 flex-wrap">
                                                            <h5 class="font-bold text-xs sm:text-sm text-slate-900" x-text="post.author"></h5>
                                                            
                                                            <!-- Badge Bác sĩ Thú Y nếu có -->
                                                            <template x-if="post.isVet || post.badge === 'Bác sĩ Thú y'">
                                                                <span class="text-[10px] bg-teal-50 border border-teal-200 text-teal-800 font-extrabold px-2 py-0.5 rounded-full inline-flex items-center gap-1 shadow-2xs">
                                                                    <i class="fa-solid fa-user-doctor text-teal-600"></i> Bác sĩ Thú y
                                                                </span>
                                                            </template>

                                                            <!-- Badge Bé Pet -->
                                                            <template x-if="post.petName">
                                                                <span class="text-[10px] bg-gradient-to-r from-orange-50 to-amber-50 border border-orange-200/80 text-orange-700 font-bold px-2 py-0.5 rounded-full inline-flex items-center gap-1" x-text="'Bé: ' + post.petName"></span>
                                                            </template>

                                                            <template x-if="post.isSaved">
                                                                <span class="text-[9px] bg-amber-100 text-amber-800 font-bold px-1.5 py-0.5 rounded-md inline-flex items-center gap-0.5" title="Đã lưu bài viết">
                                                                    <i class="fa-solid fa-bookmark text-[8px]"></i> Đã lưu
                                                                </span>
                                                            </template>
                                                        </div>
                                                        <span class="text-[11px] text-slate-400" x-text="post.time"></span>
                                                    </div>
                                                </div>
                                                
                                                <!-- Post Options (Menu 3 chấm góc phải) -->
                                                <div class="relative">
                                                    <button type="button" @click="openPostOptionsId = (openPostOptionsId === post.id ? null : post.id)" class="text-slate-400 hover:text-slate-700 w-8 h-8 rounded-full hover:bg-slate-100 flex items-center justify-center transition" title="Tùy chọn bài viết">
                                                        <i class="fa-solid fa-ellipsis"></i>
                                                    </button>

                                                    <div x-show="openPostOptionsId === post.id" @click.outside="openPostOptionsId = null" x-transition.origin.top.right class="absolute right-0 top-full mt-1.5 z-30 w-52 bg-white rounded-2xl shadow-xl border border-slate-200 py-1.5 overflow-hidden text-xs font-semibold text-slate-700">
                                                        <button type="button" @click="toggleSavePost(post.id)" class="w-full px-3.5 py-2 hover:bg-slate-50 flex items-center gap-2.5 text-left transition">
                                                            <i :class="post.isSaved ? 'fa-solid fa-bookmark text-amber-500' : 'fa-regular fa-bookmark text-slate-500'" class="w-4"></i>
                                                            <span x-text="post.isSaved ? 'Bỏ lưu bài viết' : 'Lưu bài viết'"></span>
                                                        </button>
                                                        <button type="button" @click="copyPostLink(post.id)" class="w-full px-3.5 py-2 hover:bg-slate-50 flex items-center gap-2.5 text-left transition">
                                                            <i class="fa-solid fa-link text-slate-500 w-4"></i>
                                                            <span>Sao chép liên kết</span>
                                                        </button>
                                                        <button type="button" @click="reportPost(post.id)" class="w-full px-3.5 py-2 hover:bg-slate-50 flex items-center gap-2.5 text-left transition text-amber-600">
                                                            <i class="fa-regular fa-flag w-4"></i>
                                                            <span>Báo cáo bài viết</span>
                                                        </button>
                                                        <template x-if="post.authorId === (customerProfile.id || 1) || post.author === customerProfile.name || post.time === 'Vừa xong'">
                                                            <div class="border-t border-slate-100 my-1 pt-1">
                                                                <button type="button" @click="deleteSocialPost(post.id)" class="w-full px-3.5 py-2 hover:bg-rose-50 flex items-center gap-2.5 text-left transition text-rose-600">
                                                                    <i class="fa-regular fa-trash-can w-4"></i>
                                                                    <span>Xóa bài viết</span>
                                                                </button>
                                                            </div>
                                                        </template>
                                                    </div>
                                                </div>
                                            </div>

                                            <!-- Nội dung bài viết -->
                                            <p class="text-xs sm:text-sm text-slate-700 leading-relaxed whitespace-pre-line" x-text="post.content"></p>

                                            <!-- Lưới Hình ảnh (Lightbox trigger) -->
                                            <template x-if="post.images && post.images.length > 0">
                                                <div :class="post.images.length === 1 ? 'grid grid-cols-1' : (post.images.length === 2 ? 'grid grid-cols-2 gap-2' : (post.images.length === 3 ? 'grid grid-cols-2 gap-2' : 'grid grid-cols-2 gap-2'))" class="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50">
                                                    <template x-for="(img, iidx) in post.images" :key="iidx">
                                                        <div class="relative group cursor-pointer overflow-hidden aspect-video sm:aspect-auto sm:h-56 bg-slate-900" @click="openLightbox(post.images, iidx)">
                                                            <img :src="img" @error="$event.target.src='https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=800&q=80'" class="w-full h-full object-cover group-hover:scale-105 transition duration-300">
                                                            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition flex items-center justify-center opacity-0 group-hover:opacity-100">
                                                                <span class="w-10 h-10 rounded-full bg-white/80 backdrop-blur-md text-slate-800 flex items-center justify-center shadow-lg transform scale-90 group-hover:scale-100 transition">
                                                                    <i class="fa-solid fa-magnifying-glass-plus"></i>
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </template>
                                                </div>
                                            </template>

                                            <!-- Thanh Tương Tác: Thả tim, Bình luận, Chia sẻ -->
                                            <div class="flex items-center justify-between pt-2 border-t border-slate-100 text-xs font-semibold text-slate-500">
                                                <button type="button" @click="toggleLikePost(post.id)" :class="post.isLiked ? 'text-rose-500 bg-rose-50/70 font-bold' : 'hover:text-rose-500 hover:bg-slate-50'" class="flex items-center gap-1.5 py-1.5 px-3 rounded-xl transition active:scale-95">
                                                    <i :class="[post.isLiked ? 'fa-solid fa-heart text-rose-500' : 'fa-regular fa-heart', post.likeAnimating ? 'animate-heart-pop' : '']" class="text-base transition-transform"></i>
                                                    <span x-text="post.likes"></span>
                                                </button>
                                                
                                                <button type="button" class="flex items-center gap-1.5 py-1.5 px-3 rounded-xl hover:bg-slate-50 transition hover:text-brand-600">
                                                    <i class="fa-regular fa-comment text-base"></i>
                                                    <span x-text="(post.comments ? post.comments.length : 0) + ' bình luận'"></span>
                                                </button>
                                                
                                                <div class="relative">
                                                    <button type="button" @click="openShareMenuPostId = (openShareMenuPostId === post.id ? null : post.id)" class="flex items-center gap-1.5 py-1.5 px-3 rounded-xl hover:bg-slate-50 transition hover:text-teal-600">
                                                        <i class="fa-solid fa-share-nodes text-base"></i>
                                                        <span x-text="post.shares > 0 ? ('Chia sẻ (' + post.shares + ')') : 'Chia sẻ'"></span>
                                                    </button>

                                                    <div x-show="openShareMenuPostId === post.id" @click.outside="openShareMenuPostId = null" x-transition.origin.bottom.right class="absolute right-0 bottom-full mb-2 z-30 w-56 bg-white rounded-2xl shadow-xl border border-slate-200 py-1.5 overflow-hidden text-xs font-semibold text-slate-700">
                                                        <button type="button" @click="copyPostLink(post.id)" class="w-full px-3.5 py-2 hover:bg-slate-50 flex items-center gap-2.5 text-left transition">
                                                            <i class="fa-regular fa-copy text-brand-600 w-4"></i>
                                                            <span>Sao chép liên kết</span>
                                                        </button>
                                                        <button type="button" @click="shareViaDevice(post)" class="w-full px-3.5 py-2 hover:bg-slate-50 flex items-center gap-2.5 text-left transition text-teal-700">
                                                            <i class="fa-solid fa-arrow-up-right-from-square text-teal-600 w-4"></i>
                                                            <span>Chia sẻ qua...</span>
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>

                                            <!-- Khối Bình luận real-time -->
                                            <div class="pt-2 border-t border-slate-100 space-y-2.5">
                                                <template x-if="post.comments && post.comments.length > 0">
                                                    <div class="space-y-2 max-h-60 overflow-y-auto pr-1">
                                                        <template x-for="(c, cidx) in post.comments" :key="c.id || cidx">
                                                            <div class="bg-slate-50/90 rounded-2xl p-2.5 text-xs flex items-start gap-2.5 border border-slate-100">
                                                                <img :src="c.avatar || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80'" class="w-7 h-7 rounded-full object-cover flex-shrink-0 border border-slate-200">
                                                                <div class="flex-1 min-w-0">
                                                                    <div class="flex items-center justify-between gap-1">
                                                                        <span class="font-bold text-slate-900" x-text="c.user"></span>
                                                                        <span class="text-[10px] text-slate-400" x-text="c.time || 'Vừa xong'"></span>
                                                                    </div>
                                                                    <p class="text-slate-700 mt-0.5 leading-relaxed" x-text="c.text"></p>
                                                                </div>
                                                            </div>
                                                        </template>
                                                    </div>
                                                </template>
                                                
                                                <div class="flex items-center gap-2 pt-1">
                                                    <img :src="customerProfile.avatar" class="w-7 h-7 rounded-full object-cover flex-shrink-0 border border-slate-200 hidden sm:block">
                                                    <input type="text" x-model="quickCommentText[post.id]" @keyup.enter="addCommentToPost(post.id)" placeholder="Viết bình luận cho bé cưng..." class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:bg-white transition">
                                                    <button type="button" @click="addCommentToPost(post.id)" class="px-3.5 py-2 bg-gradient-to-r from-brand-600 to-teal-600 hover:from-brand-700 hover:to-teal-700 text-white font-bold rounded-xl text-xs transition shadow-sm active:scale-95 flex items-center gap-1 flex-shrink-0">
                                                        <span>Gửi</span>
                                                        <i class="fa-solid fa-paper-plane text-[10px]"></i>
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </template>
                                </div>

                                <!-- Trạng thái khi không có bài viết trong bộ lọc -->
                                <template x-if="visibleSocialPosts.length === 0">
                                    <div class="bg-white rounded-3xl p-10 border border-slate-200/90 shadow-sm text-center space-y-3">
                                        <div class="w-16 h-16 rounded-full bg-slate-100 text-slate-400 flex items-center justify-center mx-auto text-2xl">
                                            <i class="fa-regular fa-folder-open"></i>
                                        </div>
                                        <div class="font-extrabold text-base text-slate-800">Không tìm thấy bài viết nào</div>
                                        <p class="text-xs text-slate-500 max-w-sm mx-auto" x-text="activeMenuTab === 'my_posts' ? 'Bạn chưa đăng bài viết nào. Hãy chia sẻ khoảnh khắc đầu tiên của bé cưng nhé!' : 'Chưa có cẩm nang nào trong danh mục này. Vui lòng quay lại sau.'"></p>
                                    </div>
                                </template>

                                <!-- INFINITE SCROLL (Chỉ hiện ở Bảng tin chung) -->
                                <template x-if="activeMenuTab === 'general_feed'">
                                    <div class="pt-2 pb-6">
                                        <div x-show="isLoadingMorePosts" class="flex items-center justify-center gap-2.5 py-4 text-slate-500 text-xs font-semibold bg-white rounded-2xl border border-slate-100 shadow-sm animate-pulse">
                                            <i class="fa-solid fa-circle-notch fa-spin text-brand-600 text-base"></i>
                                            <span>Đang tải thêm khoảnh khắc thú cưng mới nhất...</span>
                                        </div>

                                        <div x-show="!isLoadingMorePosts && feedVisibleCount < filteredSocialPosts.length" class="text-center">
                                            <button type="button" @click="loadMorePosts()" class="w-full py-3 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 font-bold text-xs rounded-2xl shadow-sm hover:shadow transition flex items-center justify-center gap-2 group">
                                                <i class="fa-solid fa-angles-down text-brand-600 group-hover:translate-y-0.5 transition"></i>
                                                <span>Xem thêm bài viết từ cộng đồng PetShare360</span>
                                                <span class="text-[11px] text-slate-400 font-normal" x-text="'(Còn ' + (filteredSocialPosts.length - feedVisibleCount) + ' bài viết)'"></span>
                                            </button>
                                        </div>

                                        <div x-show="feedVisibleCount >= filteredSocialPosts.length" class="text-center py-4 bg-slate-50 rounded-2xl border border-dashed border-slate-200 text-slate-400 text-xs font-medium">
                                            <i class="fa-solid fa-check-circle text-emerald-500 mr-1.5"></i>
                                            <span>Bạn đã xem hết tất cả bài viết hôm nay. Hãy đăng bài chia sẻ bé cưng của bạn nhé! 🎉</span>
                                        </div>
                                    </div>
                                </template>

                            </div>
                        </template>

                    </div>

                    <!-- CỘT PHẢI (SIDEBAR PHẢI - 300PX) -->
                    <div class="w-full lg:w-[300px] flex-shrink-0 space-y-4">
                        
                        <!-- Khối "Bác sĩ Thú y Tư vấn" (Interactive Cards with Modal Reading) -->
                        <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
                            <h5 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-2">
                                <i class="fa-solid fa-user-doctor text-brand-600"></i>Bác Sĩ Thú Y Tư Vấn
                            </h5>
                            <div class="space-y-3 text-xs">
                                <template x-for="art in vetConsultArticles" :key="art.id">
                                    <button type="button" @click="openArticleDetail(art)" class="w-full text-left p-3 rounded-2xl bg-slate-50 hover:bg-gray-50 hover:-translate-y-0.5 hover:shadow-md transition-all duration-200 cursor-pointer space-y-1.5 border border-slate-100 block group">
                                        <div class="flex items-center gap-2">
                                            <img :src="art.doctorAvatar" @error="$event.target.src='https://images.unsplash.com/photo-1594824813583-9b2f6efd559a?auto=format&fit=crop&w=150&q=80'" :alt="art.doctorName" class="w-6 h-6 rounded-full object-cover border border-teal-200 shadow-sm flex-shrink-0">
                                            <span class="text-[10px] text-teal-600 font-bold" x-text="art.doctorName"></span>
                                            <span class="text-[10px] text-slate-400 ml-auto" x-text="art.publishDate"></span>
                                        </div>
                                        <h6 class="font-bold text-slate-800 leading-snug text-xs group-hover:text-brand-600 transition" x-text="art.title"></h6>
                                    </button>
                                </template>
                            </div>
                        </div>

                        <!-- Khối "Thành viên tích cực trong tuần" (Leaderboard) -->
                        <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
                            <h5 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-2">
                                <i class="fa-solid fa-trophy text-amber-500"></i>Thành Viên Tích Cực Tuần
                            </h5>
                            <div class="space-y-2 text-xs">
                                <div class="flex items-center justify-between p-2 rounded-xl bg-amber-50/60 border border-amber-100">
                                    <div class="flex items-center gap-2">
                                        <span class="font-black text-amber-600 text-sm">#1</span>
                                        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=80&q=80" class="w-7 h-7 rounded-full object-cover">
                                        <span class="font-bold text-slate-800">Lan Hương (Bé Miu)</span>
                                    </div>
                                    <span class="font-bold text-amber-600">340 tim</span>
                                </div>
                                <div class="flex items-center justify-between p-2 rounded-xl bg-slate-50">
                                    <div class="flex items-center gap-2">
                                        <span class="font-bold text-slate-500 text-sm">#2</span>
                                        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=80&q=80" class="w-7 h-7 rounded-full object-cover">
                                        <span class="font-bold text-slate-800">Hoàng Nam (LuLu)</span>
                                    </div>
                                    <span class="font-bold text-slate-600">285 tim</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 5: PETSHOW360 (CAMERA LIVE STREAM & GIÁM SÁT DỊCH VỤ) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'petshow'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- THANH TRẠNG THÁI ĐƠN HÀNG ACTIVE (TOP SERVICE BAR) -->
                <div class="bg-slate-900 text-white rounded-3xl p-5 sm:p-6 shadow-xl border border-slate-800 space-y-4">
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-slate-800">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-2xl bg-orange-500 flex items-center justify-center text-white text-lg shadow-lg shadow-orange-500/30">
                                <i class="fa-solid fa-video animate-pulse"></i>
                            </div>
                            <div>
                                <span class="text-xs text-orange-400 font-mono font-bold tracking-wider">ĐANG GIÁM SÁT TRỰC TUYẾN</span>
                                <h3 class="text-base sm:text-lg font-extrabold text-white">Đơn hàng #SV-2026-8899 - Bé Poodle Lu đang gửi tại Pet Hotel VIP</h3>
                            </div>
                        </div>
                        <!-- Nút Liên Hệ Trực Tiếp Qua Zalo -->
                        <a href="https://zalo.me" target="_blank" class="self-start md:self-auto bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs sm:text-sm px-5 py-2.5 rounded-xl transition shadow flex items-center gap-2">
                            <i class="fa-solid fa-comment-dots text-base"></i>
                            <span>Liên Hệ Trực Tiếp Qua Zalo</span>
                        </a>
                    </div>

                    <!-- Thanh Tiến Độ Dịch Vụ 4 Bước (Bước 2 đang sáng màu cam) -->
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-xs pt-1">
                        <div class="p-3 rounded-2xl bg-slate-800/80 border border-slate-700 flex items-center gap-2.5 text-slate-300">
                            <span class="w-6 h-6 rounded-full bg-emerald-500 text-white font-bold flex items-center justify-center text-xs">✓</span>
                            <div>
                                <p class="font-bold text-white">1. Tiếp Nhận Pet</p>
                                <span class="text-[10px] text-slate-400">08:00 AM (Xong)</span>
                            </div>
                        </div>
                        <div class="p-3 rounded-2xl bg-orange-500/20 border-2 border-orange-500 flex items-center gap-2.5 text-orange-400">
                            <span class="w-6 h-6 rounded-full bg-orange-500 text-white font-bold flex items-center justify-center text-xs animate-ping">2</span>
                            <div>
                                <p class="font-bold text-orange-300">2. Đang Phục Vụ</p>
                                <span class="text-[10px] text-orange-400">Đang tại Khách sạn VIP</span>
                            </div>
                        </div>
                        <div class="p-3 rounded-2xl bg-slate-800/40 border border-slate-800 flex items-center gap-2.5 text-slate-500">
                            <span class="w-6 h-6 rounded-full bg-slate-700 text-slate-400 font-bold flex items-center justify-center text-xs">3</span>
                            <div>
                                <p class="font-bold">3. Hoàn Tất Spa</p>
                                <span class="text-[10px]">Dự kiến 04:00 PM</span>
                            </div>
                        </div>
                        <div class="p-3 rounded-2xl bg-slate-800/40 border border-slate-800 flex items-center gap-2.5 text-slate-500">
                            <span class="w-6 h-6 rounded-full bg-slate-700 text-slate-400 font-bold flex items-center justify-center text-xs">4</span>
                            <div>
                                <p class="font-bold">4. Sẵn Sàng Trả Pet</p>
                                <span class="text-[10px]">Dự kiến 06:00 PM</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- KHỐI CHÍNH: CAMERA LIVE STREAM & QUY TRÌNH CHĂM SÓC -->
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    
                    <!-- Khung Video Player Chính (2 Cột rộng) -->
                    <div class="lg:col-span-2 space-y-4">
                        <div class="bg-black rounded-3xl overflow-hidden shadow-2xl border border-slate-800 relative group aspect-video flex items-center justify-center">
                            <!-- Stream Video Mockup (Hình ảnh động chất lượng cao) -->
                            <img :src="activeLiveZone === 'dog' ? 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=1200&q=80' : (activeLiveZone === 'cat' ? 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=1200&q=80' : 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=1200&q=80')" class="w-full h-full object-cover">
                            
                            <!-- Badge Đỏ LIVE - 1080p -->
                            <div class="absolute top-4 left-4 flex items-center gap-2 z-10">
                                <span class="bg-rose-600 text-white font-black text-xs px-3 py-1 rounded-full uppercase tracking-wider flex items-center gap-1.5 shadow-lg animate-pulse">
                                    <span class="w-2 h-2 rounded-full bg-white"></span>
                                    <span>LIVE - 1080p</span>
                                </span>
                                <span class="bg-black/60 backdrop-blur text-white font-mono text-xs px-2.5 py-1 rounded-full border border-white/20">
                                    CAM-03 VIP | 60 FPS
                                </span>
                            </div>

                            <!-- Nút điều khiển Player (Phóng to, Chụp ảnh, Đổi góc quay 360) -->
                            <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-white z-10 bg-gradient-to-t from-black/80 to-transparent p-3 rounded-2xl">
                                <div class="flex items-center gap-2 text-xs">
                                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                                    <span class="font-medium">Camera HD Góc rộng 360°</span>
                                </div>
                                <div class="flex items-center gap-2">
                                    <button @click="takeLiveSnapshot()" class="p-2 rounded-xl bg-white/20 hover:bg-white/30 backdrop-blur transition text-xs flex items-center gap-1.5" title="Chụp ảnh khoảnh khắc bé">
                                        <i class="fa-solid fa-camera"></i>
                                        <span class="hidden sm:inline">Chụp khoảnh khắc</span>
                                    </button>
                                    <button @click="toggleLiveCameraAngle()" class="p-2 rounded-xl bg-white/20 hover:bg-white/30 backdrop-blur transition text-xs flex items-center gap-1.5" title="Đổi góc quay 360">
                                        <i class="fa-solid fa-arrows-rotate"></i>
                                        <span class="hidden sm:inline" x-text="'Góc quay ' + liveCameraAngle + '°'"></span>
                                    </button>
                                    <button class="p-2 rounded-xl bg-white/20 hover:bg-white/30 backdrop-blur transition text-xs" title="Toàn màn hình">
                                        <i class="fa-solid fa-expand"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Thanh chuyển đổi Khu Vực (Zone Switcher Tabs) -->
                        <div class="bg-white rounded-2xl p-2 border border-slate-200 shadow-sm flex gap-2">
                            <button @click="activeLiveZone = 'dog'" :class="activeLiveZone === 'dog' ? 'bg-brand-600 text-white font-bold' : 'text-slate-600 hover:bg-slate-100'" class="flex-1 py-2.5 px-3 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-1.5">
                                <i class="fa-solid fa-dog"></i>
                                <span>Khu Vực Chó</span>
                            </button>
                            <button @click="activeLiveZone = 'cat'" :class="activeLiveZone === 'cat' ? 'bg-brand-600 text-white font-bold' : 'text-slate-600 hover:bg-slate-100'" class="flex-1 py-2.5 px-3 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-1.5">
                                <i class="fa-solid fa-cat"></i>
                                <span>Khu Vực Mèo</span>
                            </button>
                            <button @click="activeLiveZone = 'play'" :class="activeLiveZone === 'play' ? 'bg-brand-600 text-white font-bold' : 'text-slate-600 hover:bg-slate-100'" class="flex-1 py-2.5 px-3 rounded-xl text-xs sm:text-sm transition flex items-center justify-center gap-1.5">
                                <i class="fa-solid fa-baseball"></i>
                                <span>Khu Vực Vui Chơi</span>
                            </button>
                        </div>
                    </div>

                    <!-- Khối Quy Trình Chăm Sóc Trong Ngày (Daily Care Workflow - 1 Cột) -->
                    <div class="bg-white rounded-3xl p-5 sm:p-6 border border-slate-200 shadow-sm space-y-4">
                        <div class="pb-3 border-b border-slate-100">
                            <h4 class="font-extrabold text-base text-slate-900">Nhật Ký Chăm Sóc Bé Lu Hôm Nay</h4>
                            <p class="text-xs text-slate-400">Cập nhật trực tiếp từ nhân viên trực ca</p>
                        </div>

                        <!-- Vertical Timeline -->
                        <div class="space-y-4 relative before:absolute before:left-3 before:top-2 before:bottom-2 before:w-0.5 before:bg-slate-200">
                            <template x-for="(tl, tidx) in dailyCareTimeline" :key="tidx">
                                <div class="relative pl-7 space-y-1">
                                    <div :class="tl.status === 'done' ? 'bg-emerald-500' : (tl.status === 'in_progress' ? 'bg-orange-500 ring-4 ring-orange-200' : 'bg-slate-300')" class="w-4 h-4 rounded-full absolute left-1 top-1"></div>
                                    <div class="flex items-center justify-between">
                                        <span class="text-xs font-bold text-slate-900" x-text="tl.time"></span>
                                        <span :class="tl.status === 'done' ? 'bg-emerald-100 text-emerald-800' : (tl.status === 'in_progress' ? 'bg-orange-100 text-orange-800 font-bold' : 'bg-slate-100 text-slate-600')" class="text-[10px] px-2 py-0.2 rounded-full" x-text="tl.statusText"></span>
                                    </div>
                                    <p class="text-xs text-slate-700 font-medium" x-text="tl.task"></p>
                                    <template x-if="tl.photo">
                                        <img :src="tl.photo" class="w-20 h-16 rounded-xl object-cover border border-slate-200 shadow-sm mt-1">
                                    </template>
                                    <div class="flex items-center justify-between pt-1">
                                        <span class="text-[10px] text-slate-400" x-text="'Phụ trách: ' + tl.staff"></span>
                                        <button @click="sendStaffMessage(tl.staff)" class="text-[10px] text-brand-600 hover:underline font-bold">Gửi lời nhắn</button>
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 6: ĐƠN HÀNG (DASHBOARD QUẢN LÝ ĐƠN HÀNG CHUYÊN NGHIỆP) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'orders'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">

                <!-- 1. BOX LỊCH SỬ GIAO DỊCH & ĐƠN HÀNG (NẰM TRÊN CÙNG THEO YÊU CẦU) -->
                <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-slate-100 gap-2">
                        <div>
                            <h3 class="font-extrabold text-base sm:text-lg text-slate-900 flex items-center gap-2">
                                <i class="fa-solid fa-receipt text-[#F97316]"></i>Lịch Sử Giao Dịch & Đơn Hàng
                            </h3>
                            <p class="text-xs text-slate-500 mt-0.5">Theo dõi lịch sử đơn hàng, phương thức thanh toán và trạng thái giao dịch</p>
                        </div>
                        <span class="text-xs bg-orange-50 text-orange-800 font-extrabold px-3 py-1.5 rounded-xl border border-orange-200 self-start sm:self-auto" x-text="'Tổng cộng: ' + (customerOrders ? customerOrders.length : 0) + ' giao dịch'"></span>
                    </div>

                    <div class="overflow-x-auto border border-slate-200 rounded-2xl">
                        <table class="w-full text-left text-xs border-collapse">
                            <thead class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                                <tr>
                                    <th class="py-3 px-4">Mã đơn</th>
                                    <th class="py-3 px-4">Ngày đặt</th>
                                    <th class="py-3 px-4">Sản phẩm / Dịch vụ</th>
                                    <th class="py-3 px-4 text-center">Tổng tiền</th>
                                    <th class="py-3 px-4 text-center">Phương thức</th>
                                    <th class="py-3 px-4 text-center">Trạng thái</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-100 font-medium">
                                <template x-for="ord in customerOrders" :key="'acc-ord-' + ord.id">
                                    <tr class="hover:bg-slate-50 transition">
                                        <td class="py-3 px-4 font-mono font-bold text-[#F97316]" x-text="ord.id"></td>
                                        <td class="py-3 px-4 text-slate-500" x-text="ord.date"></td>
                                        <td class="py-3 px-4 font-semibold text-slate-800" x-text="ord.items"></td>
                                        <td class="py-3 px-4 text-center font-bold text-slate-900" x-text="formatCurrency(ord.total)"></td>
                                        <td class="py-3 px-4 text-center text-slate-500" x-text="ord.paymentMethod"></td>
                                        <td class="py-3 px-4 text-center">
                                            <span class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800" x-text="ord.status"></span>
                                        </td>
                                    </tr>
                                </template>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 2. COMPONENT QUẢN LÝ ĐƠN HÀNG & DỊCH VỤ (NẰM NGAY BÊN DƯỚI) -->
                
                <!-- Header Dashboard -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200">
                    <div>
                        <h2 class="text-2xl font-black text-slate-900">Quản Lý Đơn Hàng & Dịch Vụ</h2>
                        <p class="text-xs sm:text-sm text-slate-500">Xem tiến độ vận chuyển, xem hóa đơn chi tiết, đánh giá và mua lại nhanh chóng</p>
                    </div>
                    <!-- Bộ lọc trạng thái -->
                    <div class="flex flex-wrap gap-1.5">
                        <button @click="orderFilterStatus = 'all'" :class="orderFilterStatus === 'all' ? 'bg-brand-600 text-white font-bold' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'" class="px-3 py-1.5 rounded-xl text-xs transition">Tất cả</button>
                        <button @click="orderFilterStatus = 'shipping'" :class="orderFilterStatus === 'shipping' ? 'bg-brand-600 text-white font-bold' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'" class="px-3 py-1.5 rounded-xl text-xs transition">Đang giao</button>
                        <button @click="orderFilterStatus = 'delivered'" :class="orderFilterStatus === 'delivered' ? 'bg-brand-600 text-white font-bold' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'" class="px-3 py-1.5 rounded-xl text-xs transition">Đã giao</button>
                    </div>
                </div>

                <!-- Danh sách thẻ đơn hàng -->
                <div class="space-y-5">
                    <template x-for="ord in customerOrdersEnhanced" :key="ord.id">
                        <div x-show="orderFilterStatus === 'all' || orderFilterStatus === ord.status" class="bg-white rounded-3xl p-5 sm:p-6 border border-slate-200 shadow-sm space-y-4">
                            
                            <!-- Header Đơn Hàng: Mã, Ngày, Trạng thái -->
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-slate-100 gap-2">
                                <div class="flex items-center gap-3">
                                    <span class="text-base font-extrabold text-slate-900 cursor-pointer hover:text-brand-600 transition" @click="openOrderCheckoutSummary(ord)" x-text="ord.orderCode"></span>
                                    <span class="text-xs text-slate-400" x-text="'Ngày đặt: ' + ord.date"></span>
                                </div>
                                <div class="flex items-center gap-2">
                                    <!-- Badge Trạng thái vận chuyển -->
                                    <span :class="ord.badgeColor" class="px-3 py-1 rounded-full text-xs font-bold border" x-text="ord.statusText"></span>
                                </div>
                            </div>

                            <!-- Khối Shipper (Nếu đang giao) -->
                            <template x-if="ord.status === 'shipping' && ord.shipper">
                                <div class="p-3 bg-indigo-50/70 rounded-2xl border border-indigo-100 flex items-center justify-between gap-3">
                                    <div class="flex items-center gap-2.5 text-xs text-indigo-900">
                                        <i class="fa-solid fa-motorcycle text-indigo-600 text-base"></i>
                                        <span>Shipper: <strong x-text="ord.shipper.name"></strong> - SĐT: <strong x-text="ord.shipper.phone"></strong></span>
                                    </div>
                                    <a :href="'tel:' + ord.shipper.phone" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-sm transition flex items-center gap-1.5">
                                        <i class="fa-solid fa-phone"></i>
                                        <span>Gọi Shipper</span>
                                    </a>
                                </div>
                            </template>

                            <!-- Danh sách sản phẩm trong đơn -->
                            <div class="space-y-3">
                                <template x-for="(item, iidx) in ord.items" :key="iidx">
                                    <div class="flex items-center gap-3 sm:gap-4">
                                        <img :src="item.image || item.img || getItemImage(item)" @error="$event.target.src='https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80'" class="w-16 h-16 rounded-2xl object-cover border border-slate-200">
                                        <div class="flex-1 min-w-0">
                                            <h5 class="font-bold text-xs sm:text-sm text-slate-800 truncate" x-text="item.name"></h5>
                                            <p class="text-xs text-slate-400 mt-0.5" x-text="'Phân loại: ' + item.variant + ' | SL: x' + item.qty"></p>
                                        </div>
                                        <div class="text-right">
                                            <span class="text-xs sm:text-sm font-bold text-slate-900" x-text="formatCurrency(item.price * item.qty)"></span>
                                        </div>
                                    </div>
                                </template>
                            </div>

                            <!-- Tóm tắt thanh toán & 4 Nút Hành Động ở góc dưới bên phải -->
                            <div class="pt-4 border-t border-slate-100 flex flex-col md:flex-row md:items-center justify-between gap-4">
                                <div>
                                    <span class="text-xs text-slate-500">Tổng số tiền thanh toán:</span>
                                    <span class="text-lg font-extrabold text-orange-600 ml-1.5" x-text="formatCurrency(ord.total)"></span>
                                </div>
                                <div class="flex flex-wrap items-center gap-2">
                                    <!-- 1. Nút Chi tiết đơn hàng -->
                                    <button @click="openOrderCheckoutSummary(ord)" class="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs transition flex items-center gap-1.5">
                                        <i class="fa-solid fa-receipt"></i>
                                        <span>Chi tiết đơn hàng</span>
                                    </button>

                                    <!-- 2. Nút Mua lại -->
                                    <button @click="reorderItems(ord)" class="px-4 py-2 rounded-xl bg-orange-50 hover:bg-orange-100 text-orange-700 font-bold text-xs transition flex items-center gap-1.5">
                                        <i class="fa-solid fa-rotate-right"></i>
                                        <span>Mua lại</span>
                                    </button>

                                    <!-- 3. Nút Đánh giá sản phẩm (chỉ khi Đã giao / Hoàn thành) -->
                                    <template x-if="ord.status === 'delivered'">
                                        <button @click="openReviewModal(ord)" class="px-4 py-2 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-700 font-bold text-xs transition flex items-center gap-1.5">
                                            <i class="fa-solid fa-star"></i>
                                            <span>Đánh giá sản phẩm</span>
                                        </button>
                                    </template>

                                    <!-- Xem ảnh xác nhận giao hàng (POD) -->
                                    <template x-if="ord.status === 'delivered' && ord.podPhoto">
                                        <button @click="openPODModal(ord)" class="px-4 py-2 rounded-xl bg-emerald-50 hover:bg-emerald-100 text-emerald-700 font-bold text-xs transition flex items-center gap-1.5">
                                            <i class="fa-solid fa-image"></i>
                                            <span>Xem ảnh POD</span>
                                        </button>
                                    </template>

                                    <!-- 4. Nút Yêu cầu Trả hàng / Hoàn tiền -->
                                    <template x-if="ord.status === 'delivered'">
                                        <button @click="openRefundModal(ord)" class="px-4 py-2 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-700 font-bold text-xs transition flex items-center gap-1.5">
                                            <i class="fa-solid fa-arrow-rotate-left"></i>
                                            <span>Trả hàng / Hoàn tiền</span>
                                        </button>
                                    </template>
                                </div>
                            </div>
                        </div>
                    </template>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 7: TÀI KHOẢN (SAAS DASHBOARD ACCOUNT THEO YÊU CẦU) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'account' || activeCustomerTab === 'profile'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- Header Trang Tài Khoản & Navigation Subtabs (Đã xóa nút Đơn Hàng) -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-200 gap-3">
                    <div>
                        <h2 class="text-2xl font-black text-slate-900">Quản Lý Tài Khoản Cá Nhân</h2>
                        <p class="text-xs sm:text-sm text-slate-500">Cập nhật hồ sơ chủ nuôi, danh sách thú cưng và sổ địa chỉ giao hàng</p>
                    </div>
                    <!-- Subtabs Bar (3 nút: Hồ Sơ Của Tôi, Hồ Sơ Thú Cưng, Sổ Địa Chỉ) -->
                    <div class="flex items-center gap-1.5 bg-slate-100 p-1.5 rounded-2xl self-start sm:self-auto overflow-x-auto text-xs font-bold">
                        <button @click="activeTab = 'profile'" :class="activeTab === 'profile' ? 'bg-[#F97316] text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-3.5 py-1.5 rounded-xl transition cursor-pointer">
                            Hồ Sơ Của Tôi
                        </button>
                        <button @click="activeTab = 'pets'" :class="activeTab === 'pets' ? 'bg-[#F97316] text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-3.5 py-1.5 rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <i class="fa-solid fa-paw text-[11px]"></i>
                            <span>Hồ Sơ Thú Cưng</span>
                        </button>
                        <button @click="activeTab = 'address'" :class="activeTab === 'address' ? 'bg-[#F97316] text-white shadow-xs' : 'text-slate-600 hover:text-slate-900'" class="px-3.5 py-1.5 rounded-xl transition flex items-center gap-1 cursor-pointer">
                            <i class="fa-solid fa-map-location-dot text-[11px]"></i>
                            <span>Sổ Địa Chỉ</span>
                        </button>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    
                    <!-- CỘT TRÁI: SIDEBAR NAVIGATION TRANG TÀI KHOẢN -->
                    <div class="space-y-6">
                        
                        <!-- 1. USER PROFILE SUMMARY & AVATAR -->
                        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4 text-center">
                            <div class="relative inline-block mx-auto">
                                <img :src="customerProfile.avatar" class="w-20 h-20 rounded-full object-cover border-4 border-orange-500 shadow-md">
                                <button class="absolute bottom-0 right-0 w-7 h-7 rounded-full bg-slate-900 text-white text-xs flex items-center justify-center hover:bg-orange-600 transition shadow" title="Thay đổi avatar">
                                    <i class="fa-solid fa-camera"></i>
                                </button>
                            </div>
                            <div>
                                <h4 class="font-extrabold text-base text-slate-900" x-text="customerProfile.name"></h4>
                                <p class="text-xs text-slate-400 mt-0.5" x-text="customerProfile.email"></p>
                                <span class="inline-block mt-2 text-[10px] bg-amber-100 text-amber-800 font-extrabold px-3 py-1 rounded-full uppercase tracking-wider" x-text="customerProfile.rank || 'Gold Member'"></span>
                            </div>
                        </div>

                        <!-- 2. SIDEBAR MENU TRANG TÀI KHOẢN (3 NÚT TƯƠNG TÁC: PROFILE, PETS, ADDRESS) -->
                        <div class="bg-white rounded-3xl p-4 border border-slate-200 shadow-sm space-y-2">
                            <div class="text-[11px] font-black uppercase text-slate-400 tracking-wider px-3 py-1">Menu Quản Lý</div>
                            
                            <!-- Nút 1: Hồ Sơ Của Tôi -->
                            <button type="button" @click="activeTab = 'profile'" 
                                    :class="activeTab === 'profile' ? 'bg-gradient-to-r from-orange-500 to-amber-500 text-white font-bold shadow-md shadow-orange-500/25' : 'bg-slate-50 text-slate-700 hover:bg-slate-100 font-semibold'"
                                    class="w-full py-3 px-4 rounded-2xl flex items-center gap-3 text-left transition duration-200 cursor-pointer">
                                <i class="fa-solid fa-user-circle text-lg" :class="activeTab === 'profile' ? 'text-white' : 'text-[#F97316]'"></i>
                                <div class="flex-1">
                                    <div class="text-xs sm:text-sm">Hồ Sơ Của Tôi</div>
                                    <div class="text-[10px] opacity-80 font-normal">Thông tin cá nhân & mật khẩu</div>
                                </div>
                                <i class="fa-solid fa-chevron-right text-xs opacity-60"></i>
                            </button>

                            <!-- Nút 2: Hồ Sơ Thú Cưng -->
                            <button type="button" @click="activeTab = 'pets'" 
                                    :class="activeTab === 'pets' ? 'bg-gradient-to-r from-orange-500 to-amber-500 text-white font-bold shadow-md shadow-orange-500/25' : 'bg-slate-50 text-slate-700 hover:bg-slate-100 font-semibold'"
                                    class="w-full py-3 px-4 rounded-2xl flex items-center gap-3 text-left transition duration-200 cursor-pointer">
                                <i class="fa-solid fa-paw text-lg" :class="activeTab === 'pets' ? 'text-white' : 'text-[#F97316]'"></i>
                                <div class="flex-1">
                                    <div class="text-xs sm:text-sm">Hồ Sơ Thú Cưng</div>
                                    <div class="text-[10px] opacity-80 font-normal">Quản lý bé cưng & cân nặng</div>
                                </div>
                                <i class="fa-solid fa-chevron-right text-xs opacity-60"></i>
                            </button>

                            <!-- Nút 3: Sổ Địa Chỉ -->
                            <button type="button" @click="activeTab = 'address'" 
                                    :class="activeTab === 'address' ? 'bg-gradient-to-r from-orange-500 to-amber-500 text-white font-bold shadow-md shadow-orange-500/25' : 'bg-slate-50 text-slate-700 hover:bg-slate-100 font-semibold'"
                                    class="w-full py-3 px-4 rounded-2xl flex items-center gap-3 text-left transition duration-200 cursor-pointer">
                                <i class="fa-solid fa-map-location-dot text-lg" :class="activeTab === 'address' ? 'text-white' : 'text-[#F97316]'"></i>
                                <div class="flex-1">
                                    <div class="text-xs sm:text-sm">Sổ Địa Chỉ</div>
                                    <div class="text-[10px] opacity-80 font-normal">Giao hàng & PetShip đón rước</div>
                                </div>
                                <i class="fa-solid fa-chevron-right text-xs opacity-60"></i>
                            </button>
                        </div>

                        <!-- 3. CẤP BẬC THÀNH VIÊN (MEMBERSHIP TIER CARD) -->
                        <div class="bg-gradient-to-br from-amber-500 to-orange-600 rounded-3xl p-6 text-white shadow-xl space-y-4 relative overflow-hidden">
                            <div class="flex items-center justify-between">
                                <div>
                                    <span class="text-xs uppercase font-extrabold tracking-wider text-amber-100">Hạng Thành Viên</span>
                                    <h4 class="text-xl font-black mt-0.5" x-text="customerProfile.rank || 'Gold Member'"></h4>
                                </div>
                                <div class="w-12 h-12 rounded-2xl bg-white/20 backdrop-blur flex items-center justify-center text-2xl">
                                    <i class="fa-solid fa-crown text-amber-200"></i>
                                </div>
                            </div>
                            <div class="space-y-1">
                                <div class="flex justify-between text-xs font-semibold">
                                    <span>Tích điểm: <strong>1.450 pts</strong></span>
                                    <span>Mục tiêu: 2.000 pts</span>
                                </div>
                                <div class="w-full bg-black/20 h-2.5 rounded-full overflow-hidden">
                                    <div class="bg-white h-full rounded-full" style="width: 72.5%"></div>
                                </div>
                            </div>
                            <p class="text-[11px] text-amber-100">Được giảm 5% toàn bộ sản phẩm và miễn phí 02 lần đưa đón PetShip/tháng.</p>
                        </div>
                    </div>

                    <!-- CỘT PHẢI: CONDITIONAL RENDERING THEO activeTab (PROFILE, PETS, ADDRESS) -->
                    <div class="lg:col-span-2 space-y-6">
                        
                        <!-- TAB 1: FORM HỒ SƠ CỦA TÔI (Hiển thị khi activeTab === 'profile') -->
                        <div x-show="activeTab === 'profile'" class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6 animate-fadeIn">
                            <div class="flex items-center justify-between pb-4 border-b border-slate-100">
                                <div>
                                    <h3 class="font-extrabold text-base sm:text-lg text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-user-circle text-[#F97316]"></i>Thông Tin Hồ Sơ Cá Nhân
                                    </h3>
                                    <p class="text-xs text-slate-500 mt-0.5">Quản lý họ tên, số điện thoại, email và mật khẩu bảo mật tài khoản</p>
                                </div>
                                <span class="text-xs bg-emerald-50 text-emerald-700 font-bold px-3 py-1 rounded-full border border-emerald-200">
                                    <i class="fa-solid fa-circle-check mr-1 text-[10px]"></i>Đã Xác Thực
                                </span>
                            </div>

                            <div class="space-y-4 text-xs sm:text-sm">
                                <div>
                                    <label class="block text-slate-700 mb-1.5 font-bold">Họ và tên chủ nuôi:</label>
                                    <input type="text" x-model="customerProfile.name" class="w-full bg-slate-50 border border-slate-300 rounded-2xl px-4 py-3 text-slate-800 font-semibold focus:outline-none focus:ring-2 focus:ring-orange-500 focus:bg-white shadow-2xs">
                                </div>
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-slate-700 mb-1.5 font-bold">Địa chỉ Email:</label>
                                        <input type="email" x-model="customerProfile.email" class="w-full bg-slate-50 border border-slate-300 rounded-2xl px-4 py-3 text-slate-800 font-semibold focus:outline-none focus:ring-2 focus:ring-orange-500 focus:bg-white shadow-2xs">
                                    </div>
                                    <div>
                                        <label class="block text-slate-700 mb-1.5 font-bold">Số điện thoại liên hệ:</label>
                                        <input type="tel" x-model="customerProfile.phone" class="w-full bg-slate-50 border border-slate-300 rounded-2xl px-4 py-3 text-slate-800 font-semibold focus:outline-none focus:ring-2 focus:ring-orange-500 focus:bg-white shadow-2xs">
                                    </div>
                                </div>
                            </div>

                            <div class="pt-4 border-t border-slate-100 flex flex-wrap gap-3">
                                <button type="button" @click="saveAccountProfile()" class="px-6 py-3 bg-[#F97316] hover:bg-orange-600 text-white font-bold text-xs sm:text-sm rounded-2xl shadow-sm transition cursor-pointer active:scale-95">
                                    Lưu Thay Đổi
                                </button>
                                <button type="button" @click="showChangePasswordModal = true" class="px-5 py-3 bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs sm:text-sm rounded-2xl transition cursor-pointer">
                                    Đổi Mật Khẩu
                                </button>
                            </div>
                        </div>

                        <!-- TAB 2: HỒ SƠ THÚ CƯNG ĐÃ LƯU (Hiển thị khi activeTab === 'pets') -->
                        <div x-show="activeTab === 'pets'" class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6 animate-fadeIn">
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-100 gap-2">
                                <div>
                                    <h3 class="font-extrabold text-base sm:text-lg text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-paw text-[#F97316]"></i>Hồ Sơ Thú Cưng Đã Lưu
                                    </h3>
                                    <p class="text-xs text-slate-500 mt-0.5">Danh sách các bé cưng trong gia đình dùng để đặt lịch Spa, Grooming & Khách sạn</p>
                                </div>
                                <button @click="openAddPetModal()" class="px-4 py-2 bg-orange-50 hover:bg-orange-100 text-[#F97316] font-bold text-xs rounded-xl border border-orange-200 transition flex items-center gap-1.5 shadow-2xs self-start sm:self-auto cursor-pointer">
                                    <i class="fa-solid fa-plus"></i>
                                    <span>Thêm Thú Cưng Mới</span>
                                </button>
                            </div>

                            <!-- Lưới thẻ thú cưng (Grid Layout) -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                
                                <!-- Thẻ Chức Năng: "Thêm thú cưng mới" (UI nét đứt) -->
                                <div @click="openAddPetModal()" class="border-2 border-dashed border-slate-300 hover:border-[#F97316] bg-slate-50/50 hover:bg-orange-50/30 rounded-3xl p-6 flex flex-col items-center justify-center text-center cursor-pointer transition group min-h-[200px]">
                                    <div class="w-12 h-12 rounded-2xl bg-orange-100 text-[#F97316] flex items-center justify-center text-xl group-hover:scale-110 transition shadow-sm mb-2">
                                        <i class="fa-solid fa-plus"></i>
                                    </div>
                                    <span class="font-black text-sm text-slate-800 group-hover:text-[#F97316]">Thêm Thú Cưng Mới</span>
                                    <span class="text-xs text-slate-400 mt-1 max-w-[200px]">Tải avatar, nhập cân nặng, giống loài, giới tính & thói quen</span>
                                </div>

                                <!-- Danh Sách Thẻ Thú Cưng Đã Lưu -->
                                <template x-for="p in (customerProfile.pets || pets)" :key="'pet-card-' + p.id">
                                    <div class="p-4 rounded-3xl border border-slate-200 bg-white hover:border-orange-200 hover:shadow-md transition space-y-3 flex flex-col justify-between group">
                                        <div>
                                            <div class="flex items-start gap-3">
                                                <img :src="p.avatar || p.image || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=150&q=80'" class="w-16 h-16 rounded-2xl object-cover border-2 border-slate-100 shadow-sm flex-shrink-0">
                                                <div class="min-w-0 flex-1">
                                                    <div class="flex items-center justify-between">
                                                        <h4 class="font-extrabold text-sm text-slate-900 truncate" x-text="p.name"></h4>
                                                        <span class="text-[10px] font-bold px-2 py-0.5 rounded-full" :class="p.species === 'Mèo' ? 'bg-indigo-100 text-indigo-700' : 'bg-amber-100 text-amber-800'" x-text="p.species || 'Chó'"></span>
                                                    </div>
                                                    <p class="text-xs text-[#F97316] font-semibold truncate mt-0.5" x-text="p.breed || 'Chưa rõ giống'"></p>
                                                    <div class="flex items-center gap-2 text-[11px] text-slate-500 mt-1.5 flex-wrap">
                                                        <span class="bg-orange-50 text-orange-800 px-2 py-0.5 rounded-md font-extrabold" x-text="(p.weight || '0') + ' kg'"></span>
                                                        <span>•</span>
                                                        <span x-text="p.gender || 'Đực'"></span>
                                                        <template x-if="p.neutered">
                                                            <span class="text-emerald-600 font-semibold">• Đã triệt sản</span>
                                                        </template>
                                                    </div>
                                                </div>
                                            </div>
                                            
                                            <!-- Dị ứng & thói quen -->
                                            <div class="mt-3 pt-2 border-t border-slate-100 text-xs text-slate-600 space-y-1">
                                                <div class="flex items-center gap-1.5 text-[11px]">
                                                    <i class="fa-solid fa-triangle-exclamation text-amber-500 text-[10px]"></i>
                                                    <span>Dị ứng: <strong class="text-slate-800" x-text="p.allergies || 'Không có'"></strong></span>
                                                </div>
                                                <div class="flex items-center gap-1.5 text-[11px]">
                                                    <i class="fa-solid fa-heart-pulse text-rose-500 text-[10px]"></i>
                                                    <span>Tính cách: <span class="text-slate-700" x-text="p.behavior || 'Ngoan ngoãn, thích vuốt ve'"></span></span>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Nút Sửa / Xóa -->
                                        <div class="pt-2 border-t border-slate-100 flex items-center justify-end gap-2">
                                            <button type="button" @click="openEditPetModal(p)" class="p-1.5 text-slate-400 hover:text-[#F97316] transition text-xs" title="Chỉnh sửa thông tin">
                                                <i class="fa-solid fa-pen-to-square"></i>
                                            </button>
                                            <button type="button" @click="deletePet(p.id)" class="p-1.5 text-slate-400 hover:text-rose-500 transition text-xs" title="Xóa hồ sơ bé">
                                                <i class="fa-solid fa-trash-can"></i>
                                            </button>
                                        </div>
                                    </div>
                                </template>
                            </div>
                        </div>

                        <!-- TAB 3: SỔ ĐỊA CHỈ GIAO HÀNG & ĐƯA ĐÓN (Hiển thị khi activeTab === 'address') -->
                        <div x-show="activeTab === 'address'" class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6 animate-fadeIn">
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-100 gap-3">
                                <div>
                                    <h3 class="font-black text-lg sm:text-xl text-slate-900 flex items-center gap-2">
                                        <i class="fa-solid fa-map-location-dot text-[#F97316]"></i>Sổ Địa Chỉ Giao Hàng & Đưa Đón PetShip
                                    </h3>
                                    <p class="text-xs text-slate-500 mt-1">Quản lý danh sách địa chỉ nhận hàng Shopee, giao hàng hỏa tốc 2H và đón/trả bé PetShip</p>
                                </div>
                                <button type="button" @click="openAddAddressModal()" class="px-4 py-2.5 bg-[#F97316] hover:bg-orange-600 text-white font-extrabold text-xs rounded-xl shadow-md shadow-orange-500/25 transition-all transform hover:-translate-y-0.5 flex items-center gap-2 self-start sm:self-auto cursor-pointer">
                                    <i class="fa-solid fa-plus text-xs"></i>
                                    <span>+ Thêm địa chỉ mới</span>
                                </button>
                            </div>

                            <!-- DANH SÁCH CÁC CARD ĐỊA CHỈ NẰM DỌC CHUẨN E-COMMERCE -->
                            <div class="space-y-4">
                                <template x-for="addr in (addresses || savedAddresses || [])" :key="'addr-card-' + addr.id">
                                    <div class="p-5 rounded-2xl border transition-all duration-200 bg-white hover:shadow-sm"
                                         :class="addr.isDefault ? 'border-[#F97316] ring-1 ring-orange-400/40 bg-orange-50/20' : 'border-slate-200 hover:border-slate-300'">
                                        <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-3">
                                            <!-- CỘT TRÁI: Tên người nhận | SĐT | Địa chỉ chi tiết | Tag Mặc định -->
                                            <div class="space-y-2 flex-1">
                                                <div class="flex flex-wrap items-center gap-2.5">
                                                    <span class="font-black text-sm text-slate-900" x-text="addr.name || addr.receiver || addr.recipient || 'Nguyễn Phương Thảo'"></span>
                                                    <span class="text-slate-300 text-xs">|</span>
                                                    <span class="font-mono font-bold text-xs text-slate-600" x-text="addr.phone || '0988 123 456'"></span>
                                                    <!-- Badge [Mặc định] màu cam nổi bật -->
                                                    <template x-if="addr.isDefault">
                                                        <span class="inline-flex items-center gap-1 bg-gradient-to-r from-orange-500 to-amber-500 text-white text-[10px] font-black px-2.5 py-0.5 rounded-full uppercase tracking-wider shadow-2xs">
                                                            <i class="fa-solid fa-star text-[9px]"></i> [Mặc định]
                                                        </span>
                                                    </template>
                                                </div>

                                                <div class="flex items-start gap-2 text-xs text-slate-700 leading-relaxed font-medium">
                                                    <i class="fa-solid fa-location-dot text-[#F97316] text-sm mt-0.5 shrink-0"></i>
                                                    <span x-text="addr.fullAddress || ((addr.street ? addr.street + ', ' : '') + (addr.ward ? addr.ward + ', ' : '') + (addr.district ? addr.district + ', ' : '') + 'TP. Hồ Chí Minh')"></span>
                                                </div>

                                                <div class="text-[11px] text-slate-400 flex items-center gap-2 pt-0.5">
                                                    <span class="inline-flex items-center gap-1 text-emerald-600 font-semibold">
                                                        <i class="fa-solid fa-shield-check"></i>Đã xác thực tọa độ PetShip
                                                    </span>
                                                </div>
                                            </div>

                                            <!-- CỘT PHẢI (ACTIONS): Hai nút text link 'Chỉnh sửa' và 'Xóa' -->
                                            <div class="flex items-center sm:flex-col sm:items-end justify-end gap-2.5 shrink-0 pt-2 sm:pt-0 border-t sm:border-t-0 border-slate-100">
                                                <div class="flex items-center gap-3 text-xs font-bold">
                                                    <button type="button" @click="openEditAddressModal(addr)" class="text-[#F97316] hover:text-orange-700 hover:underline flex items-center gap-1 cursor-pointer transition">
                                                        <i class="fa-regular fa-pen-to-square"></i>
                                                        <span>Chỉnh sửa</span>
                                                    </button>
                                                    <span class="text-slate-300">|</span>
                                                    <button type="button" @click="deleteAddress(addr.id)" class="text-slate-400 hover:text-rose-600 hover:underline flex items-center gap-1 cursor-pointer transition">
                                                        <i class="fa-regular fa-trash-can"></i>
                                                        <span>Xóa</span>
                                                    </button>
                                                </div>

                                                <template x-if="!addr.isDefault">
                                                    <button type="button" @click="setDefaultAddress(addr.id)" class="text-[11px] text-slate-500 hover:text-[#F97316] font-semibold underline cursor-pointer">
                                                        Thiết lập làm mặc định
                                                    </button>
                                                </template>
                                            </div>
                                        </div>
                                    </div>
                                </template>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

            <!-- ======================================================== -->
            <!-- TAB 8: GIỎ HÀNG & CHECKOUT (QUY TRÌNH 5 BƯỚC HOÀN THIỆN THEO YÊU CẦU) -->
            <!-- ======================================================== -->
            <div x-show="activeCustomerTab === 'cart' || activeCustomerTab === 'checkout'" class="space-y-6" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 translate-y-1" x-transition:enter-end="opacity-100 translate-y-0">
                
                <!-- BƯỚC 1: XEM GIỎ HÀNG ĐANG CÓ NHỮNG GÌ -->
                <div x-show="cartStep === 1" class="space-y-6">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-200 gap-2">
                        <div>
                            <h2 class="text-2xl font-black text-slate-900">GIỎ HÀNG CỦA BẠN</h2>
                            <p class="text-xs sm:text-sm text-slate-500" x-text="'Bạn đang có ' + cartItemsCount + ' sản phẩm trong giỏ hàng'"></p>
                        </div>
                        <button @click="activeCustomerTab = 'shop'" class="text-brand-600 hover:underline text-xs font-bold flex items-center gap-1">
                            <i class="fa-solid fa-arrow-left"></i>Tiếp tục mua hàng
                        </button>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        <!-- Danh sách sản phẩm dạng bảng/dòng -->
                        <div class="lg:col-span-2 space-y-6">
                            <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm overflow-x-auto">
                                <table class="w-full text-left text-xs sm:text-sm border-collapse">
                                    <thead>
                                        <tr class="border-b border-slate-200 text-slate-500 font-semibold pb-3">
                                            <th class="py-3 px-2">Sản phẩm</th>
                                            <th class="py-3 px-2">Phân loại</th>
                                            <th class="py-3 px-2 text-center">Số lượng</th>
                                            <th class="py-3 px-2 text-right">Đơn giá</th>
                                            <th class="py-3 px-2 text-right">Thành tiền</th>
                                            <th class="py-3 px-2 text-center">Xóa</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100">
                                        <template x-for="(item, cidx) in cart" :key="cidx">
                                            <tr class="hover:bg-slate-50/50">
                                                <td class="py-3.5 px-2">
                                                    <div class="flex items-center gap-3">
                                                        <img :src="item.image || item.img || getItemImage(item)" @error="$event.target.src='https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80'" class="w-12 h-12 rounded-xl object-cover border border-slate-200">
                                                        <span class="font-bold text-slate-900 line-clamp-1 max-w-[180px]" x-text="item.name"></span>
                                                    </div>
                                                </td>
                                                <td class="py-3.5 px-2 text-xs text-slate-600 font-medium" x-text="item.variantLabel || item.variant || (item.weight ? (item.weight + ' • ' + (item.flavor || 'Vị chuẩn')) : 'Tiêu chuẩn')"></td>
                                                <td class="py-3.5 px-2 text-center">
                                                    <div class="inline-flex items-center border border-slate-200 rounded-lg overflow-hidden bg-white shadow-sm">
                                                        <button type="button" @click="updateCartItemQuantity(item.id, item.variantLabel || item.variant, (item.quantity || item.qty || 1) - 1)" class="px-2.5 py-1 text-slate-500 hover:bg-slate-100 font-bold transition">−</button>
                                                        <span class="px-2.5 py-1 font-bold text-xs text-slate-800" x-text="item.quantity || item.qty || 1"></span>
                                                        <button type="button" @click="updateCartItemQuantity(item.id, item.variantLabel || item.variant, (item.quantity || item.qty || 1) + 1)" class="px-2.5 py-1 text-slate-500 hover:bg-slate-100 font-bold transition">+</button>
                                                    </div>
                                                </td>
                                                <td class="py-3.5 px-2 text-right text-slate-700 font-medium" x-text="formatCurrency(item.unitPrice || item.price)"></td>
                                                <td class="py-3.5 px-2 text-right font-extrabold text-orange-600" x-text="formatCurrency((item.unitPrice || item.price) * (item.quantity || item.qty || 1))"></td>
                                                <td class="py-3.5 px-2 text-center">
                                                    <button type="button" @click="removeFromCart(item.id)" class="text-slate-400 hover:text-rose-600 transition" title="Xóa món này">
                                                        <i class="fa-solid fa-trash-can"></i>
                                                    </button>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>

                            <!-- Khu vực bổ trợ: Ghi chú đơn hàng & Chính sách đổi trả -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-2">
                                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">Ghi chú đơn hàng:</label>
                                    <textarea x-model="cartNotes" rows="3" placeholder="Ghi chú thêm về thời gian nhận hàng, giao giờ hành chính..." class="w-full bg-slate-50 border border-slate-200 rounded-2xl p-3 text-xs text-slate-800 focus:outline-none focus:ring-1 focus:ring-brand-500"></textarea>
                                </div>
                                <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-2">
                                    <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">Chính sách Đổi/Trả PetCare360:</label>
                                    <ul class="text-xs text-slate-500 space-y-1">
                                        <li>• Đổi trả miễn phí trong 3 ngày nếu phát hiện lỗi bao bì.</li>
                                        <li>• Hỗ trợ đổi vị hạt nếu bé thú cưng mẫn cảm không hợp.</li>
                                        <li>• Đền bù 200% nếu phát hiện sản phẩm không chính hãng.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <!-- Cột tổng quan bên phải (Thông tin đơn hàng) -->
                        <div class="space-y-4">
                            <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                                <h3 class="font-extrabold text-base text-slate-900 pb-3 border-b border-slate-100">Thông Tin Đơn Hàng</h3>
                                <div class="flex justify-between text-sm">
                                    <span class="text-slate-500">Tạm tính:</span>
                                    <span class="font-extrabold text-slate-900 text-base" x-text="formatCurrency(cartSubtotal)"></span>
                                </div>
                                <!-- KHỐI COMPONENT CHỌN MÃ KHUYẾN MÃI (TICKET STYLE COMPONENT - YÊU CẦU 3.1) -->
                                <div @click="openVoucherWallet()" class="p-3.5 rounded-2xl border-2 border-dashed border-orange-300 bg-orange-50/50 hover:bg-orange-50 cursor-pointer transition flex items-center justify-between group">
                                    <div class="flex items-center gap-3">
                                        <div class="w-9 h-9 rounded-xl bg-orange-500 text-white flex items-center justify-center font-bold text-base shadow-sm group-hover:scale-105 transition">
                                            <i class="fa-solid fa-ticket"></i>
                                        </div>
                                        <div>
                                            <div class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
                                                <span>PetCare Voucher</span>
                                                <span class="text-[9px] bg-orange-100 text-orange-800 font-bold px-1.5 py-0.5 rounded">Kho Voucher</span>
                                            </div>
                                            <template x-if="!hasAppliedVouchers">
                                                <p class="text-[11px] text-slate-500 font-medium mt-0.5">Chọn hoặc nhập mã khuyến mãi</p>
                                            </template>
                                            <template x-if="hasAppliedVouchers">
                                                <div class="flex flex-wrap gap-1 mt-1">
                                                    <template x-if="appliedVouchers.shipping">
                                                        <span class="inline-flex items-center gap-1 bg-blue-100 text-blue-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-blue-200">
                                                            <i class="fa-solid fa-truck-fast text-[9px]"></i>
                                                            <span x-text="appliedVouchers.shipping.code"></span>
                                                            <button type="button" @click.stop="removeVoucher('shipping')" class="text-blue-600 hover:text-blue-900 font-black ml-1 text-xs">&times;</button>
                                                        </span>
                                                    </template>
                                                    <template x-if="appliedVouchers.order">
                                                        <span class="inline-flex items-center gap-1 bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-emerald-200">
                                                            <i class="fa-solid fa-tag text-[9px]"></i>
                                                            <span x-text="appliedVouchers.order.code"></span>
                                                            <button type="button" @click.stop="removeVoucher('order')" class="text-emerald-600 hover:text-emerald-900 font-black ml-1 text-xs">&times;</button>
                                                        </span>
                                                    </template>
                                                </div>
                                            </template>
                                        </div>
                                    </div>
                                    <div class="flex items-center gap-1 text-xs font-bold text-orange-600 group-hover:translate-x-1 transition">
                                        <span x-text="hasAppliedVouchers ? 'Đổi mã' : 'Chọn'"></span>
                                        <i class="fa-solid fa-chevron-right text-[10px]"></i>
                                    </div>
                                </div>
                                <template x-if="totalDiscount > 0">
                                    <div class="flex justify-between text-xs text-emerald-600 font-extrabold">
                                        <span>Giảm giá:</span>
                                        <span x-text="'-' + formatCurrency(totalDiscount)"></span>
                                    </div>
                                </template>
                                <!-- Nút bấm lớn màu đen "THANH TOÁN" -->
                                <button @click="goToCartStep(2)" class="w-full py-4 rounded-2xl bg-black hover:bg-slate-800 text-white font-extrabold text-base transition shadow-lg flex items-center justify-center gap-2">
                                    <span>THANH TOÁN</span>
                                    <i class="fa-solid fa-arrow-right"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- BƯỚC 2: XÁC THỰC THÔNG TIN NHẬN HÀNG (THÔNG TIN GIAO HÀNG & LỊCH HẸN DỊCH VỤ) -->
                <div x-show="cartStep === 2" class="space-y-6">
                    <!-- Header thanh tiến trình -->
                    <div class="py-3 border-b border-slate-200 flex items-center gap-2 text-xs sm:text-sm font-bold text-slate-500">
                        <span class="text-slate-400 hover:text-orange-600 cursor-pointer flex items-center gap-1" @click="goToCartStep(1)">
                            <i class="fa-solid fa-cart-shopping text-xs"></i>
                            <span>1. Giỏ hàng</span>
                        </span>
                        <i class="fa-solid fa-chevron-right text-[10px] text-slate-300"></i>
                        <span class="text-orange-600 font-extrabold flex items-center gap-1 bg-orange-50 px-2.5 py-1 rounded-lg">
                            <i class="fa-solid fa-truck-ramp-box text-xs"></i>
                            <span>2. Thông tin nhận hàng & Lịch hẹn</span>
                        </span>
                        <i class="fa-solid fa-chevron-right text-[10px] text-slate-300"></i>
                        <span class="text-slate-400 flex items-center gap-1">
                            <i class="fa-solid fa-credit-card text-xs"></i>
                            <span>3. Phương thức thanh toán</span>
                        </span>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        <!-- CỘT BÊN TRÁI: THÔNG TIN GIAO NHẬN HÀNG / LỊCH HẸN (CONDITIONAL RENDERING) -->
                        <div class="lg:col-span-2 space-y-5">

                            <!-- TRƯỜNG HỢP 1: CHỈ CÓ SẢN PHẨM VẬT LÝ (hasProduct = true & hasService = false) -->
                            <template x-if="hasProduct && !hasService">
                                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-5">
                                    <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                        <div>
                                            <span class="px-2.5 py-0.5 bg-orange-100 text-orange-700 font-extrabold text-[10px] rounded-full uppercase tracking-wider">Đơn Sản Phẩm</span>
                                            <h3 class="font-extrabold text-lg text-slate-900 mt-1 flex items-center gap-2">
                                                <i class="fa-solid fa-box-open text-orange-500"></i>
                                                <span>Thông tin nhận sản phẩm</span>
                                            </h3>
                                            <p class="text-xs text-slate-400" x-text="'Tài khoản: ' + customerProfile.name + ' (' + customerProfile.phone + ')'"></p>
                                        </div>
                                        <button @click="logout()" class="text-xs text-rose-500 hover:underline font-bold">Đăng xuất</button>
                                    </div>

                                    <!-- Option Giao tận nơi / Nhận tại cửa hàng -->
                                    <div class="space-y-2">
                                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">Phương thức nhận hàng:</label>
                                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                            <label class="p-3.5 rounded-2xl border cursor-pointer transition flex items-center gap-2.5" :class="deliveryMethod === 'door' ? 'border-orange-500 bg-orange-50/60 ring-2 ring-orange-500/20' : 'border-slate-200 hover:bg-slate-50'">
                                                <input type="radio" value="door" x-model="deliveryMethod" class="text-orange-500">
                                                <div>
                                                    <span class="font-bold text-xs sm:text-sm text-slate-800 block">Giao tận nơi</span>
                                                    <span class="text-[11px] text-slate-500">Phí giao hàng: 35.000đ (2-3 ngày)</span>
                                                </div>
                                            </label>
                                            <label class="p-3.5 rounded-2xl border cursor-pointer transition flex items-center gap-2.5" :class="deliveryMethod === 'store' ? 'border-orange-500 bg-orange-50/60 ring-2 ring-orange-500/20' : 'border-slate-200 hover:bg-slate-50'">
                                                <input type="radio" value="store" x-model="deliveryMethod" class="text-orange-500">
                                                <div>
                                                    <span class="font-bold text-xs sm:text-sm text-slate-800 block">Nhận tại cửa hàng</span>
                                                    <span class="text-[11px] text-emerald-600 font-semibold">Miễn phí nhận tại cơ sở 88 NTMK</span>
                                                </div>
                                            </label>
                                        </div>
                                    </div>

                                    <!-- Form điền địa chỉ người nhận (Kèm Validation & Inline Errors) -->
                                    <div class="space-y-3.5 text-xs sm:text-sm pt-2">
                                        <div>
                                            <label class="block text-slate-600 font-bold mb-1">Quốc gia:</label>
                                            <input type="text" value="Việt Nam" readonly class="w-full bg-slate-100 border border-slate-200 rounded-xl px-4 py-2.5 text-slate-600 font-semibold cursor-not-allowed">
                                        </div>
                                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                            <div>
                                                <label class="block text-slate-600 font-bold mb-1">Họ và tên người nhận: <span class="text-rose-500">*</span></label>
                                                <input type="text" x-model="checkoutShippingForm.name" @blur="checkoutShippingForm.touched.name = true" placeholder="Nguyễn Văn A" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white" :class="checkoutFormErrors.name ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                <p x-show="checkoutFormErrors.name" x-text="checkoutFormErrors.name" class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1"></p>
                                            </div>
                                            <div>
                                                <label class="block text-slate-600 font-bold mb-1">Số điện thoại người nhận: <span class="text-rose-500">*</span></label>
                                                <input type="tel" x-model="checkoutShippingForm.phone" @blur="checkoutShippingForm.touched.phone = true" placeholder="0909123456 (10 số)" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white font-mono" :class="checkoutFormErrors.phone ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                <p x-show="checkoutFormErrors.phone" x-text="checkoutFormErrors.phone" class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1"></p>
                                            </div>
                                        </div>

                                        <template x-if="deliveryMethod === 'door'">
                                            <div class="space-y-3 pt-1">
                                                <div>
                                                    <label class="block text-slate-600 font-bold mb-1">Địa chỉ cụ thể (Số nhà, tên đường): <span class="text-rose-500">*</span></label>
                                                    <input type="text" x-model="checkoutShippingForm.address" @blur="checkoutShippingForm.touched.address = true" placeholder="Ví dụ: 125 Hoàng Quốc Việt" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white" :class="checkoutFormErrors.address ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                    <p x-show="checkoutFormErrors.address" x-text="checkoutFormErrors.address" class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1"></p>
                                                </div>
                                                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                                                    <div>
                                                        <label class="block text-slate-500 text-[11px] font-bold mb-1">Tỉnh / Thành phố: <span class="text-rose-500">*</span></label>
                                                        <input type="text" value="TP. Hồ Chí Minh (Mã 79)" readonly class="w-full bg-slate-100 border border-slate-200 rounded-xl px-3 py-2 text-xs font-semibold text-slate-600 cursor-not-allowed">
                                                    </div>
                                                    <div>
                                                        <label class="block text-slate-500 text-[11px] font-bold mb-1">Quận / Huyện: <span class="text-rose-500">*</span></label>
                                                        <select x-model="checkoutShippingForm.district" @change="onDistrictChange(); checkoutShippingForm.touched.district = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                            <template x-for="d in currentProvinceDistricts" :key="d.name">
                                                                <option :value="d.name" x-text="d.name"></option>
                                                            </template>
                                                        </select>
                                                    </div>
                                                    <div>
                                                        <label class="block text-slate-500 text-[11px] font-bold mb-1">Phường / Xã: <span class="text-rose-500">*</span></label>
                                                        <select x-model="checkoutShippingForm.ward" @change="checkoutShippingForm.touched.ward = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                            <template x-for="w in currentDistrictWards" :key="w">
                                                                <option :value="w" x-text="w"></option>
                                                            </template>
                                                        </select>
                                                    </div>
                                                </div>
                                            </div>
                                        </template>

                                        <template x-if="deliveryMethod === 'store'">
                                            <div class="p-4 bg-orange-50/60 rounded-2xl border border-orange-200 text-xs space-y-1.5 text-slate-700">
                                                <div class="font-bold text-orange-800 flex items-center gap-1.5">
                                                    <i class="fa-solid fa-store"></i>
                                                    <span>Địa chỉ nhận hàng tại shop:</span>
                                                </div>
                                                <p class="font-semibold text-slate-900">• Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Phường Đa Kao, Quận 1, TP.HCM</p>
                                                <p class="text-slate-500">• Giờ mở cửa đón khách: 08:00 - 21:00 hàng ngày (Hotline: 028 3930 8888)</p>
                                            </div>
                                        </template>
                                    </div>
                                </div>
                            </template>

                            <!-- TRƯỜNG HỢP 2: CHỈ CÓ DỊCH VỤ (!hasProduct && hasService) -->
                            <template x-if="!hasProduct && hasService">
                                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-5">
                                    <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                        <div>
                                            <span class="px-2.5 py-0.5 bg-blue-100 text-blue-700 font-extrabold text-[10px] rounded-full uppercase tracking-wider">Đơn Dịch Vụ Trực Tiếp</span>
                                            <h3 class="font-extrabold text-lg text-slate-900 mt-1 flex items-center gap-2">
                                                <i class="fa-solid fa-calendar-check text-blue-600"></i>
                                                <span>Thông Tin Lịch Hẹn Dịch Vụ</span>
                                            </h3>
                                            <p class="text-xs text-slate-400">Dịch vụ thực hiện trực tiếp tại cơ sở hoặc qua PetShip đưa đón</p>
                                        </div>
                                        <span class="text-xs font-bold text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200 flex items-center gap-1"><i class="fa-solid fa-pen-to-square text-[10px]"></i> Có thể chỉnh sửa</span>
                                    </div>

                                    <!-- Khối Read-only: Tên khách hàng, SĐT, Cơ sở thực hiện và Địa chỉ PetShip -->
                                                                        <!-- Khối Thông Tin Lịch Hẹn Dịch Vụ (Đã Mở Khóa Chỉnh Sửa & Form Đưa Đón PetShip) -->
                                    <div class="bg-slate-50 rounded-2xl p-5 border border-slate-200 space-y-4">
                                        <!-- Mở khóa Thông tin liên hệ (Editable Contact Info) -->
                                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs sm:text-sm">
                                            <div class="space-y-1">
                                                <label class="text-slate-700 text-xs font-bold block">Tên người đại diện đặt lịch: <span class="text-rose-500">*</span></label>
                                                <input type="text" x-model="checkoutBookingContactName" @input="checkoutBookingContactTouched.name = true" placeholder="Nguyễn Phương Thảo" class="w-full bg-white border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:border-brand-500" :class="(checkoutBookingContactTouched.name && (!checkoutBookingContactName || checkoutBookingContactName.trim().length < 2)) ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                <p x-show="checkoutBookingContactTouched.name && (!checkoutBookingContactName || checkoutBookingContactName.trim().length < 2)" class="text-rose-500 text-[11px] font-semibold mt-0.5 flex items-center gap-1">
                                                    <i class="fa-solid fa-circle-exclamation"></i> Vui lòng nhập họ và tên (tối thiểu 2 ký tự)
                                                </p>
                                            </div>
                                            <div class="space-y-1">
                                                <label class="text-slate-700 text-xs font-bold block">Số điện thoại liên hệ: <span class="text-rose-500">*</span></label>
                                                <input type="tel" x-model="checkoutBookingContactPhone" @input="checkoutBookingContactTouched.phone = true" placeholder="0988 123 456 (10 số)" class="w-full bg-white border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:border-brand-500 font-mono" :class="(checkoutBookingContactTouched.phone && (!checkoutBookingContactPhone || !/^(0[35789])[0-9]{8}$/.test(checkoutBookingContactPhone.trim().replace(/\s/g,'')))) ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                <p x-show="checkoutBookingContactTouched.phone && (!checkoutBookingContactPhone || !/^(0[35789])[0-9]{8}$/.test(checkoutBookingContactPhone.trim().replace(/\s/g,'')))" class="text-rose-500 text-[11px] font-semibold mt-0.5 flex items-center gap-1">
                                                    <i class="fa-solid fa-circle-exclamation"></i> Vui lòng nhập số điện thoại hợp lệ (10 số)
                                                </p>
                                            </div>
                                        </div>

                                        <div class="space-y-1 text-xs sm:text-sm">
                                            <label class="text-slate-600 text-xs font-bold block">Cơ sở thực hiện:</label>
                                            <div class="p-3.5 bg-white rounded-xl border border-blue-200 text-slate-800 font-bold flex items-center gap-2.5 shadow-sm">
                                                <div class="w-8 h-8 rounded-lg bg-rose-50 text-rose-600 flex items-center justify-center font-bold text-sm flex-shrink-0">
                                                    <i class="fa-solid fa-location-dot"></i>
                                                </div>
                                                <div>
                                                    <span class="text-slate-900 block font-extrabold">Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Phường Đa Kao, Quận 1, TPHCM</span>
                                                    <span class="block text-[11px] text-slate-400 font-normal">Hotline cơ sở: 028 3930 8888 • Giờ mở cửa: 08:00 - 21:00 hàng ngày</span>
                                                </div>
                                            </div>
                                        </div>

                                                                                <!-- Khối Phương thức đưa đón PetShip (Case 2: Dịch vụ đơn lẻ) -->
                                        <div class="space-y-3 text-xs sm:text-sm">
                                            <div class="flex items-center justify-between">
                                                <label class="text-slate-700 text-xs font-bold flex items-center gap-1.5">
                                                    <i class="fa-solid fa-truck-ramp-box text-orange-500"></i>
                                                    <span>Phương thức đưa đón PetShip:</span>
                                                </label>
                                                <div>
                                                    <template x-if="hasPetShip">
                                                        <span class="text-[10px] text-orange-700 font-extrabold bg-orange-100 px-2.5 py-0.5 rounded-full border border-orange-200 flex items-center gap-1">
                                                            <span class="w-1.5 h-1.5 rounded-full bg-orange-500 animate-pulse"></span>
                                                            Đã chọn dịch vụ PetShip tận nhà
                                                        </span>
                                                    </template>
                                                    <template x-if="!hasPetShip">
                                                        <span class="text-[10px] text-slate-600 font-bold bg-slate-200 px-2.5 py-0.5 rounded-full border border-slate-300">
                                                            Tự đưa đón tại cơ sở
                                                        </span>
                                                    </template>
                                                </div>
                                            </div>

                                            <!-- 2 tùy chọn trực quan -->
                                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                                                <!-- Tự đưa đón -->
                                                <div @click="setPetShipMode(false)"
                                                     class="p-3.5 rounded-2xl border-2 cursor-pointer transition flex items-start gap-3 select-none"
                                                     :class="!hasPetShip ? 'border-brand-500 bg-brand-50/30 shadow-sm' : 'border-slate-200 bg-white hover:border-slate-300'">
                                                    <input type="radio" name="petship_method_case2" :checked="!hasPetShip" class="mt-0.5 text-brand-600 focus:ring-brand-500 cursor-pointer">
                                                    <div>
                                                        <span class="font-extrabold text-xs text-slate-900 block flex items-center gap-1.5">
                                                            <i class="fa-solid fa-person-walking text-slate-500"></i>
                                                            <span>Tự đưa đón tại cơ sở</span>
                                                        </span>
                                                        <span class="text-[11px] text-slate-500 block mt-0.5 leading-snug">Khách mang bé đến 88 NTMK, Q1 (Miễn phí)</span>
                                                    </div>
                                                </div>

                                                <!-- Xe PetShip -->
                                                <div @click="setPetShipMode(true)"
                                                     class="p-3.5 rounded-2xl border-2 cursor-pointer transition flex items-start gap-3 select-none"
                                                     :class="hasPetShip ? 'border-orange-500 bg-orange-50/40 shadow-sm ring-2 ring-orange-500/20' : 'border-slate-200 bg-white hover:border-slate-300'">
                                                    <input type="radio" name="petship_method_case2" :checked="hasPetShip" class="mt-0.5 text-orange-600 focus:ring-orange-500 cursor-pointer">
                                                    <div>
                                                        <span class="font-extrabold text-xs text-slate-900 block flex items-center gap-1.5">
                                                            <i class="fa-solid fa-van-shuttle text-orange-600"></i>
                                                            <span>Xe đưa đón PetShip tận nhà</span>
                                                        </span>
                                                        <span class="text-[11px] text-orange-600 font-bold block mt-0.5 leading-snug">Đón & trả bé tận cửa (+60.000đ)</span>
                                                    </div>
                                                </div>
                                            </div>

                                            <!-- Form Nhập Địa Chỉ PetShip (Render khi hasPetShip === true) -->
                                            <template x-if="hasPetShip">
                                                <div class="p-4 sm:p-5 bg-gradient-to-br from-orange-50/70 to-amber-50/40 rounded-2xl border-2 border-orange-200 space-y-3.5 animate-fadeIn">
                                                    <div class="flex items-center justify-between pb-2 border-b border-orange-200/70">
                                                        <div class="flex items-center gap-2 text-orange-900 font-extrabold text-xs sm:text-sm">
                                                            <div class="w-6 h-6 rounded-lg bg-orange-500 text-white flex items-center justify-center text-xs shadow-xs">
                                                                <i class="fa-solid fa-location-dot"></i>
                                                            </div>
                                                            <span>Địa Chỉ Đón & Trả Thú Cưng (Khu vực TP.HCM)</span>
                                                        </div>
                                                        <span class="text-[11px] text-orange-700 font-bold bg-white px-2 py-0.5 rounded-full border border-orange-200 shadow-xs">
                                                            Tài xế chuyên dụng
                                                        </span>
                                                    </div>

                                                    <!-- Ô input: Địa chỉ cụ thể (Số nhà, tên đường) (Bắt buộc) -->
                                                    <div>
                                                        <label class="block text-slate-700 text-xs font-bold mb-1.5 flex items-center justify-between">
                                                            <span>Địa chỉ cụ thể (Số nhà, tên đường): <span class="text-rose-500">*</span></span>
                                                            <span class="text-[10px] text-slate-400 font-normal">Tối thiểu 5 ký tự</span>
                                                        </label>
                                                        <div class="relative">
                                                            <input type="text"
                                                                   x-model="petShipAddress.street"
                                                                   @input="petShipAddressTouched.street = true"
                                                                   @blur="petShipAddressTouched.street = true"
                                                                   placeholder="Ví dụ: 125 Hoàng Quốc Việt, Tòa A, Phòng 402..."
                                                                   class="w-full bg-white border rounded-xl pl-10 pr-4 py-2.5 text-slate-800 text-xs sm:text-sm font-semibold focus:outline-none transition"
                                                                   :class="(petShipAddressTouched.street && (!petShipAddress.street || petShipAddress.street.trim().length < 5))
                                                                           ? 'border-rose-400 bg-rose-50/20 focus:border-rose-500 focus:ring-2 focus:ring-rose-200'
                                                                           : 'border-slate-300 focus:border-orange-500 focus:ring-2 focus:ring-orange-200'">
                                                            <i class="fa-solid fa-house text-slate-400 absolute left-3.5 top-3.5 text-xs"></i>
                                                        </div>
                                                        <p x-show="petShipAddressTouched.street && (!petShipAddress.street || petShipAddress.street.trim().length < 5)"
                                                           class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1">
                                                            <i class="fa-solid fa-circle-exclamation"></i> Vui lòng nhập địa chỉ cụ thể (tối thiểu 5 ký tự)
                                                        </p>
                                                    </div>

                                                    <!-- Tái sử dụng component AddressSelector (Dropdown Tỉnh/Thành khóa cứng, dropdown Quận/Huyện, Phường/Xã) -->
                                                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                                                        <!-- Dropdown Tỉnh/Thành phố bị khóa cứng ở 'TP. Hồ Chí Minh' -->
                                                        <div>
                                                            <label class="block text-slate-700 text-[11px] font-bold mb-1">
                                                                Tỉnh / Thành phố: <span class="text-rose-500">*</span>
                                                            </label>
                                                            <div class="relative">
                                                                <select disabled class="w-full bg-slate-100 border border-slate-300 rounded-xl px-3 py-2 text-xs font-bold text-slate-600 cursor-not-allowed appearance-none">
                                                                    <option value="TP. Hồ Chí Minh" selected>TP. Hồ Chí Minh</option>
                                                                </select>
                                                                <i class="fa-solid fa-lock text-slate-400 absolute right-3 top-2.5 text-xs"></i>
                                                            </div>
                                                        </div>

                                                        <!-- Dropdown Quận / Huyện -->
                                                        <div>
                                                            <label class="block text-slate-700 text-[11px] font-bold mb-1">
                                                                Quận / Huyện: <span class="text-rose-500">*</span>
                                                            </label>
                                                            <div class="relative">
                                                                <select x-model="petShipAddress.district"
                                                                        @change="onPetShipDistrictChange()"
                                                                        @blur="petShipAddressTouched.district = true"
                                                                        class="w-full bg-white border rounded-xl pl-3 pr-8 py-2 text-xs font-semibold focus:outline-none transition appearance-none cursor-pointer"
                                                                        :class="(petShipAddressTouched.district && (!petShipAddress.district || !petShipAddress.district.trim()))
                                                                                ? 'border-rose-400 bg-rose-50/20 focus:border-rose-500'
                                                                                : 'border-slate-300 focus:border-orange-500'">
                                                                    <option value="">-- Chọn Quận/Huyện --</option>
                                                                    <template x-for="d in petShipDistricts" :key="d.name">
                                                                        <option :value="d.name" x-text="d.name" :selected="d.name === petShipAddress.district"></option>
                                                                    </template>
                                                                </select>
                                                                <i class="fa-solid fa-chevron-down text-slate-400 absolute right-3 top-2.5 text-[10px] pointer-events-none"></i>
                                                            </div>
                                                            <p x-show="petShipAddressTouched.district && (!petShipAddress.district || !petShipAddress.district.trim())"
                                                               class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1">
                                                                <i class="fa-solid fa-circle-exclamation"></i> Vui lòng chọn Quận/Huyện
                                                            </p>
                                                        </div>

                                                        <!-- Dropdown Phường / Xã -->
                                                        <div>
                                                            <label class="block text-slate-700 text-[11px] font-bold mb-1">
                                                                Phường / Xã: <span class="text-rose-500">*</span>
                                                            </label>
                                                            <div class="relative">
                                                                <select x-model="petShipAddress.ward"
                                                                        @change="petShipAddressTouched.ward = true"
                                                                        @blur="petShipAddressTouched.ward = true"
                                                                        :disabled="!petShipAddress.district"
                                                                        class="w-full bg-white border rounded-xl pl-3 pr-8 py-2 text-xs font-semibold focus:outline-none transition appearance-none cursor-pointer disabled:bg-slate-100 disabled:cursor-not-allowed"
                                                                        :class="(petShipAddressTouched.ward && (!petShipAddress.ward || !petShipAddress.ward.trim()))
                                                                                ? 'border-rose-400 bg-rose-50/20 focus:border-rose-500'
                                                                                : 'border-slate-300 focus:border-orange-500'">
                                                                    <option value="">-- Chọn Phường/Xã --</option>
                                                                    <template x-for="w in petShipWards" :key="w">
                                                                        <option :value="w" x-text="w" :selected="w === petShipAddress.ward"></option>
                                                                    </template>
                                                                </select>
                                                                <i class="fa-solid fa-chevron-down text-slate-400 absolute right-3 top-2.5 text-[10px] pointer-events-none"></i>
                                                            </div>
                                                            <p x-show="petShipAddressTouched.ward && (!petShipAddress.ward || !petShipAddress.ward.trim())"
                                                               class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1">
                                                                <i class="fa-solid fa-circle-exclamation"></i> Vui lòng chọn Phường/Xã
                                                            </p>
                                                        </div>
                                                    </div>

                                                    <!-- Ghi chú vận chuyển -->
                                                    <div class="flex items-center gap-2 text-[11px] text-slate-500 bg-white/60 p-2.5 rounded-xl border border-orange-200/60">
                                                        <i class="fa-solid fa-circle-info text-orange-500 text-xs"></i>
                                                        <span>Tài xế PetCare360 sẽ gọi trước 15-30 phút trước khi đến đón thú cưng tại địa chỉ trên.</span>
                                                    </div>
                                                </div>
                                            </template>
                                        </div>



                                        <!-- Danh sách dịch vụ trong giỏ -->
                                        <div class="pt-3 border-t border-slate-200/80">
                                            <label class="text-slate-600 text-xs font-bold block mb-2">Chi tiết các dịch vụ đã chọn:</label>
                                            <div class="space-y-2">
                                                <template x-for="(srv, sidx) in serviceCartItems" :key="sidx">
                                                    <div class="p-3 bg-white rounded-xl border border-slate-200 flex items-center justify-between text-xs">
                                                        <div class="flex items-center gap-2.5">
                                                            <span class="w-2.5 h-2.5 rounded-full" :class="isHotelItem(srv) ? 'bg-orange-500' : 'bg-blue-500'"></span>
                                                            <div>
                                                                <p class="font-bold text-slate-900" x-text="srv.name"></p>
                                                                <p class="text-slate-400 text-[11px]" x-text="srv.variant || (srv.bookingDetails ? srv.bookingDetails.petName + ' (' + (srv.bookingDetails.date || srv.bookingDetails.checkInDate) + ')' : '')"></p>
                                                            </div>
                                                        </div>
                                                        <div class="text-right">
                                                            <span class="font-extrabold text-slate-900" x-text="formatCurrency(srv.totalCost || srv.price)"></span>
                                                            <template x-if="isHotelItem(srv)">
                                                                <span class="block text-[10px] text-orange-600 font-semibold">(Cọc 50%: <span x-text="formatCurrency(hotelDeposit)"></span>)</span>
                                                            </template>
                                                        </div>
                                                    </div>
                                                </template>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </template>

                            <!-- TRƯỜNG HỢP 3: MIXED CART (hasProduct = true & hasService = true) -->
                            <template x-if="hasProduct && hasService">
                                <div class="space-y-5">
                                    <div class="p-4 bg-gradient-to-r from-orange-50 via-amber-50 to-orange-50 rounded-2xl border border-orange-200 flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <div class="w-10 h-10 rounded-xl bg-orange-500 text-white flex items-center justify-center font-bold text-base shadow">
                                                <i class="fa-solid fa-layer-group"></i>
                                            </div>
                                            <div>
                                                <h4 class="font-extrabold text-sm text-slate-900">Giỏ Hàng Hỗn Hợp (Mixed Cart)</h4>
                                                <p class="text-xs text-slate-600">Đơn hàng gồm cả Sản phẩm vật lý & Dịch vụ thú cưng</p>
                                            </div>
                                        </div>
                                        <span class="text-[11px] font-bold text-orange-700 bg-white px-3 py-1 rounded-full border border-orange-200 shadow-sm">2 Khối Tách Biệt</span>
                                    </div>

                                    <!-- Khối 1 - "Thông tin nhận Sản phẩm" (Thẻ/Card có viền xám nhạt) -->
                                    <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-4">
                                        <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                            <div class="flex items-center gap-2.5">
                                                <span class="w-7 h-7 rounded-lg bg-orange-500 text-white font-black text-xs flex items-center justify-center shadow-sm">1</span>
                                                <h4 class="font-extrabold text-base text-slate-900">Thông tin nhận Sản phẩm</h4>
                                            </div>
                                            <span class="text-xs text-slate-400 font-semibold">Giao hàng / Nhận tại shop</span>
                                        </div>

                                        <!-- Option Giao hàng / Nhận tại shop -->
                                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                            <label class="p-3.5 rounded-2xl border cursor-pointer transition flex items-center gap-2.5" :class="deliveryMethod === 'door' ? 'border-orange-500 bg-orange-50/60 ring-2 ring-orange-500/20' : 'border-slate-200 hover:bg-slate-50'">
                                                <input type="radio" value="door" x-model="deliveryMethod" class="text-orange-500">
                                                <div>
                                                    <span class="font-bold text-xs sm:text-sm text-slate-800 block">Giao tận nơi</span>
                                                    <span class="text-[11px] text-slate-500">Phí giao hàng: 35.000đ</span>
                                                </div>
                                            </label>
                                            <label class="p-3.5 rounded-2xl border cursor-pointer transition flex items-center gap-2.5" :class="deliveryMethod === 'store' ? 'border-orange-500 bg-orange-50/60 ring-2 ring-orange-500/20' : 'border-slate-200 hover:bg-slate-50'">
                                                <input type="radio" value="store" x-model="deliveryMethod" class="text-orange-500">
                                                <div>
                                                    <span class="font-bold text-xs sm:text-sm text-slate-800 block">Nhận tại cửa hàng</span>
                                                    <span class="text-[11px] text-emerald-600 font-semibold">Miễn phí tại 88 NTMK, Q1</span>
                                                </div>
                                            </label>
                                        </div>

                                        <!-- Form điền địa chỉ người nhận Sản phẩm -->
                                        <div class="space-y-3 text-xs sm:text-sm pt-1">
                                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                                <div>
                                                    <label class="block text-slate-600 font-bold mb-1">Họ tên người nhận: <span class="text-rose-500">*</span></label>
                                                    <input type="text" x-model="checkoutShippingForm.name" @blur="checkoutShippingForm.touched.name = true" placeholder="Nguyễn Văn A" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white" :class="checkoutFormErrors.name ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                    <p x-show="checkoutFormErrors.name" x-text="checkoutFormErrors.name" class="text-rose-500 text-[11px] font-semibold mt-1"></p>
                                                </div>
                                                <div>
                                                    <label class="block text-slate-600 font-bold mb-1">Số điện thoại: <span class="text-rose-500">*</span></label>
                                                    <input type="tel" x-model="checkoutShippingForm.phone" @blur="checkoutShippingForm.touched.phone = true" placeholder="0909123456" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white font-mono" :class="checkoutFormErrors.phone ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                    <p x-show="checkoutFormErrors.phone" x-text="checkoutFormErrors.phone" class="text-rose-500 text-[11px] font-semibold mt-1"></p>
                                                </div>
                                            </div>

                                            <template x-if="deliveryMethod === 'door'">
                                                <div class="space-y-3 pt-1">
                                                    <div>
                                                        <label class="block text-slate-600 font-bold mb-1">Địa chỉ cụ thể: <span class="text-rose-500">*</span></label>
                                                        <input type="text" x-model="checkoutShippingForm.address" @blur="checkoutShippingForm.touched.address = true" placeholder="Số nhà, tên đường" class="w-full bg-slate-50 border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:bg-white" :class="checkoutFormErrors.address ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                        <p x-show="checkoutFormErrors.address" x-text="checkoutFormErrors.address" class="text-rose-500 text-[11px] font-semibold mt-1"></p>
                                                    </div>
                                                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                                                        <div>
                                                            <label class="block text-slate-500 text-[11px] font-bold mb-1">Tỉnh / Thành phố: <span class="text-rose-500">*</span></label>
                                                            <select x-model="checkoutShippingForm.city" @change="onCityChange(); checkoutShippingForm.touched.city = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                                <template x-for="p in vnProvinces" :key="p.name">
                                                                    <option :value="p.name" x-text="p.name"></option>
                                                                </template>
                                                            </select>
                                                        </div>
                                                        <div>
                                                            <label class="block text-slate-500 text-[11px] font-bold mb-1">Quận / Huyện: <span class="text-rose-500">*</span></label>
                                                            <select x-model="checkoutShippingForm.district" @change="onDistrictChange(); checkoutShippingForm.touched.district = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                                <template x-for="d in currentProvinceDistricts" :key="d.name">
                                                                    <option :value="d.name" x-text="d.name"></option>
                                                                </template>
                                                            </select>
                                                        </div>
                                                        <div>
                                                            <label class="block text-slate-500 text-[11px] font-bold mb-1">Phường / Xã: <span class="text-rose-500">*</span></label>
                                                            <select x-model="checkoutShippingForm.ward" @change="checkoutShippingForm.touched.ward = true" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-semibold focus:outline-none focus:bg-white">
                                                                <template x-for="w in currentDistrictWards" :key="w">
                                                                    <option :value="w" x-text="w"></option>
                                                                </template>
                                                            </select>
                                                        </div>
                                                    </div>
                                                </div>
                                            </template>
                                        </div>
                                    </div>

                                    <!-- Khối 2 - "Thông tin Lịch hẹn Dịch vụ" (Đã Mở Khóa Chỉnh Sửa & Form Đưa Đón PetShip) -->
                                    <div class="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm space-y-4">
                                        <div class="flex items-center justify-between pb-3 border-b border-slate-100">
                                            <div class="flex items-center gap-2.5">
                                                <span class="w-7 h-7 rounded-lg bg-blue-600 text-white font-black text-xs flex items-center justify-center shadow-sm">2</span>
                                                <h4 class="font-extrabold text-base text-slate-900">Thông tin Lịch hẹn Dịch vụ</h4>
                                            </div>
                                            <span class="text-xs text-emerald-700 font-bold bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200 flex items-center gap-1">
                                                <i class="fa-solid fa-pen-to-square text-[10px]"></i> Cho phép sửa
                                            </span>
                                        </div>

                                        <!-- Mở khóa Thông tin liên hệ (Editable Contact Info) -->
                                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm">
                                            <div class="space-y-1">
                                                <label class="text-slate-700 text-xs font-bold block">Tên người đại diện đặt lịch: <span class="text-rose-500">*</span></label>
                                                <input type="text" x-model="checkoutBookingContactName" @input="checkoutBookingContactTouched.name = true" placeholder="Nguyễn Phương Thảo" class="w-full bg-white border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:border-brand-500" :class="(checkoutBookingContactTouched.name && (!checkoutBookingContactName || checkoutBookingContactName.trim().length < 2)) ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                <p x-show="checkoutBookingContactTouched.name && (!checkoutBookingContactName || checkoutBookingContactName.trim().length < 2)" class="text-rose-500 text-[11px] font-semibold mt-0.5 flex items-center gap-1">
                                                    <i class="fa-solid fa-circle-exclamation"></i> Vui lòng nhập họ tên
                                                </p>
                                            </div>
                                            <div class="space-y-1">
                                                <label class="text-slate-700 text-xs font-bold block">Số điện thoại liên hệ: <span class="text-rose-500">*</span></label>
                                                <input type="tel" x-model="checkoutBookingContactPhone" @input="checkoutBookingContactTouched.phone = true" placeholder="0988 123 456" class="w-full bg-white border rounded-xl px-4 py-2.5 text-slate-800 font-semibold focus:outline-none focus:border-brand-500 font-mono" :class="(checkoutBookingContactTouched.phone && (!checkoutBookingContactPhone || !/^(0[35789])[0-9]{8}$/.test(checkoutBookingContactPhone.trim().replace(/\s/g,'')))) ? 'border-rose-400 bg-rose-50/20' : 'border-slate-300'">
                                                <p x-show="checkoutBookingContactTouched.phone && (!checkoutBookingContactPhone || !/^(0[35789])[0-9]{8}$/.test(checkoutBookingContactPhone.trim().replace(/\s/g,'')))" class="text-rose-500 text-[11px] font-semibold mt-0.5 flex items-center gap-1">
                                                    <i class="fa-solid fa-circle-exclamation"></i> SĐT không hợp lệ
                                                </p>
                                            </div>
                                        </div>

                                        <div class="space-y-1 text-xs sm:text-sm">
                                            <label class="text-slate-600 text-xs font-bold block">Cơ sở thực hiện:</label>
                                            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-slate-800 font-bold flex items-center gap-2">
                                                <i class="fa-solid fa-location-dot text-rose-500"></i>
                                                <span>Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Phường Đa Kao, Quận 1, TPHCM</span>
                                            </div>
                                        </div>

                                                                                <!-- Khối Phương thức đưa đón PetShip (Case 3: Giỏ hàng hỗn hợp Mixed Cart) -->
                                        <div class="space-y-3 text-xs sm:text-sm">
                                            <div class="flex items-center justify-between">
                                                <label class="text-slate-700 text-xs font-bold flex items-center gap-1.5">
                                                    <i class="fa-solid fa-truck-ramp-box text-orange-500"></i>
                                                    <span>Phương thức đưa đón PetShip:</span>
                                                </label>
                                                <div>
                                                    <template x-if="hasPetShip">
                                                        <span class="text-[10px] text-orange-700 font-extrabold bg-orange-100 px-2.5 py-0.5 rounded-full border border-orange-200 flex items-center gap-1">
                                                            <span class="w-1.5 h-1.5 rounded-full bg-orange-500 animate-pulse"></span>
                                                            Đã chọn dịch vụ PetShip tận nhà
                                                        </span>
                                                    </template>
                                                    <template x-if="!hasPetShip">
                                                        <span class="text-[10px] text-slate-600 font-bold bg-slate-200 px-2.5 py-0.5 rounded-full border border-slate-300">
                                                            Tự đưa đón tại cơ sở
                                                        </span>
                                                    </template>
                                                </div>
                                            </div>

                                            <!-- 2 tùy chọn trực quan -->
                                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                                                <!-- Tự đưa đón -->
                                                <div @click="setPetShipMode(false)"
                                                     class="p-3.5 rounded-2xl border-2 cursor-pointer transition flex items-start gap-3 select-none"
                                                     :class="!hasPetShip ? 'border-brand-500 bg-brand-50/30 shadow-sm' : 'border-slate-200 bg-white hover:border-slate-300'">
                                                    <input type="radio" name="petship_method_case3" :checked="!hasPetShip" class="mt-0.5 text-brand-600 focus:ring-brand-500 cursor-pointer">
                                                    <div>
                                                        <span class="font-extrabold text-xs text-slate-900 block flex items-center gap-1.5">
                                                            <i class="fa-solid fa-person-walking text-slate-500"></i>
                                                            <span>Tự đưa đón tại cơ sở</span>
                                                        </span>
                                                        <span class="text-[11px] text-slate-500 block mt-0.5 leading-snug">Khách mang bé đến 88 NTMK, Q1 (Miễn phí)</span>
                                                    </div>
                                                </div>

                                                <!-- Xe PetShip -->
                                                <div @click="setPetShipMode(true)"
                                                     class="p-3.5 rounded-2xl border-2 cursor-pointer transition flex items-start gap-3 select-none"
                                                     :class="hasPetShip ? 'border-orange-500 bg-orange-50/40 shadow-sm ring-2 ring-orange-500/20' : 'border-slate-200 bg-white hover:border-slate-300'">
                                                    <input type="radio" name="petship_method_case3" :checked="hasPetShip" class="mt-0.5 text-orange-600 focus:ring-orange-500 cursor-pointer">
                                                    <div>
                                                        <span class="font-extrabold text-xs text-slate-900 block flex items-center gap-1.5">
                                                            <i class="fa-solid fa-van-shuttle text-orange-600"></i>
                                                            <span>Xe đưa đón PetShip tận nhà</span>
                                                        </span>
                                                        <span class="text-[11px] text-orange-600 font-bold block mt-0.5 leading-snug">Đón & trả bé tận cửa (+60.000đ)</span>
                                                    </div>
                                                </div>
                                            </div>

                                            <!-- Form Nhập Địa Chỉ PetShip (Render khi hasPetShip === true) -->
                                            <template x-if="hasPetShip">
                                                <div class="p-4 sm:p-5 bg-gradient-to-br from-orange-50/70 to-amber-50/40 rounded-2xl border-2 border-orange-200 space-y-3.5 animate-fadeIn">
                                                    <div class="flex items-center justify-between pb-2 border-b border-orange-200/70">
                                                        <div class="flex items-center gap-2 text-orange-900 font-extrabold text-xs sm:text-sm">
                                                            <div class="w-6 h-6 rounded-lg bg-orange-500 text-white flex items-center justify-center text-xs shadow-xs">
                                                                <i class="fa-solid fa-location-dot"></i>
                                                            </div>
                                                            <span>Địa Chỉ Đón & Trả Thú Cưng (Khu vực TP.HCM)</span>
                                                        </div>
                                                        <span class="text-[11px] text-orange-700 font-bold bg-white px-2 py-0.5 rounded-full border border-orange-200 shadow-xs">
                                                            Tài xế chuyên dụng
                                                        </span>
                                                    </div>

                                                    <!-- TỐI ƯU UX CHO GIỎ HÀNG HỖN HỢP: Checkbox đồng bộ địa chỉ -->
                                                    <div class="p-3 bg-white/95 rounded-xl border border-orange-300 flex items-center justify-between shadow-xs">
                                                        <label class="flex items-center gap-2.5 cursor-pointer text-xs font-bold text-slate-800 select-none">
                                                            <input type="checkbox"
                                                                   x-model="syncWithShippingAddress"
                                                                   @change="onToggleSyncWithShippingAddress()"
                                                                   class="w-4 h-4 rounded text-orange-600 focus:ring-orange-500 border-slate-300 cursor-pointer">
                                                            <span>Sử dụng cùng địa chỉ nhận hàng phía trên</span>
                                                        </label>
                                                        <span class="text-[10px] text-orange-700 font-extrabold bg-orange-100 px-2 py-0.5 rounded-md flex items-center gap-1">
                                                            <i class="fa-solid fa-copy text-[10px]"></i> Tự động sao chép
                                                        </span>
                                                    </div>

                                                    <!-- Ô input: Địa chỉ cụ thể (Số nhà, tên đường) (Bắt buộc) -->
                                                    <div>
                                                        <label class="block text-slate-700 text-xs font-bold mb-1.5 flex items-center justify-between">
                                                            <span>Địa chỉ cụ thể (Số nhà, tên đường): <span class="text-rose-500">*</span></span>
                                                            <span class="text-[10px] text-slate-400 font-normal">Tối thiểu 5 ký tự</span>
                                                        </label>
                                                        <div class="relative">
                                                            <input type="text"
                                                                   x-model="petShipAddress.street"
                                                                   @input="petShipAddressTouched.street = true"
                                                                   @blur="petShipAddressTouched.street = true"
                                                                   placeholder="Ví dụ: 125 Hoàng Quốc Việt, Tòa A, Phòng 402..."
                                                                   class="w-full bg-white border rounded-xl pl-10 pr-4 py-2.5 text-slate-800 text-xs sm:text-sm font-semibold focus:outline-none transition"
                                                                   :class="(petShipAddressTouched.street && (!petShipAddress.street || petShipAddress.street.trim().length < 5))
                                                                           ? 'border-rose-400 bg-rose-50/20 focus:border-rose-500 focus:ring-2 focus:ring-rose-200'
                                                                           : 'border-slate-300 focus:border-orange-500 focus:ring-2 focus:ring-orange-200'">
                                                            <i class="fa-solid fa-house text-slate-400 absolute left-3.5 top-3.5 text-xs"></i>
                                                        </div>
                                                        <p x-show="petShipAddressTouched.street && (!petShipAddress.street || petShipAddress.street.trim().length < 5)"
                                                           class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1">
                                                            <i class="fa-solid fa-circle-exclamation"></i> Vui lòng nhập địa chỉ cụ thể (tối thiểu 5 ký tự)
                                                        </p>
                                                    </div>

                                                    <!-- Tái sử dụng component AddressSelector (Dropdown Tỉnh/Thành khóa cứng, dropdown Quận/Huyện, Phường/Xã) -->
                                                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                                                        <!-- Dropdown Tỉnh/Thành phố bị khóa cứng ở 'TP. Hồ Chí Minh' -->
                                                        <div>
                                                            <label class="block text-slate-700 text-[11px] font-bold mb-1">
                                                                Tỉnh / Thành phố: <span class="text-rose-500">*</span>
                                                            </label>
                                                            <div class="relative">
                                                                <select disabled class="w-full bg-slate-100 border border-slate-300 rounded-xl px-3 py-2 text-xs font-bold text-slate-600 cursor-not-allowed appearance-none">
                                                                    <option value="TP. Hồ Chí Minh" selected>TP. Hồ Chí Minh</option>
                                                                </select>
                                                                <i class="fa-solid fa-lock text-slate-400 absolute right-3 top-2.5 text-xs"></i>
                                                            </div>
                                                        </div>

                                                        <!-- Dropdown Quận / Huyện -->
                                                        <div>
                                                            <label class="block text-slate-700 text-[11px] font-bold mb-1">
                                                                Quận / Huyện: <span class="text-rose-500">*</span>
                                                            </label>
                                                            <div class="relative">
                                                                <select x-model="petShipAddress.district"
                                                                        @change="onPetShipDistrictChange()"
                                                                        @blur="petShipAddressTouched.district = true"
                                                                        class="w-full bg-white border rounded-xl pl-3 pr-8 py-2 text-xs font-semibold focus:outline-none transition appearance-none cursor-pointer"
                                                                        :class="(petShipAddressTouched.district && (!petShipAddress.district || !petShipAddress.district.trim()))
                                                                                ? 'border-rose-400 bg-rose-50/20 focus:border-rose-500'
                                                                                : 'border-slate-300 focus:border-orange-500'">
                                                                    <option value="">-- Chọn Quận/Huyện --</option>
                                                                    <template x-for="d in petShipDistricts" :key="d.name">
                                                                        <option :value="d.name" x-text="d.name" :selected="d.name === petShipAddress.district"></option>
                                                                    </template>
                                                                </select>
                                                                <i class="fa-solid fa-chevron-down text-slate-400 absolute right-3 top-2.5 text-[10px] pointer-events-none"></i>
                                                            </div>
                                                            <p x-show="petShipAddressTouched.district && (!petShipAddress.district || !petShipAddress.district.trim())"
                                                               class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1">
                                                                <i class="fa-solid fa-circle-exclamation"></i> Vui lòng chọn Quận/Huyện
                                                            </p>
                                                        </div>

                                                        <!-- Dropdown Phường / Xã -->
                                                        <div>
                                                            <label class="block text-slate-700 text-[11px] font-bold mb-1">
                                                                Phường / Xã: <span class="text-rose-500">*</span>
                                                            </label>
                                                            <div class="relative">
                                                                <select x-model="petShipAddress.ward"
                                                                        @change="petShipAddressTouched.ward = true"
                                                                        @blur="petShipAddressTouched.ward = true"
                                                                        :disabled="!petShipAddress.district"
                                                                        class="w-full bg-white border rounded-xl pl-3 pr-8 py-2 text-xs font-semibold focus:outline-none transition appearance-none cursor-pointer disabled:bg-slate-100 disabled:cursor-not-allowed"
                                                                        :class="(petShipAddressTouched.ward && (!petShipAddress.ward || !petShipAddress.ward.trim()))
                                                                                ? 'border-rose-400 bg-rose-50/20 focus:border-rose-500'
                                                                                : 'border-slate-300 focus:border-orange-500'">
                                                                    <option value="">-- Chọn Phường/Xã --</option>
                                                                    <template x-for="w in petShipWards" :key="w">
                                                                        <option :value="w" x-text="w" :selected="w === petShipAddress.ward"></option>
                                                                    </template>
                                                                </select>
                                                                <i class="fa-solid fa-chevron-down text-slate-400 absolute right-3 top-2.5 text-[10px] pointer-events-none"></i>
                                                            </div>
                                                            <p x-show="petShipAddressTouched.ward && (!petShipAddress.ward || !petShipAddress.ward.trim())"
                                                               class="text-rose-500 text-[11px] font-semibold mt-1 flex items-center gap-1">
                                                                <i class="fa-solid fa-circle-exclamation"></i> Vui lòng chọn Phường/Xã
                                                            </p>
                                                        </div>
                                                    </div>

                                                    <!-- Ghi chú vận chuyển -->
                                                    <div class="flex items-center gap-2 text-[11px] text-slate-500 bg-white/60 p-2.5 rounded-xl border border-orange-200/60">
                                                        <i class="fa-solid fa-circle-info text-orange-500 text-xs"></i>
                                                        <span>Tài xế PetCare360 sẽ gọi trước 15-30 phút trước khi đến đón thú cưng tại địa chỉ trên.</span>
                                                    </div>
                                                </div>
                                            </template>
                                        </div>
                                    
                                    </div>
                                </div>
                            </template>

                            <!-- Thanh nút điều hướng dưới chân cột trái -->
                            <div class="pt-2 flex justify-between items-center">
                                <button @click="goToCartStep(1)" class="text-slate-500 hover:text-slate-800 text-xs font-bold flex items-center gap-1.5 transition">
                                    <i class="fa-solid fa-arrow-left"></i>
                                    <span>Quay lại giỏ hàng</span>
                                </button>
                                <button type="button" @click="proceedToPaymentStep()" :disabled="!isStep2CheckoutValid" :class="!isStep2CheckoutValid ? 'opacity-50 cursor-not-allowed bg-slate-300 text-slate-500' : 'bg-orange-500 hover:bg-orange-600 text-white shadow-lg shadow-orange-500/25'" class="py-3.5 px-7 rounded-2xl font-extrabold text-xs sm:text-sm transition flex items-center gap-2">
                                    <span>Tiếp tục đến phương thức thanh toán</span>
                                    <i class="fa-solid fa-arrow-right text-xs"></i>
                                </button>
                            </div>
                        </div>

                        <!-- CỘT BÊN PHẢI: TÓM TẮT ĐƠN HÀNG, KHO VOUCHER & TOÁN THANH TOÁN (CHECKOUT MATH) -->
                        <div class="space-y-4">
                            <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                                <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                                    <h4 class="font-extrabold text-sm text-slate-800">Đơn hàng của bạn</h4>
                                    <span class="text-xs text-slate-400 font-bold" x-text="cart.length + ' mục'"></span>
                                </div>

                                <!-- Danh sách sản phẩm / dịch vụ trong giỏ -->
                                <div class="space-y-3 max-h-56 overflow-y-auto pr-1">
                                    <template x-for="(item, cidx) in cart" :key="cidx">
                                        <div class="flex items-center justify-between text-xs py-1 border-b border-slate-50">
                                            <div class="flex items-center gap-2.5">
                                                <img :src="item.image || item.img || getItemImage(item)" @error="$event.target.src='https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80'" class="w-10 h-10 rounded-lg object-cover border border-slate-100 flex-shrink-0">
                                                <div>
                                                    <p class="font-bold text-slate-800 line-clamp-1 max-w-[140px]" x-text="item.name"></p>
                                                    <div class="flex items-center gap-1.5 text-[11px] text-slate-400">
                                                        <span x-text="'SL: x' + (item.qty || item.quantity || 1)"></span>
                                                        <template x-if="item.isService">
                                                            <span class="px-1.5 py-0.2 bg-blue-50 text-blue-700 font-bold rounded text-[10px]">Dịch vụ</span>
                                                        </template>
                                                        <template x-if="!item.isService">
                                                            <span class="px-1.5 py-0.2 bg-orange-50 text-orange-700 font-bold rounded text-[10px]">Sản phẩm</span>
                                                        </template>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="text-right">
                                                <span class="font-extrabold text-slate-900" x-text="formatCurrency((item.price || item.totalCost || 0) * (item.qty || item.quantity || 1))"></span>
                                                <template x-if="isHotelItem(item)">
                                                    <span class="block text-[10px] text-orange-600 font-semibold italic">Cọc 50%</span>
                                                </template>
                                            </div>
                                        </div>
                                    </template>
                                </div>

                                <!-- KHỐI COMPONENT CHỌN MÃ KHUYẾN MÃI (TICKET STYLE COMPONENT - YÊU CẦU 3.1) -->
                                <div class="pt-2">
                                    <div @click="openVoucherWallet()" class="p-3.5 rounded-2xl border-2 border-dashed border-orange-300 bg-orange-50/50 hover:bg-orange-50 cursor-pointer transition flex items-center justify-between group">
                                        <div class="flex items-center gap-3">
                                            <div class="w-9 h-9 rounded-xl bg-orange-500 text-white flex items-center justify-center font-bold text-base shadow-sm group-hover:scale-105 transition">
                                                <i class="fa-solid fa-ticket"></i>
                                            </div>
                                            <div>
                                                <div class="text-xs font-extrabold text-slate-900 flex items-center gap-1.5">
                                                    <span>PetCare Voucher</span>
                                                    <span class="text-[9px] bg-orange-100 text-orange-800 font-bold px-1.5 py-0.5 rounded">Kho Voucher</span>
                                                </div>
                                                <template x-if="!hasAppliedVouchers">
                                                    <p class="text-[11px] text-slate-500 font-medium mt-0.5">Chọn hoặc nhập mã khuyến mãi</p>
                                                </template>
                                                <template x-if="hasAppliedVouchers">
                                                    <div class="flex flex-wrap gap-1 mt-1">
                                                        <template x-if="appliedVouchers.shipping">
                                                            <span class="inline-flex items-center gap-1 bg-blue-100 text-blue-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-blue-200">
                                                                <i class="fa-solid fa-truck-fast text-[9px]"></i>
                                                                <span x-text="appliedVouchers.shipping.code"></span>
                                                                <button type="button" @click.stop="removeVoucher('shipping')" class="text-blue-600 hover:text-blue-900 font-black ml-1 text-xs">&times;</button>
                                                            </span>
                                                        </template>
                                                        <template x-if="appliedVouchers.order">
                                                            <span class="inline-flex items-center gap-1 bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-emerald-200">
                                                                <i class="fa-solid fa-tag text-[9px]"></i>
                                                                <span x-text="appliedVouchers.order.code"></span>
                                                                <button type="button" @click.stop="removeVoucher('order')" class="text-emerald-600 hover:text-emerald-900 font-black ml-1 text-xs">&times;</button>
                                                            </span>
                                                        </template>
                                                    </div>
                                                </template>
                                            </div>
                                        </div>
                                        <div class="flex items-center gap-1 text-xs font-bold text-orange-600 group-hover:translate-x-1 transition">
                                            <span x-text="hasAppliedVouchers ? 'Đổi mã' : 'Chọn'"></span>
                                            <i class="fa-solid fa-chevron-right text-[10px]"></i>
                                        </div>
                                    </div>
                                </div>

                                <!-- BẢNG TÍNH TIỀN MINH BẠCH (CHECKOUT MATH - YÊU CẦU 1.4, 1.5, 3.4) -->
                                <div class="pt-3 border-t border-slate-100 space-y-2 text-xs">
                                    <!-- Dòng 1: Tạm tính -->
                                    <div class="flex justify-between text-slate-600">
                                        <span>Tạm tính (Hàng & Dịch vụ):</span>
                                        <span class="font-bold text-slate-800" x-text="formatCurrency(cartSubtotal)"></span>
                                    </div>

                                    <!-- Dòng 2: Phí vận chuyển (Chỉ tính khi hasProduct && deliveryMethod === 'door') -->
                                    <div class="flex justify-between text-slate-600">
                                        <span>Phí vận chuyển:</span>
                                        <template x-if="effectiveShippingFee > 0">
                                            <span class="font-bold text-slate-800" x-text="formatCurrency(effectiveShippingFee)"></span>
                                        </template>
                                        <template x-if="effectiveShippingFee === 0">
                                            <span class="font-bold text-emerald-600">Miễn phí</span>
                                        </template>
                                    </div>

                                    <!-- Dòng 3: Giảm giá (Voucher) -->
                                    <template x-if="totalDiscount > 0">
                                        <div class="flex justify-between text-emerald-600 font-extrabold">
                                            <span class="flex items-center gap-1">
                                                <i class="fa-solid fa-circle-check text-[10px]"></i>
                                                <span>Giảm giá Voucher:</span>
                                            </span>
                                            <span x-text="'-' + formatCurrency(totalDiscount)"></span>
                                        </div>
                                    </template>

                                    <!-- Dòng 4: Tổng giá trị đơn hàng (grandTotal - Màu đen/xám, font thường) -->
                                    <div class="flex justify-between text-slate-700 pt-1 border-t border-slate-100">
                                        <span>Tổng giá trị đơn hàng:</span>
                                        <span class="font-bold text-slate-900" x-text="formatCurrency(grandTotal)"></span>
                                    </div>

                                    <!-- Dòng 5: TỔNG THANH TOÁN HIỆN TẠI (currentPayment - Màu cam, in đậm, to nhất) -->
                                    <div class="pt-2 border-t border-dashed border-orange-200">
                                        <div class="flex justify-between items-baseline">
                                            <span class="text-xs font-bold text-slate-900 uppercase">TỔNG THANH TOÁN HIỆN TẠI:</span>
                                            <span class="text-xl font-black text-orange-600" x-text="formatCurrency(currentPayment)"></span>
                                        </div>
                                        <p class="text-[10px] text-slate-400 italic text-right mt-0.5">Số tiền thực tế thanh toán lúc này</p>
                                    </div>

                                    <!-- Dòng 6: Số tiền thu sau tại cơ sở (remainingBalance - Màu xám, in nghiêng, font nhỏ) -->
                                    <template x-if="hasHotel && remainingBalance > 0">
                                        <div class="flex justify-between text-[11px] text-slate-500 italic pt-1">
                                            <span>Số tiền thu sau tại cơ sở:</span>
                                            <span class="font-semibold" x-text="formatCurrency(remainingBalance)"></span>
                                        </div>
                                    </template>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- BƯỚC 3: PHƯƠNG THỨC THANH TOÁN (PAYMENT UI & ACCORDION) -->
                <div x-show="cartStep === 3" class="space-y-6">
                    <div class="py-3 border-b border-slate-200 flex items-center gap-2 text-xs sm:text-sm font-bold text-slate-500">
                        <span class="text-slate-400 hover:text-orange-600 cursor-pointer flex items-center gap-1" @click="goToCartStep(1)">
                            <i class="fa-solid fa-cart-shopping text-xs"></i>
                            <span>1. Giỏ hàng</span>
                        </span>
                        <i class="fa-solid fa-chevron-right text-[10px] text-slate-300"></i>
                        <span class="text-slate-400 hover:text-orange-600 cursor-pointer flex items-center gap-1" @click="goToCartStep(2)">
                            <i class="fa-solid fa-truck-ramp-box text-xs"></i>
                            <span>2. Thông tin nhận hàng & Lịch hẹn</span>
                        </span>
                        <i class="fa-solid fa-chevron-right text-[10px] text-slate-300"></i>
                        <span class="text-orange-600 font-extrabold flex items-center gap-1 bg-orange-50 px-2.5 py-1 rounded-lg">
                            <i class="fa-solid fa-credit-card text-xs"></i>
                            <span>3. Phương thức thanh toán</span>
                        </span>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        <!-- Cột trái: Accordion các phương thức thanh toán -->
                        <div class="lg:col-span-2 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                            
                            <!-- Thông tin tóm tắt phương thức vận chuyển -->
                            <div class="space-y-2">
                                <h4 class="font-extrabold text-sm text-slate-800 uppercase tracking-wider">Hình thức nhận hàng & Địa điểm</h4>
                                <div class="p-4 rounded-2xl border border-slate-200 bg-slate-50 flex items-center justify-between">
                                    <div class="flex items-center gap-2.5 text-xs sm:text-sm">
                                        <i class="fa-solid fa-truck-fast text-orange-600 text-base"></i>
                                        <div>
                                            <template x-if="hasProduct && deliveryMethod === 'door'">
                                                <span class="font-bold text-slate-800">Giao tận nơi: <span class="font-normal" x-text="checkoutShippingForm.address + ', ' + checkoutShippingForm.ward + ', ' + checkoutShippingForm.district + ', ' + checkoutShippingForm.city"></span></span>
                                            </template>
                                            <template x-if="hasProduct && deliveryMethod === 'store'">
                                                <span class="font-bold text-slate-800">Nhận tại shop: <span class="font-normal">88 Nguyễn Thị Minh Khai, Q1, TP.HCM</span></span>
                                            </template>
                                            <template x-if="!hasProduct && hasService">
                                                <span class="font-bold text-slate-800">Lịch hẹn dịch vụ: <span class="font-normal">88 Nguyễn Thị Minh Khai (PetShip: <span x-text="servicePetShipAddress || 'Khách tự đưa đón'"></span>)</span></span>
                                            </template>
                                        </div>
                                    </div>
                                    <span class="font-bold text-slate-900 text-xs sm:text-sm" x-text="effectiveShippingFee > 0 ? formatCurrency(effectiveShippingFee) : '0 đ'"></span>
                                </div>
                            </div>

                            <!-- ACCORDION PHƯƠNG THỨC THANH TOÁN (YÊU CẦU 2.2) -->
                            <div class="space-y-3">
                                <h4 class="font-extrabold text-sm text-slate-800 uppercase tracking-wider">Chọn phương thức thanh toán</h4>
                                
                                <!-- 1. Chuyển khoản VietQR MB Bank (Khuyên dùng - Dynamic VietQR) -->
                                <div class="rounded-2xl border transition overflow-hidden" :class="paymentMethod === 'vietqr' ? 'border-orange-500 bg-orange-50/20 shadow-sm' : 'border-slate-200'">
                                    <label class="p-4 cursor-pointer flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <input type="radio" value="vietqr" x-model="paymentMethod" class="text-orange-500">
                                            <div>
                                                <div class="flex items-center gap-2">
                                                    <span class="font-extrabold text-xs sm:text-sm text-slate-900">Chuyển khoản VietQR (MB Bank)</span>
                                                    <span class="px-2 py-0.5 bg-emerald-100 text-emerald-800 font-bold text-[10px] rounded-full">Xác thực tự động</span>
                                                </div>
                                                <span class="text-slate-400 text-[11px] block mt-0.5">Tự động điền số tiền & cú pháp chuyển khoản bằng Dynamic QR</span>
                                            </div>
                                        </div>
                                        <i class="fa-solid fa-qrcode text-orange-600 text-lg"></i>
                                    </label>

                                    <!-- Chi tiết VietQR Accordion khi chọn -->
                                    <template x-if="paymentMethod === 'vietqr'">
                                        <div class="p-4 sm:p-5 bg-white border-t border-orange-200 space-y-4">
                                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
                                                <!-- Mã QR động (VietQR API) -->
                                                <div class="text-center p-3 bg-slate-50 rounded-2xl border border-slate-200 space-y-2">
                                                    <img :src="vietQrUrl" alt="VietQR PetCare360" class="w-48 h-48 mx-auto rounded-xl border-2 border-orange-200 shadow p-1 bg-white object-contain">
                                                    <p class="text-[11px] text-slate-500 font-medium">Quét bằng ứng dụng của bất kỳ ngân hàng nào</p>
                                                </div>

                                                <!-- Thông tin tài khoản -->
                                                <div class="space-y-2.5 text-xs text-slate-700">
                                                    <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-100">
                                                        <span class="text-slate-400 text-[11px] block">Ngân hàng thụ hưởng:</span>
                                                        <strong class="text-slate-900 text-sm">MB Bank (Quân Đội)</strong>
                                                    </div>
                                                    <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                                                        <div>
                                                            <span class="text-slate-400 text-[11px] block">Số tài khoản:</span>
                                                            <strong class="text-slate-900 text-sm font-mono tracking-wider">8888 9999 6666</strong>
                                                        </div>
                                                        <button type="button" @click="navigator.clipboard.writeText('888899996666'); alert('Đã sao chép STK: 888899996666');" class="px-2.5 py-1 bg-slate-200 hover:bg-slate-300 rounded-lg text-[10px] font-bold text-slate-700 transition">Sao chép</button>
                                                    </div>
                                                    <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-100">
                                                        <span class="text-slate-400 text-[11px] block">Chủ tài khoản:</span>
                                                        <strong class="text-slate-900 font-semibold">CT CP PETCARE360 VIETNAM</strong>
                                                    </div>
                                                    <div class="p-2.5 bg-orange-50 rounded-xl border border-orange-200 flex items-center justify-between">
                                                        <div>
                                                            <span class="text-orange-700 text-[11px] block font-bold">Số tiền chuyển:</span>
                                                            <strong class="text-orange-600 text-base font-black" x-text="formatCurrency(currentPayment)"></strong>
                                                        </div>
                                                        <div class="text-right">
                                                            <span class="text-slate-500 text-[11px] block">Nội dung:</span>
                                                            <strong class="font-mono text-slate-900 bg-white px-2 py-0.5 rounded border border-slate-200" x-text="'PETCARE360 ' + (completedOrderNumber ? completedOrderNumber.replace('#','') : 'DH157817')"></strong>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </template>
                                </div>

                                <!-- 2. Ví điện tử MoMo / ZaloPay (Có Accordion UI mở rộng mã QR MoMo tương tự VietQR) -->
                                <div class="rounded-2xl border transition overflow-hidden" :class="(paymentMethod === 'ewallet' || paymentMethod === 'momo') ? 'border-orange-500 bg-orange-50/20 shadow-sm' : 'border-slate-200'">
                                    <label class="p-4 cursor-pointer flex items-center justify-between">
                                        <div class="flex items-center gap-3">
                                            <input type="radio" value="momo" x-model="paymentMethod" @change="selectedPaymentMethod = 'momo'" class="text-orange-500">
                                            <div>
                                                <span class="font-extrabold text-xs sm:text-sm text-slate-900 block">Ví điện tử MoMo / ZaloPay</span>
                                                <span class="text-slate-400 text-[11px]">Quét mã QR thanh toán tức thì qua ứng dụng MoMo hoặc ZaloPay</span>
                                            </div>
                                        </div>
                                        <div class="flex items-center gap-2">
                                            <span class="px-2 py-0.5 bg-pink-100 text-pink-700 font-black text-[10px] rounded-md">MoMo</span>
                                            <span class="px-2 py-0.5 bg-blue-100 text-blue-700 font-black text-[10px] rounded-md">ZaloPay</span>
                                        </div>
                                    </label>

                                    <!-- Khung thanh toán MoMo Accordion mở rộng -->
                                    <template x-if="paymentMethod === 'ewallet' || paymentMethod === 'momo'">
                                        <div class="p-4 sm:p-5 bg-white border-t border-orange-200 space-y-4 animate-fadeIn">
                                            <div class="flex flex-col md:flex-row items-center gap-6">
                                                <!-- Ảnh QR MoMo -->
                                                <div class="flex flex-col items-center">
                                                    <div class="p-3 bg-pink-50/60 rounded-2xl border border-pink-200 shadow-sm text-center">
                                                        <img :src="momoQrImage" alt="QR MoMo Payment" class="w-48 h-auto rounded-xl object-contain shadow-sm border border-slate-100">
                                                        <div class="mt-2 text-center">
                                                            <span class="text-xs font-black text-slate-900 block">PHAM HOANG HUONG GIANG</span>
                                                            <span class="text-[11px] text-slate-500 font-mono">*******199</span>
                                                        </div>
                                                    </div>
                                                </div>

                                                <!-- Thông tin thanh toán MoMo -->
                                                <div class="flex-1 w-full space-y-3 text-xs sm:text-sm">
                                                    <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                                                        <h5 class="font-bold text-slate-800 text-sm flex items-center gap-2">
                                                            <i class="fa-solid fa-qrcode text-pink-600"></i>
                                                            <span>Mã QR Thanh Toán Tự Động (MoMo/ZaloPay)</span>
                                                        </h5>
                                                        <span class="text-[10px] font-bold bg-emerald-50 text-emerald-600 px-2 py-0.5 rounded-full border border-emerald-200 flex items-center gap-1">
                                                            <i class="fa-solid fa-circle-check text-[9px]"></i> Miễn phí giao dịch
                                                        </span>
                                                    </div>

                                                    <div class="space-y-2">
                                                        <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                                                            <div>
                                                                <span class="text-slate-400 text-[11px] block">Người thụ hưởng:</span>
                                                                <strong class="text-slate-900 font-bold">PHAM HOANG HUONG GIANG</strong>
                                                            </div>
                                                            <span class="font-mono text-xs text-slate-600 bg-white px-2 py-1 rounded border border-slate-200">*******199</span>
                                                        </div>

                                                        <div class="p-3 bg-orange-50 rounded-xl border border-orange-200 flex items-center justify-between">
                                                            <div>
                                                                <span class="text-orange-700 text-[11px] block font-bold">Số tiền cần thanh toán:</span>
                                                                <strong class="text-orange-600 text-lg font-black" x-text="formatCurrency(currentPayment)"></strong>
                                                            </div>
                                                            <div class="text-right">
                                                                <span class="text-slate-500 text-[11px] block">Lời nhắn/Nội dung:</span>
                                                                <strong class="font-mono text-slate-900 bg-white px-2.5 py-1 rounded border border-slate-200 text-xs font-bold" x-text="'PETCARE360 ' + (completedOrderNumber ? completedOrderNumber.replace('#','') : 'DH157817')"></strong>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div class="p-3 bg-pink-50/60 rounded-xl border border-pink-100 flex items-center gap-2.5 text-xs text-pink-900">
                                                        <i class="fa-solid fa-mobile-screen-button text-base text-pink-600 flex-shrink-0"></i>
                                                        <span>Mở ứng dụng <strong>MoMo</strong> hoặc <strong>ZaloPay</strong> để quét mã, giao dịch được xác nhận tức thì.</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </template>
                                </div>

                                <!-- 5. COD (Chỉ dành cho sản phẩm vật lý) -->
                                <div class="rounded-2xl border transition overflow-hidden" :class="hasService ? 'opacity-50 bg-slate-50 border-slate-200 cursor-not-allowed' : (paymentMethod === 'cod' ? 'border-orange-500 bg-orange-50/20' : 'border-slate-200')">
                                    <label class="p-4 flex items-center justify-between" :class="hasService ? 'cursor-not-allowed' : 'cursor-pointer'">
                                        <div class="flex items-center gap-3">
                                            <input type="radio" value="cod" x-model="paymentMethod" :disabled="hasService" class="text-orange-500">
                                            <div>
                                                <div class="flex items-center gap-2">
                                                    <span class="font-extrabold text-xs sm:text-sm text-slate-900">Thanh toán khi nhận hàng (COD)</span>
                                                    <template x-if="hasService">
                                                        <span class="px-2 py-0.5 bg-slate-200 text-slate-600 font-bold text-[10px] rounded-md">Không khả dụng</span>
                                                    </template>
                                                </div>
                                                <template x-if="hasService">
                                                    <span class="text-rose-500 text-[11px] block mt-0.5 font-medium">Chỉ áp dụng cho đơn 100% sản phẩm vật lý. Dịch vụ cần thanh toán hoặc đặt cọc online.</span>
                                                </template>
                                                <template x-if="!hasService">
                                                    <span class="text-slate-400 text-[11px] block mt-0.5">Kiểm tra hàng trước khi thanh toán tiền mặt</span>
                                                </template>
                                            </div>
                                        </div>
                                        <i class="fa-solid fa-hand-holding-dollar text-slate-400 text-lg"></i>
                                    </label>
                                </div>
                            </div>

                            <div class="pt-4 flex justify-between items-center">
                                <button @click="goToCartStep(2)" class="text-slate-500 hover:text-slate-800 text-xs font-bold flex items-center gap-1.5 transition">
                                    <i class="fa-solid fa-arrow-left"></i>
                                    <span>Quay lại thông tin giao hàng</span>
                                </button>
                                <!-- NÚT HOÀN TẤT ĐƠN HÀNG (SUBMIT CHECKOUT) -->
                                <button @click="finalizeOrder()" class="py-4 px-9 rounded-2xl bg-orange-500 hover:bg-orange-600 text-white font-black text-sm sm:text-base transition shadow-xl shadow-orange-500/30 flex items-center gap-2.5">
                                    <span>Hoàn tất đơn hàng</span>
                                    <i class="fa-solid fa-check"></i>
                                </button>
                            </div>
                        </div>

                        <!-- Cột phải: Tóm tắt thanh toán -->
                        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                            <h4 class="font-extrabold text-sm text-slate-800 pb-2 border-b border-slate-100">Tóm tắt thanh toán</h4>
                            <div class="space-y-2 text-xs text-slate-600">
                                <div class="flex justify-between">
                                    <span>Tạm tính (Hàng & Dịch vụ):</span>
                                    <span class="font-bold text-slate-800" x-text="formatCurrency(cartSubtotal)"></span>
                                </div>
                                <div class="flex justify-between">
                                    <span>Phí vận chuyển:</span>
                                    <span class="font-bold text-slate-800" x-text="effectiveShippingFee > 0 ? formatCurrency(effectiveShippingFee) : '0 đ'"></span>
                                </div>
                                <template x-if="totalDiscount > 0">
                                    <div class="flex justify-between text-emerald-600 font-extrabold">
                                        <span>Giảm giá:</span>
                                        <span x-text="'-' + formatCurrency(totalDiscount)"></span>
                                    </div>
                                </template>
                                <div class="flex justify-between text-slate-700 pt-1 border-t border-slate-100">
                                    <span>Tổng giá trị đơn:</span>
                                    <span class="font-bold text-slate-900" x-text="formatCurrency(grandTotal)"></span>
                                </div>
                                <div class="pt-2 border-t border-dashed border-orange-200">
                                    <div class="flex justify-between items-baseline">
                                        <span class="text-xs font-bold text-slate-900 uppercase">TỔNG THANH TOÁN HIỆN TẠI:</span>
                                        <span class="text-xl font-black text-orange-600" x-text="formatCurrency(currentPayment)"></span>
                                    </div>
                                    <p class="text-[10px] text-slate-400 italic text-right mt-0.5">Số tiền thanh toán ngay lúc này</p>
                                </div>
                                <template x-if="hasHotel && remainingBalance > 0">
                                    <div class="flex justify-between text-[11px] text-slate-500 italic pt-1">
                                        <span>Số tiền thu sau tại cơ sở:</span>
                                        <span class="font-semibold" x-text="formatCurrency(remainingBalance)"></span>
                                    </div>
                                </template>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- BƯỚC 4: XÁC NHẬN ĐƠN HÀNG, GIỮ KHO 15 PHÚT, WEBHOOK & TẢI BIÊN LAI (YÊU CẦU 2.3) -->
                <div x-show="cartStep === 4" class="max-w-3xl mx-auto bg-white rounded-3xl p-6 sm:p-10 border border-slate-200 shadow-sm space-y-6 text-center animate-fadeIn">
                    
                    <!-- Icon trạng thái -->
                    <template x-if="!webhookSuccessReceived">
                        <div class="w-16 h-16 rounded-full bg-amber-100 text-amber-600 flex items-center justify-center text-3xl mx-auto shadow-md">
                            <i class="fa-solid fa-clock"></i>
                        </div>
                    </template>
                    <template x-if="webhookSuccessReceived">
                        <div class="w-16 h-16 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-3xl mx-auto shadow-md">
                            <i class="fa-solid fa-check"></i>
                        </div>
                    </template>

                    <div>
                        <h2 class="text-2xl sm:text-3xl font-black text-slate-900" x-text="webhookSuccessReceived ? 'Thanh toán thành công!' : 'Đặt hàng & Giữ chỗ thành công!'"></h2>
                        <p class="text-sm text-slate-500 mt-1">Cảm ơn bạn đã tin tưởng dịch vụ và sản phẩm của PetCare360!</p>
                        <span class="inline-block mt-2 font-mono font-extrabold text-brand-700 bg-brand-50 px-4 py-1.5 rounded-full text-sm border border-brand-200" x-text="'Mã đơn hàng: ' + (currentPendingOrder ? currentPendingOrder.orderCode : completedOrderNumber)"></span>
                    </div>

                    <!-- BANNER COUNTDOWN TIMER GIỮ KHO 15 PHÚT -->
                    <template x-if="!webhookSuccessReceived">
                        <div class="p-4 bg-amber-50 rounded-2xl border border-amber-200 text-center space-y-2">
                            <div class="flex items-center justify-center gap-2 text-amber-800 font-extrabold text-sm">
                                <i class="fa-solid fa-hourglass-half text-amber-600 animate-spin"></i>
                                <span>TỒN KHO ĐƯỢC GIỮ TẠM TRONG:</span>
                                <span class="text-xl font-mono font-black text-orange-600" x-text="formattedCountdown"></span>
                            </div>
                            <p class="text-xs text-amber-700 max-w-lg mx-auto">Vui lòng hoàn tất chuyển khoản trong vòng 15 phút để hệ thống Gateway xác thực Webhook và trừ kho vĩnh viễn.</p>
                        </div>
                    </template>

                    <!-- BANNER WEBHOOK THÀNH CÔNG -->
                    <template x-if="webhookSuccessReceived">
                        <div class="p-4 bg-emerald-50 rounded-2xl border border-emerald-200 text-center space-y-1">
                            <div class="flex items-center justify-center gap-2 text-emerald-800 font-extrabold text-sm">
                                <i class="fa-solid fa-circle-check text-emerald-600 text-base"></i>
                                <span>XÁC THỰC THANH TOÁN WEBHOOK THÀNH CÔNG!</span>
                            </div>
                            <p class="text-xs text-emerald-700">Đơn hàng đã được xác nhận, kho hàng đã trừ vĩnh viễn. Nhân viên PetCare360 sẽ sớm liên hệ phục vụ quý khách.</p>
                        </div>
                    </template>

                    <!-- KHỐI CHUYỂN KHOẢN VIETQR ĐỘNG -->
                    <div class="p-5 bg-slate-50 rounded-2xl border border-slate-200 text-left text-xs space-y-3">
                        <h4 class="font-extrabold text-slate-800 uppercase tracking-wider text-xs flex items-center justify-between">
                            <span>Thông tin đơn hàng & Chuyển khoản</span>
                            <span class="font-bold text-orange-600" x-text="currentPendingOrder ? currentPendingOrder.statusText : 'Chờ thanh toán'"></span>
                        </h4>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-1 items-center">
                            <!-- VietQR Code -->
                            <div class="p-3 bg-white rounded-xl border border-slate-200 text-center space-y-1.5 shadow-sm">
                                <img :src="vietQrUrl" class="w-40 h-40 mx-auto rounded-lg border border-orange-100 p-0.5 object-contain">
                                <p class="text-[11px] text-slate-500 font-medium">Mã VietQR động tự động điền STK & Số tiền</p>
                            </div>

                            <!-- Chi tiết đơn -->
                            <div class="space-y-1.5 text-xs text-slate-700">
                                <p>• Người nhận: <strong class="text-slate-900" x-text="checkoutShippingForm.name"></strong> - SĐT: <strong class="text-slate-900 font-mono" x-text="checkoutShippingForm.phone"></strong></p>
                                <p>• Địa chỉ: <strong class="text-slate-800" x-text="checkoutShippingForm.address ? (checkoutShippingForm.address + ', ' + checkoutShippingForm.ward + ', ' + checkoutShippingForm.district + ', ' + checkoutShippingForm.city) : 'Cơ sở Chính 88 NTMK'"></strong></p>
                                <p>• Ngân hàng: <strong>MB Bank (8888 9999 6666 - CT CP PETCARE360 VIETNAM)</strong></p>
                                <p>• Cú pháp CK: <strong class="font-mono bg-white px-2 py-0.5 rounded border text-slate-900" x-text="'PETCARE360 ' + (currentPendingOrder ? currentPendingOrder.orderCode.replace('#','') : 'DH157817')"></strong></p>
                                <p class="pt-1">• Số tiền thanh toán ngay: <strong class="text-orange-600 text-base font-black" x-text="formatCurrency(currentPendingOrder ? currentPendingOrder.amount_paid : currentPayment)"></strong></p>
                                <template x-if="currentPendingOrder && currentPendingOrder.balance_due > 0">
                                    <p class="text-[11px] text-slate-500 italic">• Số tiền thu sau tại cơ sở: <strong class="text-slate-700 font-bold" x-text="formatCurrency(currentPendingOrder.balance_due)"></strong></p>
                                </template>
                            </div>
                        </div>

                        <!-- KHỐI GIẢ LẬP WEBHOOK & TẢI BIÊN LAI THỦ CÔNG (YÊU CẦU 2.3) -->
                        <div class="pt-3 border-t border-slate-200 space-y-2">
                            <div class="flex flex-col sm:flex-row gap-2.5 items-center justify-between">
                                <!-- Nút Giả Lập Webhook -->
                                <button type="button" @click="simulatePaymentWebhook()" class="w-full sm:w-auto px-4 py-2.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-extrabold text-xs rounded-xl shadow transition flex items-center justify-center gap-1.5">
                                    <i class="fa-solid fa-bolt"></i>
                                    <span>⚡ Giả lập Webhook: Thanh toán thành công (Test Gateway)</span>
                                </button>

                                <!-- Nút Tải Biên Lai / Duyệt Thủ Công -->
                                <div class="flex items-center gap-2 w-full sm:w-auto">
                                    <label class="cursor-pointer px-3.5 py-2.5 bg-slate-200 hover:bg-slate-300 text-slate-700 font-bold text-xs rounded-xl transition flex items-center gap-1.5 flex-1 sm:flex-initial justify-center">
                                        <i class="fa-solid fa-upload"></i>
                                        <span>Tải biên lai</span>
                                        <input type="file" accept="image/*" @change="handleReceiptUpload($event)" class="hidden">
                                    </label>
                                    <button type="button" @click="adminManualApprove()" class="px-3.5 py-2.5 bg-amber-500 hover:bg-amber-600 text-white font-bold text-xs rounded-xl transition flex-1 sm:flex-initial">
                                        Admin duyệt tay
                                    </button>
                                </div>
                            </div>
                            <template x-if="uploadedReceiptUrl">
                                <div class="p-2.5 bg-white rounded-xl border border-slate-200 flex items-center gap-3">
                                    <img :src="uploadedReceiptUrl" class="w-12 h-12 object-cover rounded-lg border">
                                    <div>
                                        <p class="text-xs font-bold text-slate-800">Đã đính kèm ảnh biên lai giao dịch</p>
                                        <span class="text-[10px] text-slate-400">Admin có thể kiểm tra và duyệt trừ kho ngay</span>
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>

                    <div class="pt-2 text-xs text-slate-500">
                        Cần hỗ trợ đơn hàng? Hotline CSKH 24/7: <strong class="text-orange-600">1900 6888 (Phím 1)</strong>
                    </div>

                    <div class="pt-4 flex justify-center gap-3">
                        <button @click="activeCustomerTab = 'shop'; cartStep = 1;" class="px-6 py-3 rounded-2xl bg-orange-500 hover:bg-orange-600 text-white font-extrabold text-xs sm:text-sm transition shadow-lg shadow-orange-500/20">
                            Tiếp tục mua sắm
                        </button>
                        <button @click="activeCustomerTab = 'orders'; cartStep = 1;" class="px-6 py-3 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs sm:text-sm transition">
                            Xem lịch sử đơn hàng
                        </button>
                    </div>
                </div>

                <!-- BƯỚC 5: QUẢN LÝ ĐƠN HÀNG SAU KHI ĐẶT (LỊCH SỬ ĐƠN HÀNG TRONG TÀI KHOẢN) -->
                <div x-show="cartStep === 5" class="space-y-6">
                    <div class="flex items-center justify-between pb-3 border-b border-slate-200">
                        <h2 class="text-2xl font-black text-slate-900">Tài Khoản Của Bạn</h2>
                        <button @click="goToCartStep(1)" class="text-xs text-brand-600 font-bold hover:underline">Quay lại giỏ hàng</button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                        <!-- Menu bên trái (Sidebar) -->
                        <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-2 text-xs font-semibold">
                            <button @click="activeCustomerTab = 'account'" class="w-full py-2.5 px-3 rounded-xl bg-brand-50 text-brand-700 text-left">Thông tin tài khoản</button>
                            <button @click="activeCustomerTab = 'account'" class="w-full py-2.5 px-3 rounded-xl text-slate-600 hover:bg-slate-50 text-left">Danh sách địa chỉ</button>
                            <button @click="logout()" class="w-full py-2.5 px-3 rounded-xl text-rose-600 hover:bg-rose-50 text-left">Đăng xuất</button>
                        </div>

                        <!-- Khung "DANH SÁCH ĐƠN HÀNG MỚI NHẤT" -->
                        <div class="md:col-span-3 bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                            <h3 class="font-extrabold text-base text-slate-900">DANH SÁCH ĐƠN HÀNG MỚI NHẤT</h3>
                            <div class="overflow-x-auto">
                                <table class="w-full text-left text-xs border-collapse">
                                    <thead>
                                        <tr class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                                            <th class="py-3 px-3">Mã đơn hàng</th>
                                            <th class="py-3 px-3">Ngày đặt</th>
                                            <th class="py-3 px-3">Thành tiền</th>
                                            <th class="py-3 px-3">Trạng thái thanh toán</th>
                                            <th class="py-3 px-3">Vận chuyển</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100">
                                        <template x-for="ord in customerOrdersEnhanced" :key="ord.id">
                                            <tr class="hover:bg-slate-50">
                                                <td class="py-3 px-3 font-bold text-brand-600 cursor-pointer hover:underline" @click="openOrderCheckoutSummary(ord)" x-text="ord.orderCode"></td>
                                                <td class="py-3 px-3 text-slate-500" x-text="ord.date"></td>
                                                <td class="py-3 px-3 font-bold text-orange-600" x-text="formatCurrency(ord.total)"></td>
                                                <td class="py-3 px-3">
                                                    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 text-amber-800" x-text="ord.paymentStatus"></span>
                                                </td>
                                                <td class="py-3 px-3">
                                                    <span :class="ord.badgeColor" class="px-2 py-0.5 rounded-full text-[10px] font-bold border" x-text="ord.statusText"></span>
                                                </td>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </main>

        <!-- Footer Chung -->
        <footer class="bg-slate-900 text-white pt-14 pb-10 border-t border-slate-800 mt-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <!-- Chân trang 4 cột bằng nhau -->
                <div class="grid grid-cols-1 md:grid-cols-4 gap-8 lg:gap-12">
                    
                    <!-- Cột 1 (Thông tin chung) -->
                    <div class="space-y-4">
                        <div class="flex items-center gap-2.5">
                            <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-[#F97316] to-amber-500 flex items-center justify-center text-white shadow-md">
                                <i class="fa-solid fa-paw text-lg"></i>
                            </div>
                            <span class="text-xl font-black text-white">PetCare<span class="text-[#F97316]">360</span></span>
                        </div>
                        <p class="text-xs text-slate-300 leading-relaxed">
                            PetCare360 - Điểm tựa yêu thương & hệ sinh thái dinh dưỡng trọn đời cho thú cưng. Cam kết chuẩn mực, tận tâm như người thân trong gia đình.
                        </p>
                        <div class="pt-2 text-xs text-slate-400 space-y-2">
                            <p class="flex items-start gap-2">
                                <i class="fa-solid fa-phone text-[#F97316] mt-0.5"></i>
                                <span><strong>Hotline:</strong> 1900 6888 Phím 1</span>
                            </p>
                            <p class="flex items-start gap-2">
                                <i class="fa-solid fa-envelope text-[#F97316] mt-0.5"></i>
                                <span><strong>Email:</strong> cskh@petcare360.vn</span>
                            </p>
                            <p class="flex items-start gap-2">
                                <i class="fa-solid fa-location-dot text-[#F97316] mt-0.5"></i>
                                <span><strong>Trụ sở:</strong> 123 Nguyễn Thị Minh Khai, P.6, Q.3, TP.HCM</span>
                            </p>
                        </div>
                    </div>

                    <!-- Cột 2 (Dịch Vụ Nổi Bật) -->
                    <div class="space-y-4">
                        <h4 class="font-extrabold text-sm text-white uppercase tracking-wider border-b border-slate-800 pb-2">Dịch Vụ Nổi Bật</h4>
                        <ul class="space-y-2.5 text-xs text-slate-300">
                            <li>
                                <a href="#" @click.prevent="activeCustomerTab = 'booking'; servicePricingTab = 'grooming';" class="hover:text-[#F97316] transition flex items-center gap-2">
                                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>Grooming & Spa Thú Cưng
                                </a>
                            </li>
                            <li>
                                <a href="#" @click.prevent="activeCustomerTab = 'booking'; servicePricingTab = 'hotel';" class="hover:text-[#F97316] transition flex items-center gap-2">
                                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>Khách Sạn Thú Cưng 5 Sao
                                </a>
                            </li>
                            <li>
                                <a href="#" @click.prevent="activeCustomerTab = 'shop';" class="hover:text-[#F97316] transition flex items-center gap-2">
                                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>Sản Phẩm & Dinh Dưỡng
                                </a>
                            </li>
                        </ul>
                    </div>

                    <!-- Cột 3 (Chính Sách & Pháp Lý) -->
                    <div class="space-y-4">
                        <h4 class="font-extrabold text-sm text-white uppercase tracking-wider border-b border-slate-800 pb-2">Chính Sách & Pháp Lý</h4>
                        <ul class="space-y-2.5 text-xs text-slate-300">
                            <li><button @click="openPolicyModal('privacy')" class="hover:text-[#F97316] transition flex items-center gap-2 text-left"><i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>Chính sách Bảo mật</button></li>
                            <li><button @click="openPolicyModal('terms')" class="hover:text-[#F97316] transition flex items-center gap-2 text-left"><i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>Điều khoản Dịch vụ</button></li>
                            <li><button @click="openPolicyModal('cookie')" class="hover:text-[#F97316] transition flex items-center gap-2 text-left"><i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>Chính sách Cookie</button></li>
                            <li><button @click="openPolicyModal('community')" class="hover:text-[#F97316] transition flex items-center gap-2 text-left"><i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>Nguyên tắc cộng đồng</button></li>
                            <li><button @click="openPolicyModal('refund')" class="hover:text-[#F97316] transition flex items-center gap-2 text-left"><i class="fa-solid fa-chevron-right text-[10px] text-slate-500"></i>Chính sách hoàn tiền</button></li>
                        </ul>
                    </div>

                    <!-- Cột 4 (Thanh Toán & Bản Quyền) -->
                    <div class="space-y-4">
                        <h4 class="font-extrabold text-sm text-white uppercase tracking-wider border-b border-slate-800 pb-2">Thanh Toán An Toàn</h4>
                        <p class="text-xs text-slate-400">Đa dạng hình thức thanh toán an toàn chuẩn SSL:</p>
                        <div class="grid grid-cols-3 gap-2.5">
                            <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700/80 flex flex-col items-center justify-center gap-1.5 hover:border-emerald-500 transition group" title="Tiền mặt khi nhận hàng (COD)">
                                <i class="fa-solid fa-money-bill-wave text-emerald-400 text-lg group-hover:scale-110 transition"></i>
                                <span class="text-[10px] text-slate-300 font-semibold">Tiền mặt</span>
                            </div>
                            <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700/80 flex flex-col items-center justify-center gap-1.5 hover:border-sky-500 transition group" title="Thẻ ngân hàng VietQR / ATM">
                                <i class="fa-solid fa-building-columns text-sky-400 text-lg group-hover:scale-110 transition"></i>
                                <span class="text-[10px] text-slate-300 font-semibold">Thẻ NH</span>
                            </div>
                            <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700/80 flex flex-col items-center justify-center gap-1.5 hover:border-pink-500 transition group" title="Ví điện tử MoMo">
                                <i class="fa-solid fa-wallet text-pink-400 text-lg group-hover:scale-110 transition"></i>
                                <span class="text-[10px] text-slate-300 font-semibold">Ví điện tử</span>
                            </div>
                        </div>
                        <div class="pt-4 border-t border-slate-800/80">
                            <p class="text-[11px] text-slate-400 leading-relaxed">
                                © 2026 PetCare360 Corporation.<br>All rights reserved.
                            </p>
                        </div>
                    </div>

                </div>
            </div>
        </footer>

        
        <!-- Quick Switcher to Admin View -->
        <div class="fixed bottom-20 md:bottom-6 right-6 z-40">
            <button @click="switchToAdmin()" class="px-4 py-2.5 rounded-2xl bg-slate-900/90 hover:bg-slate-900 text-white text-xs font-black shadow-xl backdrop-blur border border-slate-700 flex items-center gap-2 group transform hover:scale-105 transition-all">
                <div class="w-6 h-6 rounded-lg bg-sky-500/20 text-sky-400 flex items-center justify-center">
                    <i class="fa-solid fa-chart-pie text-xs"></i>
                </div>
                <span>Giao diện Admin</span>
                <span class="text-[9px] bg-sky-500 text-white px-1.5 py-0.5 rounded-full uppercase font-bold">9 Tabs</span>
            </button>
        </div>

        <!-- Mobile Bottom Navigation Bar Customer -->
        <div class="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 z-30 px-2 py-1.5 flex justify-around items-center text-[10px]">
            <button @click="activeCustomerTab = 'home'" :class="activeCustomerTab === 'home' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-house text-base mb-0.5"></i>
                <span>Trang chủ</span>
            </button>
            <button @click="activeCustomerTab = 'shop'" :class="activeCustomerTab === 'shop' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-box-open text-base mb-0.5"></i>
                <span>Sản phẩm</span>
            </button>
            <button @click="activeCustomerTab = 'booking'" :class="activeCustomerTab === 'booking' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-scissors text-base mb-0.5"></i>
                <span>Dịch vụ</span>
            </button>
            <button @click="activeCustomerTab = 'petshare'" :class="activeCustomerTab === 'petshare' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-newspaper text-base mb-0.5"></i>
                <span>PetShare</span>
            </button>
            <button @click="activeCustomerTab = 'petshow'" :class="activeCustomerTab === 'petshow' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                <i class="fa-solid fa-video text-base mb-0.5 text-rose-500"></i>
                <span>PetShow</span>
            </button>
            <button @click="activeCustomerTab = 'orders'" :class="activeCustomerTab === 'orders' ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1 relative">
                <i class="fa-solid fa-receipt text-base mb-0.5"></i>
                <span>Đơn hàng</span>
                <span x-show="customerOrdersEnhanced.length > 0" class="absolute top-0 right-1 w-2 h-2 bg-amber-500 rounded-full"></span>
            </button>
            <template x-if="isAuth">
                <button @click="activeCustomerTab = 'account'" :class="(activeCustomerTab === 'account' || activeCustomerTab === 'profile') ? 'text-brand-600 font-bold' : 'text-slate-500'" class="flex flex-col items-center p-1">
                    <i class="fa-solid fa-user-gear text-base mb-0.5"></i>
                    <span>Tài khoản</span>
                </button>
            </template>
            <template x-if="!isAuth">
                <button @click="openLoginModal()" class="flex flex-col items-center p-1 text-slate-500 hover:text-brand-600">
                    <i class="fa-solid fa-right-to-bracket text-base mb-0.5"></i>
                    <span>Đăng nhập</span>
                </button>
            </template>
        </div>
    </div>
"""
