JS_HTML = '''<!-- ==================== LOGIC XỬ LÝ DỮ LIỆU & ALPINE.JS STORE TOÀN DIỆN ==================== -->
<script>
function superPetCareApp() {
    return {
        init() {
            if (typeof window !== 'undefined') {
                const h = window.location.hash;
                const s = window.location.search;
                if (h === '#booking' || h === '#services' || h === '#dichvu' || s.includes('tab=booking')) {
                    this.activeCustomerTab = 'booking';
                }
            }
            this.syncPetBookingDetails(this.serviceBookingForm.petId);
            
            // Chuẩn hóa và đồng bộ thuộc tính image/img cho toàn bộ danh sách đơn hàng
            if (this.customerOrdersEnhanced && Array.isArray(this.customerOrdersEnhanced)) {
                this.customerOrdersEnhanced.forEach(ord => {
                    if (ord.items && Array.isArray(ord.items)) {
                        ord.items.forEach(it => {
                            const validImg = it.image || it.img || this.getItemImage(it);
                            it.image = validImg;
                            it.img = validImg;
                        });
                    }
                });
            }
            if (this.cart && Array.isArray(this.cart)) {
                this.cart.forEach(it => {
                    const validImg = it.image || it.img || this.getItemImage(it);
                    it.image = validImg;
                    it.img = validImg;
                });
            }
        },

        // Trạng thái xác thực & Điều hướng
        isLoggedIn: false, // Mặc định khi vào là Khách chưa đăng nhập
        get isAuth() { return this.isLoggedIn; },
        set isAuth(val) { this.isLoggedIn = val; },
        get userToken() { return this.isLoggedIn ? 'mock-user-token-petcare-2026' : null; },
        currentRole: 'customer', // Mặc định hiển thị giao diện khách hàng
        activeCustomerTab: 'home', // 'home' | 'petshare' | 'shop' | 'booking' | 'orders' | 'profile' | 'faq' | 'legal'
        get currentTab() { return this.activeCustomerTab; },
        set currentTab(val) { this.activeCustomerTab = val; },

        activeAdminTab: 'dashboard', // 'dashboard' | 'appointments' | 'orders' | 'products' | 'pets' | 'analytics'
        get adminTab() { return this.activeAdminTab; },
        set adminTab(val) { this.activeAdminTab = val; },

        adminTimeFilter: 'all', // 'all' | 'today' | '7days' | 'month' | 'quarter'
        globalBranch: 'all', // 'all' | 'HN' | 'Q1' | 'Q7' | 'BT'
        currentOrderTypeTab: 'all',
        showLowStockOnly: false,
        sidebarOpen: false,

        // Thông báo hệ thống Admin
        showAdminNotifications: false,
        adminNotifications: [
            { id: 1, type: 'order', icon: 'fa-solid fa-receipt', title: 'Đơn hàng mới thanh toán', desc: 'Khách hàng Nguyễn Phương Thảo vừa thanh toán đơn ORD-8821 qua VietQR (700.000đ)', time: '2 phút trước', read: false },
            { id: 2, type: 'appointment', icon: 'fa-solid fa-calendar-check', title: 'Lịch hẹn mới được đặt', desc: 'Lịch Spa Cắt tỉa bé Bơ (Corgi) lúc 09:30 ngày 21/10 tại CN Quận 7 đã được ghi nhận', time: '15 phút trước', read: false },
            { id: 3, type: 'warning', icon: 'fa-solid fa-triangle-exclamation', title: 'Cảnh báo tồn kho an toàn', desc: 'Sản phẩm "Gel Dinh Dưỡng Virbac Nutri-plus" tại CN Quận 7 sắp hết hàng (còn 6 tuýp)', time: '35 phút trước', read: false },
            { id: 4, type: 'service', icon: 'fa-solid fa-stethoscope', title: 'Cập nhật trạng thái dịch vụ', desc: 'Lịch hẹn APT-1088 đã được Bác sĩ chuyển sang trạng thái: Đang tiếp khách', time: '1 giờ trước', read: false },
            { id: 5, type: 'system', icon: 'fa-solid fa-shield-cat', title: 'Hệ sinh thái PetCare360', desc: 'Hoàn tất chu kỳ tính điểm & cập nhật đặc quyền thành viên 6 tháng định kỳ Q4/2026', time: '2 giờ trước', read: false }
        ],

        // Bộ lọc & Tìm kiếm Khách hàng & Admin
        searchQuery: '',
        // ==================== 1. SẢN PHẨM & E-COMMERCE CATALOG & DETAIL ====================
        shopViewMode: 'catalog', // 'catalog' | 'detail'
        shopSpecies: '', // '' | 'Chó' | 'Mèo' | 'Thỏ'
        shopProductType: '', // '' | 'Thức ăn hạt' | 'Pate' | 'Cát vệ sinh' | 'Phụ kiện & Đồ chơi' | 'Thuốc thú y'
        shopBrand: '',
        shopMaxPrice: 1500000,
        shopExpressShip: false,
        shopSortBy: 'newest', // 'newest' | 'bestseller' | 'price_asc' | 'price_desc'
        shopCurrentPage: 1,
        shopPageSize: 12,
                shopCategory: '', // '' = Tất cả | 'Thức ăn & Dinh dưỡng' | 'Phụ kiện & Vệ sinh' | 'Thuốc & Y tế'

        // BẢNG GIÁ KHÁCH SẠN THÚ CƯNG 5 SAO DUY NHẤT ÁP DỤNG CHUNG CHO CHÓ & MÈO THEO CÂN NẶNG
        baseServicePrice: 350000,
        selectedWeightSize: '8kg - 12kg',
        hotelPopupRow: null,
        currentPetGroomingTier: '8kg-12kg',
        currentPetHotelTier: '8kg - 12kg',
        groomingIncludeSpa: true,
        groomingCutType: 'grooming', // 'grooming' | 'shave' | 'none'
        selectedBaseService: {
            id: 'hotel_overnight_8-12',
            name: 'Khách Sạn Thú Cưng Tiêu Chuẩn 5 Sao (Lưu Trú Qua Đêm 24h - 8kg - 12kg)',
            category: 'hotel',
            type: 'overnight',
            weightTier: '8kg - 12kg',
            price: 350000,
            duration: 'Lưu trú theo ngày (24h)'
        },
        // BẢNG GIÁ KHÁCH SẠN THÚ CƯNG THEO PHÂN HẠNG CÂN NẶNG (7 SIZE CHUẨN DÙNG CHUNG CHÓ & MÈO)
        petHotelWeightPriceList: [
            { size: 'Dưới 2kg', duration: 'Lưu trú theo ngày (24h)', price: 200000, daycarePrice: 140000, desc: 'Mèo sơ sinh, cún siêu nhỏ (Chihuahua teacup, Tiny Poodle, Phốc sơ sinh)' },
            { size: '2kg - 5kg', duration: 'Lưu trú theo ngày (24h)', price: 250000, daycarePrice: 180000, desc: 'Mèo trưởng thành, chó nhỏ (Poodle Toy, Phốc sóc, Phốc hươu)' },
            { size: '5kg - 8kg', duration: 'Lưu trú theo ngày (24h)', price: 300000, daycarePrice: 220000, desc: 'Mèo lớn (Mèo Anh lông ngắn/dài, Ba Tư), chó nhỏ (Bắc Kinh, Pug)' },
            { size: '8kg - 12kg', duration: 'Lưu trú theo ngày (24h)', price: 350000, daycarePrice: 260000, desc: 'Corgi, Shiba Inu, French Bulldog, Mèo khổng lồ Maine Coon' },
            { size: '12kg - 18kg', duration: 'Lưu trú theo ngày (24h)', price: 400000, daycarePrice: 300000, desc: 'Border Collie, Bull Anh, Beagle, Cocker Spaniel, chó tầm trung' },
            { size: '18kg - 25kg', duration: 'Lưu trú theo ngày (24h)', price: 450000, daycarePrice: 340000, desc: 'Husky, Samoyed, Golden Retriever nhỏ, Chó Phú Quốc, chó cỡ lớn' },
            { size: 'Trên 25kg', duration: 'Lưu trú theo ngày (24h)', price: 500000, daycarePrice: 380000, desc: 'Alaska Malamute, Golden lớn, Labrador, Doberman, Becgie' }
        ],

        hotelExtraServicesList: [
            { name: 'Tắm sấy khử khuẩn trước khi check-out', price: '50.000 đ' },
            { name: 'Xe đưa đón PetShip360 tận nhà', price: '60.000 đ / lượt' },
            { name: 'Cắt mài móng & Vệ sinh tai mắt', price: '40.000 đ' },
            { name: 'Khẩu phần thịt bò/cá hồi áp chảo tươi', price: '50.000 đ / bữa' }
        ],

        // Fallback mock array gồm 8 object sản phẩm thú cưng chuẩn thiết kế
        fallbackRelatedProducts: [
            { id: 1, name: 'Thức Ăn Hạt Royal Canin Mini Adult (Chó Nhỏ)', brand: 'Royal Canin (Pháp)', category: 'Thức ăn & Dinh dưỡng', price: 360000, originalPrice: 420000, discountPercent: '-15%', rating: 4.9, sold: 1420, image: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80', expressShip: true },
            { id: 2, name: 'Hạt Royal Canin Kitten Dinh Dưỡng Toàn Diện Cho Mèo Con', brand: 'Royal Canin (Pháp)', category: 'Thức ăn & Dinh dưỡng', price: 395000, originalPrice: 480000, discountPercent: '-18%', rating: 5.0, sold: 1890, image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80', expressShip: true },
            { id: 3, name: 'Thức Ăn Hạt Orijen Original Biologically Appropriate', brand: 'Orijen (Canada)', category: 'Thức ăn & Dinh dưỡng', price: 890000, originalPrice: 1100000, discountPercent: '-20%', rating: 4.9, sold: 530, image: 'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?auto=format&fit=crop&w=500&q=80', expressShip: true },
            { id: 4, name: 'Combo 12 Lon Pate Monge Hạt Bổ Dưỡng Cho Chó (Ý)', brand: 'Monge (Italy)', category: 'Thức ăn & Dinh dưỡng', price: 420000, originalPrice: 520000, discountPercent: '-20%', rating: 4.8, sold: 1120, image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=500&q=80', expressShip: true },
            { id: 5, name: 'Pate Ciao Churu Cá Ngừ & Sò Điệp Bổ Sung Nước Cho Mèo (Gói 20 Thanh)', brand: 'Inaba Ciao (Nhật)', category: 'Thức ăn & Dinh dưỡng', price: 215000, originalPrice: 280000, discountPercent: '-23%', rating: 5.0, sold: 3400, image: 'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=500&q=80', expressShip: true },
            { id: 6, name: 'Gel Dinh Dưỡng Bổ Sung Năng Lượng & Vitamin Nutri-plus Gel', brand: 'Virbac (Pháp)', category: 'Thức ăn & Dinh dưỡng', price: 295000, originalPrice: 350000, discountPercent: '-15%', rating: 5.0, sold: 2150, image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80', expressShip: true },
            { id: 7, name: 'Cát Đậu Nành Tofu Cature Kháng Khuẩn Tự Nhiên (Hương Trà Xanh 6L)', brand: 'Cature (Mỹ)', category: 'Phụ kiện & Vệ sinh', price: 165000, originalPrice: 220000, discountPercent: '-25%', rating: 4.8, sold: 2890, image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=500&q=80', expressShip: true },
            { id: 8, name: 'Sữa Tắm Trị Nấm & Khử Mùi Hôi Cho Thú Cưng Davis Chlorhexidine 4%', brand: 'Davis (Mỹ)', category: 'Phụ kiện & Vệ sinh', price: 340000, originalPrice: 420000, discountPercent: '-20%', rating: 4.9, sold: 980, image: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=500&q=80', expressShip: true }
        ],
        selectedProductDetailId: 1,
        mainProductImage: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=800&q=80',
        productThumbnails: [
            'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=400&q=80',
            'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?auto=format&fit=crop&w=400&q=80',
            'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=400&q=80',
            'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=400&q=80'
        ],
        selectedWeight: '3kg',
        selectedFlavor: 'Vị Cá Hồi',
        productDetailQty: 1,
        productDetailTab: 'desc', // 'desc' | 'feeding' | 'reviews'
        reviewFilterPhotosOnly: false,
        productReviewsList: [
            {
                id: 1,
                author: 'Nguyễn Văn Minh',
                user: 'Nguyễn Văn Minh',
                avatar: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=150&q=80',
                rating: 5,
                stars: [1, 2, 3, 4, 5],
                date: '25/10/2026',
                variant: '3kg - Vị Cá Hồi',
                comment: 'Hạt thơm ngậy, cún nhà mình rất thích. Lông mượt hơn rõ sau 2 tuần sử dụng. Giao hàng PetShip360 chỉ 1 tiếng là tới tận nhà!',
                photos: [
                    'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                    'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80'
                ],
                photo: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                verified: true,
                likes: 18,
                isLiked: false,
                showReplyInput: false,
                newReplyText: '',
                replies: [
                    {
                        author: 'PetCare360 Support',
                        isAdmin: true,
                        date: '25/10/2026',
                        content: 'Cảm ơn anh Minh đã tin tưởng lựa chọn PetCare360! Chúc bé cún luôn khỏe mạnh và năng động ạ.'
                    }
                ]
            },
            {
                id: 2,
                author: 'Trần Thị Thu Hà',
                user: 'Trần Thị Thu Hà',
                avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=150&q=80',
                rating: 5,
                stars: [1, 2, 3, 4, 5],
                date: '20/10/2026',
                variant: '1kg - Vị Thịt Bò',
                comment: 'Bao bì zip đóng kín bảo quản tốt. Viên hạt vừa miệng không bị vụn bở, bé ăn sạch bát!',
                photos: [
                    'https://images.unsplash.com/photo-1587300003388-59208cc962cb?auto=format&fit=crop&w=600&q=80'
                ],
                photo: 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?auto=format&fit=crop&w=600&q=80',
                verified: true,
                likes: 12,
                isLiked: false,
                showReplyInput: false,
                newReplyText: '',
                replies: []
            },
            {
                id: 3,
                author: 'Lê Hoàng Nam',
                user: 'Lê Hoàng Nam',
                avatar: 'https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?auto=format&fit=crop&w=150&q=80',
                rating: 4.8,
                stars: [1, 2, 3, 4, 5],
                date: '15/10/2026',
                variant: '10kg - Vị Cá Hồi',
                comment: 'Mua bao 10kg tiết kiệm được nhiều. Hàng chính hãng 100% có tem kiểm định y tế đầy đủ.',
                photos: [
                    'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=600&q=80'
                ],
                photo: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=600&q=80',
                verified: true,
                likes: 9,
                isLiked: false,
                showReplyInput: false,
                newReplyText: '',
                replies: []
            }
        ],

        // ==================== 2. DỊCH VỤ & PRICING MATRIX & BOOKING ====================
        servicePricingTab: 'grooming', // 'grooming' | 'hotel' | 'vaccine' | 'spa'
        
        // BẢNG GIÁ DỊCH VỤ THEO 3 ẢNH THỰC TẾ YÊU CẦU:
        // Ảnh 2: SERVICES PRICE LIST (Grooming & Spa + Dịch vụ lẻ + Gói tắm tháng)
        groomingPriceList: [
            { weight: '< 2kg', spa: 270000, grooming: 420000, shave: 350000 },
            { weight: '2kg-5kg', spa: 330000, grooming: 500000, shave: 420000 },
            { weight: '5kg-8kg', spa: 380000, grooming: 590000, shave: 500000 },
            { weight: '8kg-12kg', spa: 440000, grooming: 690000, shave: 570000 },
            { weight: '12kg-18kg', spa: 520000, grooming: 800000, shave: 660000 },
            { weight: '18kg-25kg', spa: 610000, grooming: 930000, shave: 770000 },
            { weight: '25kg-35kg', spa: 720000, grooming: 1100000, shave: 890000 },
            { weight: '> 35kg', spa: 850000, grooming: 1300000, shave: 1000000 }
        ],
        otherServicesList: [
            { name: 'Nail clip (Cắt móng)', price: '80.000 đ' },
            { name: 'Ear wash (Vệ sinh tai)', price: '60.000 đ' },
            { name: 'Brush teeth (Vệ sinh răng miệng)', price: '55.000 đ' },
            { name: 'Detangle depending on areas (Gỡ rối theo tình trạng)', price: '50.000 - 700.000 đ' },
            { name: 'Treatment shampoo (Tắm đặc trị ve, nấm/viêm da)', price: '50.000 đ' },
            { name: 'Surcharge for late check-in (Phụ thu sau 5PM)', price: '70.000 đ' }
        ],

        
        // Tiêm phòng & Khám tận nhà
        vaccinePriceList: [
            { name: 'Vắc-xin 7 Bệnh Toàn Diện Cho Chó (Pháp)', price: 350000, duration: '30 phút', desc: 'Khám sàng lọc lâm sàng miễn phí, tiêm bắp không đau, dán tem sổ tiêm y tế' },
            { name: 'Vắc-xin 4 Bệnh Nhập Khẩu Cho Mèo (Mỹ)', price: 380000, duration: '30 phút', desc: 'Phòng giảm bạch cầu, viêm mũi khí quản, Calicivirus và Chlamydia' },
            { name: 'Tiêm Phòng Bệnh Dại Rabies', price: 150000, duration: '15 phút', desc: 'Chứng nhận tiêm phòng dại hợp pháp theo quy định Chi cục Thú y' },
            { name: 'Home Visit Khám Tổng Quát & Lấy Máu Tại Nhà', price: 450000, duration: '45 - 60 phút', desc: 'Bác sĩ thú y đến tận nhà mang đầy đủ vali y tế chuyên dụng, không gây stress cho bé' },
            { name: 'Tẩy Giun Định Kỳ & Nhỏ Gáy Trị Ve Rận', price: 120000, duration: '15 phút', desc: 'Thuốc chính hãng ngoại nhập tiêu diệt sạch ve rận, giun đũa, giun móc' }
        ],
        pricingMatrixData: {
            grooming: [
                { name: 'Cắt Tỉa Lông & Tạo Kiểu Chuẩn Hàn', duration: '60 - 90 phút', steps: '5 bước: Vệ sinh tai móng, vắt tuyến hôi, tắm thảo dược, sấy ion âm, tạo phom', priceS: 250000, priceM: 350000, priceL: 480000, priceXL: 650000 },
                { name: 'Tắm Trị Liệu Trị Nấm & Viêm Da', duration: '45 - 60 phút', steps: '4 bước: Ngâm bồn dược thảo Davis 4%, sấy lạnh dịu nhẹ, xịt nano bạc', priceS: 220000, priceM: 300000, priceL: 420000, priceXL: 580000 },
                { name: 'Gói Spa Toàn Diện Thư Giãn Tinh Dầu', duration: '90 - 120 phút', steps: '7 bước chuyên sâu: Massage bấm huyệt, ngâm sục Jacuzzi, dưỡng lông tơ', priceS: 320000, priceM: 450000, priceL: 600000, priceXL: 790000 }
            ],
                        vaccine: [
                { name: 'Vắc-xin 7 Bệnh Nhập Khẩu Pháp', duration: '30 phút', steps: 'Khám sàng lọc lâm sàng miễn phí, đo thân nhiệt, tiêm bắp không đau, dán tem sổ', priceS: 220000, priceM: 220000, priceL: 220000, priceXL: 220000 },
                { name: 'Home Visit Khám & Tiêm Tận Nhà', duration: '45 phút', steps: 'Bác sĩ thú y mang vali dụng cụ chuyên khoa đến nhà, cấp sổ theo dõi điện tử', priceS: 350000, priceM: 380000, priceL: 420000, priceXL: 480000 },
                { name: 'Xét Nghiệm Máu 18 Chỉ Số Nhanh', duration: '20 phút', steps: 'Lấy máu xét nghiệm máy tự động Mindray, trả kết quả & phác đồ dinh dưỡng', priceS: 450000, priceM: 450000, priceL: 450000, priceXL: 450000 }
            ]
        },
        serviceBookingForm: {
            serviceName: 'Gói Spa & Grooming Cắt Tỉa Lông Toàn Diện',
            petId: 1,
            branch: 'Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Quận 1, TPHCM',
            date: '2026-10-28',
            slot: '09:30',
            timeSlot: '09:30',
            hotelCheckInDate: '2026-10-28',
            hotelCheckOutDate: '2026-10-29',
            hotelCheckInTime: '09:00',
            hotelCheckOutTime: '17:00',
            slots: [
                { time: '08:30', status: 'available', label: 'Còn rảnh' },
                { time: '09:30', status: 'available', label: 'Còn rảnh' },
                { time: '10:30', status: 'full', label: 'Đã đầy' },
                { time: '14:00', status: 'available', label: 'Còn rảnh' },
                { time: '15:30', status: 'available', label: 'Còn rảnh' },
                { time: '17:00', status: 'full', label: 'Đã đầy' },
                { time: '18:30', status: 'available', label: 'Còn rảnh' }
            ],
            addons: ['massage'],
            needPetShip: true,
            petShipAddress: '88 Nguyễn Thị Minh Khai, Quận 1, TP.HCM',
            specialNotes: 'Bé sợ tiếng máy sấy to, cần làm nhẹ nhàng vùng tai.'
        },

        // ==================== 3. POPUP MODAL THÔNG TIN CHI TIẾT THÚ CƯNG (800PX) ====================
        showPetBookingDetailModal: false,
        petBookingDetail: {
            petId: 1,
            name: 'Bơ',
            species: 'Chó',
            breed: 'Corgi Vàng Trắng',
            age: '2 tuổi',
            gender: 'Đực',
            isNeutered: true,
            weight: 5.8,
            suggestedCage: 'Size M (Phù hợp cún 5-10kg, chuồng 80x60x70cm)',
            isVaccinated: true,
            vaccinePhoto: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=400&q=80',
            conditions: 'Không có tiền sử bệnh nền mãn tính',
            allergies: 'Dị ứng hạt ngũ cốc độn, mẫn cảm hải sản',
            medicines: 'Viên uống bổ sung canxi (08:00 sáng sau ăn)',
            dietChoice: 'hotel', // 'self' | 'hotel'
            hygieneHabit: 'walk', // 'tray' | 'pad' | 'walk'
            personalityTags: ['Hòa đồng', 'Sợ tiếng sấy'],
            checkIn: '2026-10-28T09:00',
            checkOut: '2026-10-29T17:00',
            specialStaffNotes: 'Bé ăn chậm, nhớ xoa đầu khen ngợi khi bé ăn hết bát.'
        },

        // ==================== 4. PETSHARE360 SOCIAL FEED ====================
        socialNotificationsOpen: false,
        activeMenuTab: 'general_feed', // 'general_feed' | 'my_posts' | 'vet_tips' | 'pet_streak'
        get socialActiveMenu() { return this.activeMenuTab; },
        set socialActiveMenu(v) { this.activeMenuTab = v; },

        newPostText: '',
        newPostMedia: '',
        newPostMediaList: [],
        newPostPetId: 1,
        selectedTaggedPet: null,
        tagPetPopoverOpen: false,
        emojiPickerOpen: false,
        openPostOptionsId: null,
        openShareMenuPostId: null,
        feedVisibleCount: 3,
        isLoadingMorePosts: false,
        showLightboxModal: false,
        lightboxImages: [],
        lightboxActiveIndex: 0,
        quickCommentText: {},
        toastNotification: { show: false, message: '' },
        streakDays: 12,

        // Checklist chăm sóc hàng ngày của Streak
        streakChecklist: [
            { id: 1, title: 'Cho bé ăn đúng giờ & định lượng hạt dinh dưỡng', time: '07:30 AM', points: 15, completed: true, icon: 'fa-bowl-food', color: 'text-amber-500' },
            { id: 2, title: 'Dắt bé đi dạo công viên & vận động 30 phút', time: '05:30 PM', points: 30, completed: false, icon: 'fa-person-walking-with-cane', color: 'text-emerald-500' },
            { id: 3, title: 'Thay nước sạch khử khuẩn & bổ sung men vi sinh', time: '12:00 PM', points: 15, completed: true, icon: 'fa-droplet', color: 'text-blue-500' },
            { id: 4, title: 'Chải lông massage & kiểm tra vệ sinh mắt, tai, kẽ móng', time: '08:00 PM', points: 20, completed: false, icon: 'fa-soap', color: 'text-purple-500' }
        ],

        // Lịch check-in tuần
        streakDaysOfWeek: [
            { day: 'T2', date: '21/10', done: true },
            { day: 'T3', date: '22/10', done: true },
            { day: 'T4', date: '23/10', done: true },
            { day: 'T5', date: '24/10', done: true },
            { day: 'T6', date: '25/10', done: true },
            { day: 'T7', date: '26/10', done: true, today: true },
            { day: 'CN', date: '27/10', done: false }
        ],

        // Bộ sưu tập huy hiệu Streak
        streakBadges: [
            { id: 1, name: 'Sen Chuyên Cần', desc: 'Duy trì chăm sóc 7 ngày liên tục', icon: 'fa-medal', color: 'from-amber-400 to-orange-500', unlocked: true },
            { id: 2, name: 'Bậc Thầy Đi Dạo', desc: 'Dắt cún đi dạo tích lũy > 10km', icon: 'fa-person-walking', color: 'from-emerald-400 to-teal-500', unlocked: true },
            { id: 3, name: 'Bác Sĩ Tại Gia', desc: 'Cập nhật sổ sức khỏe & tiêm phòng chuẩn lịch', icon: 'fa-user-doctor', color: 'from-blue-400 to-indigo-500', unlocked: true },
            { id: 4, name: 'Sen Vàng Huyền Thoại', desc: 'Chuỗi Streak chạm mốc 30 ngày', icon: 'fa-crown', color: 'from-purple-400 to-pink-500', unlocked: false, progress: '12/30' }
        ],

        get userPets() {
            return this.pets || [];
        },

        // Bộ lọc bài viết theo activeMenuTab (general_feed, my_posts, vet_tips)
        get filteredSocialPosts() {
            const all = this.socialPosts || [];
            const tab = this.activeMenuTab || 'general_feed';
            const currentUserId = this.customerProfile?.id || 1;
            const currentUserName = this.customerProfile?.name || 'Nguyễn Phương Thảo';

            if (tab === 'my_posts') {
                return all.filter(p => p.authorId === currentUserId || p.author === currentUserName || p.author === 'Nguyễn Hoàng Giang');
            }
            if (tab === 'vet_tips') {
                return all.filter(p => p.isVet === true || p.tag === 'vet' || (p.author && p.author.startsWith('Bs.')) || p.badge === 'Bác sĩ Thú y');
            }
            // default: general_feed
            return all;
        },

        // Bài viết hiển thị (có cắt theo feedVisibleCount đối với general_feed)
        get visibleSocialPosts() {
            if (this.activeMenuTab === 'general_feed') {
                return this.filteredSocialPosts.slice(0, this.feedVisibleCount);
            }
            return this.filteredSocialPosts;
        },

        socialNotifications: [
            { id: 1, user: 'Bs. Trần Thu Hà', avatar: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=150&q=80', text: 'đã trả lời bình luận của bạn trong bài viết về Dinh dưỡng cho Corgi', time: '10 phút trước', read: false },
            { id: 2, user: 'Hoàng Minh Đức', avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80', text: 'đã thả tim bài đăng của bạn', time: '35 phút trước', read: false },
            { id: 3, user: 'Lê Thị Mai', avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=150&q=80', text: 'đã nhắc đến bạn trong một bình luận: #PoodleSàiGòn', time: '2 giờ trước', read: true }
        ],

        socialPosts: [
            {
                id: 1,
                authorId: 1,
                author: 'Nguyễn Phương Thảo',
                petName: 'Bơ (Butter)',
                breed: 'Corgi Vàng Trắng',
                avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80',
                time: '15 phút trước',
                content: 'Hôm nay dẫn bé Bơ đi spa tạo phom mông trái tim tại PetCare360 về cưng xỉu luôn mọi người ơi! Các bác sĩ và KTV siêu nhẹ nhàng, bé về thơm tho không hề bị stress #PoodleSàiGòn #CorgiĐángYêu #KinhNghiệmTắmPet',
                images: [
                    'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=600&q=80',
                    'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=600&q=80'
                ],
                likes: 42,
                isLiked: false,
                isSaved: false,
                likeAnimating: false,
                shares: 6,
                comments: [
                    { id: 1, user: 'Bs. Trần Thu Hà', avatar: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=150&q=80', text: 'Bé Bơ hợp tác lắm nè mẹ Thảo ơi, chúc bé luôn khỏe mạnh nhé!', time: '10 phút trước' },
                    { id: 2, user: 'Hoàng Minh Đức', avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80', text: 'Nhìn quả mông tròn xoe mê quá bạn!', time: '5 phút trước' }
                ]
            },
            {
                id: 2,
                authorId: 2,
                author: 'Lê Thị Mai',
                petName: 'Bé Lu',
                breed: 'Poodle Nâu Đỏ',
                avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=150&q=80',
                time: '2 giờ trước',
                content: 'Góc chia sẻ kinh nghiệm cho các sen có pet hay kén ăn: Mình đổi sang hạt Royal Canin kết hợp pate cá hồi sấy lạnh của PetCare360 được 1 tuần nay, trộm vía Lu ăn hết vèo không chừa một hạt! #MẹoChămSóc #PoodleSàiGòn',
                images: [
                    'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80'
                ],
                likes: 68,
                isLiked: true,
                isSaved: false,
                likeAnimating: false,
                shares: 11,
                comments: [
                    { id: 1, user: 'Phạm Quỳnh Anh', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=150&q=80', text: 'Dòng này hạt mềm vừa răng cún nhỏ, bé nhà mình cũng mê tít!', time: '1 giờ trước' }
                ]
            },
            {
                id: 3,
                authorId: 101,
                isVet: true,
                badge: 'Bác sĩ Thú y',
                author: 'Bs. Trần Thu Hà (Chuyên khoa Dinh dưỡng & Da liễu)',
                petName: 'PetCare360 Clinic',
                breed: 'Bác Sĩ Thú Y',
                avatar: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=150&q=80',
                time: '3 giờ trước',
                content: `🩺 [MẸO BÁC SĨ] Hướng dẫn bổ sung men vi sinh và canxi chuẩn y khoa cho cún mèo giai đoạn dưới 1 tuổi:
1. Tuyệt đối không cho uống sữa bò tươi thông thường vì hầu hết thú cưng không dung nạp lactose, dễ gây viêm ruột.
2. Bổ sung men vi sinh probiotic cách bữa ăn chính 30 phút để kích thích hệ miễn dịch đường ruột tối ưu.
3. Canxi nano chỉ nên bổ sung theo cân nặng chuẩn và có chỉ định của bác sĩ thú y để tránh nguy cơ vôi hóa xương sớm.
#CẩmNangBácSĩ #DinhDưỡngThúCưng #SứcKhỏePet #PetCareClinic`,
                images: [
                    'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80'
                ],
                likes: 184,
                isLiked: false,
                isSaved: true,
                likeAnimating: false,
                shares: 42,
                comments: [
                    { id: 1, user: 'Nguyễn Phương Thảo', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80', text: 'Cảm ơn bác sĩ Hà đã chia sẻ bài viết rất hữu ích cho các sen ạ! ❤️', time: '1 giờ trước' }
                ]
            },
            {
                id: 4,
                authorId: 3,
                author: 'Hoàng Minh Đức',
                petName: 'Bông Lan',
                breed: 'Mèo Anh Lông Ngắn',
                avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=150&q=80',
                time: '4 giờ trước',
                content: 'Gửi Bông Lan ở Pet Hotel 5 sao 3 ngày đi công tác mà nhìn camera live stream thấy bé được nằm phòng điều hòa chơi cầu trượt VIP sướng hơn ở nhà nữa haha #MèoAnhLôngNgắn #PetHotel5Sao',
                images: [
                    'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=600&q=80',
                    'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=600&q=80'
                ],
                likes: 95,
                isLiked: false,
                isSaved: false,
                likeAnimating: false,
                shares: 14,
                comments: []
            },
            {
                id: 5,
                authorId: 102,
                isVet: true,
                badge: 'Bác sĩ Thú y',
                author: 'Bs. Lê Văn Minh (Bác sĩ Trưởng khoa Tiêm chủng)',
                petName: 'PetCare360 Clinic',
                breed: 'Bác Sĩ Thú Y',
                avatar: 'https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=150&q=80',
                time: '6 giờ trước',
                content: `💉 [LỊCH TIÊM CHỦNG] Lịch tiêm nhắc lại hàng năm cho chó (Vaccine 7 bệnh) và mèo (Vaccine 4 bệnh):
- Kháng thể vaccine sẽ suy giảm sau 11-12 tháng, do đó việc tiêm nhắc đúng hạn là bắt buộc để bảo vệ bé khỏi các bệnh hiểm nghèo như Care, Parvo, Dại và Giảm bạch cầu.
- Trước ngày tiêm: Bé cần khỏe mạnh, ăn uống bình thường và được tẩy giun trước 5-7 ngày.
- Hãy đặt lịch tiêm chủng tại nhà trên PetCare360 để bé không phải di chuyển xa nhé!
#TiêmPhòngThúCưng #VaccinePet #BácSĩThúY #PetCare360`,
                images: [
                    'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80'
                ],
                likes: 142,
                isLiked: false,
                isSaved: false,
                likeAnimating: false,
                shares: 28,
                comments: []
            },
            {
                id: 6,
                authorId: 4,
                author: 'Trần Bảo Ngọc',
                petName: 'Milo',
                breed: 'Golden Retriever',
                avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=150&q=80',
                time: '8 giờ trước',
                content: 'Chiều chủ nhật cho Milo ra bãi cỏ vận động của PetCare360 chạy nhảy tưng bừng. Cậu chàng kết bạn được với cả hội Corgi và Samoyed, quẩy nhiệt tình về ngủ khò khò luôn 🐶⚽ #GoldenRetriever #PetCare360 #CuốiTuầnCùngPet',
                images: [
                    'https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&w=600&q=80',
                    'https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?auto=format&fit=crop&w=600&q=80'
                ],
                likes: 112,
                isLiked: false,
                isSaved: false,
                likeAnimating: false,
                shares: 18,
                comments: []
            },
            {
                id: 7,
                authorId: 1,
                author: 'Nguyễn Phương Thảo',
                petName: 'Bơ (Butter)',
                breed: 'Corgi Vàng Trắng',
                avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80',
                time: '1 ngày trước',
                content: 'Hôm nay Bơ đạt chuỗi 12 ngày streak dắt đi dạo 30 phút mỗi ngày rồi nè các sen! Trộm vía dạo này bớt tăng động phá phách hẳn, chân tay săn chắc tròn lẳn cưng xỉu 🐾❤️ #StreakChămPet #CorgiButter #PetCare360',
                images: [
                    'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=600&q=80'
                ],
                likes: 76,
                isLiked: true,
                isSaved: false,
                likeAnimating: false,
                shares: 15,
                comments: []
            },
            {
                id: 8,
                authorId: 6,
                author: 'Vũ Anh Tuấn',
                petName: 'Bắp & Bơ',
                breed: 'Mèo Tai Cụp Scottish',
                avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=150&q=80',
                time: '2 ngày trước',
                content: 'Hai đứa nhỏ sinh đôi Bắp & Bơ lần đầu thử pate cá ngừ phô mai của PetCare360, ăn tranh nhau đến mức liếm sạch cả đĩa. Sen nào có mèo biếng ăn thì highly recommend thử nha! 🥣🧀 #MèoTaiCụp #ScottishFold #PateMèo',
                images: [
                    'https://images.unsplash.com/photo-1574158622682-e40e69881006?auto=format&fit=crop&w=600&q=80',
                    'https://images.unsplash.com/photo-1561948955-570b270e7c36?auto=format&fit=crop&w=600&q=80'
                ],
                likes: 87,
                isLiked: false,
                isSaved: false,
                likeAnimating: false,
                shares: 9,
                comments: []
            }
        ],

        // ==================== 5. PETSHOW360 CAMERA LIVE ====================
        hasActiveLiveOrder: true,
        activeLiveZone: 'dog', // 'dog' | 'cat' | 'play'
        liveCameraAngle: 0,
        isLiveFullscreen: false,
        dailyCareTimeline: [
            { time: '08:00 AM', status: 'completed', title: 'Cho ăn sáng (Hạt Royal Canin 50g)', staff: 'KTV. Nguyễn Lan', photo: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=400&q=80' },
            { time: '10:00 AM', status: 'completed', title: 'Dắt đi dạo khu sân cỏ & Vệ sinh', staff: 'KTV. Trần Nam', photo: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=400&q=80' },
            { time: '02:00 PM', status: 'in_progress', title: 'Tắm sấy dưỡng lông & Cắt tỉa móng', staff: 'BS. Lê Minh', photo: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=400&q=80' },
            { time: '05:00 PM', status: 'pending', title: 'Cho ăn tối & Vệ sinh buồng ngủ', staff: 'KTV. Nguyễn Lan', photo: '' }
        ],

        // ==================== 6. ĐƠN HÀNG DASHBOARD & ACTIONS ====================
        orderFilterStatus: 'all', // 'all' | 'pending' | 'packing' | 'shipping' | 'delivered' | 'cancelled'
        selectedOrderForDetail: null,
        showOrderSummaryModal: false,
        showReviewModal: false,
        reviewOrderData: { orderId: null, productName: '', rating: 5, comment: '', photos: [] },
        showRefundModal: false,
        refundOrderData: { orderId: null, reason: 'Sản phẩm lỗi/hư hỏng khi vận chuyển', details: '', evidence: '' },
        showPODModal: false,
        currentPOD: { photo: '', shipper: '', phone: '', time: '' },
        customerOrdersEnhanced: [
            {
                id: 'ORD-8891',
                orderCode: '#157817',
                date: '27/10/2026',
                status: 'shipping',
                statusText: 'Đang giao hàng',
                badgeColor: 'bg-indigo-100 text-indigo-800 border-indigo-200',
                paymentMethod: 'COD - Tiền mặt khi nhận hàng',
                paymentStatus: 'Chờ thanh toán khi nhận',
                shipper: { name: 'Nguyễn Văn Hùng', phone: '0988 777 666' },
                recipient: { name: 'Nguyễn Hoàng Giang', phone: '0909 123 456', address: '125 Hoàng Quốc Việt, P. Nghĩa Đô, Q. Cầu Giấy, Hà Nội' },
                items: [
                    { name: 'Thức Ăn Hạt Royal Canin Mini Adult (Chó Nhỏ)',
                species: 'Chó',
                productType: 'Thức ăn hạt',
                brandName: 'Royal Canin',
                originalPrice: 420000,
                discountPercent: '-15%',
                expressShip: true, variant: '3kg - Vị Cá Hồi', qty: 1, price: 520000, img: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=200&q=80', image: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=200&q=80' },
                    { name: 'Gel Dinh Dưỡng Nutri-plus Gel', variant: 'Tuýp 120g', qty: 1, price: 165000, img: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=200&q=80', image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=200&q=80' }
                ],
                subtotal: 685000,
                shippingFee: 35000,
                discount: 0,
                total: 720000
            },
            {
                id: 'ORD-8892',
                orderCode: '#157642',
                date: '24/10/2026',
                status: 'delivered',
                statusText: 'Đã giao / Hoàn thành',
                badgeColor: 'bg-emerald-100 text-emerald-800 border-emerald-200',
                paymentMethod: 'Chuyển khoản VietQR',
                paymentStatus: 'Đã thanh toán',
                shipper: { name: 'Trần Thanh Phong', phone: '0912 345 678' },
                podPhoto: 'https://images.unsplash.com/photo-1549465220-1a8b9238cd48?auto=format&fit=crop&w=600&q=80',
                recipient: { name: 'Nguyễn Hoàng Giang', phone: '0909 123 456', address: '125 Hoàng Quốc Việt, P. Nghĩa Đô, Q. Cầu Giấy, Hà Nội' },
                items: [
                    { name: 'Cát Đậu Nành Tofu Cature Kháng Khuẩn Tự Nhiên', variant: 'Hương Trà Xanh 6L', qty: 2, price: 145000, img: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?auto=format&fit=crop&w=200&q=80', image: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?auto=format&fit=crop&w=200&q=80' },
                    { name: 'Sữa Tắm Trị Nấm Davis 4%', variant: 'Chai 355ml', qty: 1, price: 235000, img: 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=200&q=80', image: 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=200&q=80' }
                ],
                subtotal: 525000,
                shippingFee: 0,
                discount: 0,
                total: 525000
            },
            {
                id: 'ORD-8893',
                orderCode: '#157520',
                date: '22/10/2026',
                status: 'packing',
                statusText: 'Đang đóng gói',
                badgeColor: 'bg-blue-100 text-blue-800 border-blue-200',
                paymentMethod: 'Ví điện tử MoMo',
                paymentStatus: 'Đã thanh toán',
                recipient: { name: 'Nguyễn Hoàng Giang', phone: '0909 123 456', address: '125 Hoàng Quốc Việt, Cầu Giấy, Hà Nội' },
                items: [
                    { name: 'Thức Ăn Hạt Orijen Original Biologically Appropriate',
                species: 'Chó',
                productType: 'Thức ăn hạt',
                brandName: 'Orijen',
                originalPrice: 1100000,
                discountPercent: '-20%',
                expressShip: true, variant: '3kg - Vị Gà & Cá', qty: 1, price: 680000, img: 'https://images.unsplash.com/photo-1608408891486-e547372c3d82?auto=format&fit=crop&w=200&q=80', image: 'https://images.unsplash.com/photo-1608408891486-e547372c3d82?auto=format&fit=crop&w=200&q=80' }
                ],
                subtotal: 680000,
                shippingFee: 0,
                discount: 0,
                total: 680000
            },
            {
                id: 'ORD-8894',
                orderCode: '#157401',
                date: '18/10/2026',
                status: 'pending',
                statusText: 'Chờ xác nhận',
                badgeColor: 'bg-amber-100 text-amber-800 border-amber-200',
                paymentMethod: 'Chuyển khoản VietQR',
                paymentStatus: 'Đã thanh toán',
                recipient: { name: 'Nguyễn Hoàng Giang', phone: '0909 123 456', address: 'Chi nhánh Quận 7 (Tiếp nhận tại viện)' },
                items: [
                    { name: 'Gói Spa & Grooming Cắt Tỉa Lông Toàn Diện', variant: 'Bé Bơ (Corgi 5.8kg)', qty: 1, price: 350000, img: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=200&q=80', image: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=200&q=80' }
                ],
                subtotal: 350000,
                shippingFee: 0,
                discount: 0,
                total: 350000
            }
        ],

        // ==================== 7. GIỎ HÀNG 5 BƯỚC (MIXED CART & VOUCHER WALLET) ====================
        cartStep: 1, // 1: Giỏ hàng, 2: Giao hàng, 3: Thanh toán, 4: Thành công / Giữ kho, 5: Lịch sử đơn hàng
        cartNotes: '',
        couponCode: '',
        discountAmount: 0,
        deliveryMethod: 'door', // 'door' | 'store'
        baseShippingFee: 35000,
        checkoutShippingForm: {
            country: 'Việt Nam',
            name: 'Nguyễn Hoàng Giang',
            phone: '0909123456',
            address: '125 Hoàng Quốc Việt',
            city: 'TP. Hồ Chí Minh',
            district: 'Quận 1',
            ward: 'Phường Đa Kao',
            notes: '',
            touched: {
                name: false,
                phone: false,
                address: false,
                city: false,
                district: false,
                ward: false
            }
        },
        vnProvinces: [
            {
                name: 'TP. Hồ Chí Minh',
                districts: [
                    { name: 'Quận 1', wards: ['Phường Bến Nghé', 'Phường Bến Thành', 'Phường Đa Kao', 'Phường Tân Định', 'Phường Nguyễn Thái Bình', 'Phường Phạm Ngũ Lão', 'Phường Cầu Kho', 'Phường Cầu Ông Lãnh', 'Phường Cô Giang', 'Phường Nguyễn Cư Trinh'] },
                    { name: 'Quận 3', wards: ['Phường Võ Thị Sáu', 'Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5', 'Phường 9', 'Phường 10', 'Phường 11', 'Phường 12', 'Phường 14'] },
                    { name: 'Quận 4', wards: ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 6', 'Phường 8', 'Phường 9', 'Phường 10', 'Phường 13', 'Phường 14', 'Phường 15', 'Phường 16', 'Phường 18'] },
                    { name: 'Quận 5', wards: ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5', 'Phường 6', 'Phường 7', 'Phường 8', 'Phường 9', 'Phường 10', 'Phường 11', 'Phường 12', 'Phường 13', 'Phường 14'] },
                    { name: 'Quận 6', wards: ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5', 'Phường 6', 'Phường 7', 'Phường 8', 'Phường 9', 'Phường 10', 'Phường 11', 'Phường 12', 'Phường 13', 'Phường 14'] },
                    { name: 'Quận 7', wards: ['Phường Tân Phong', 'Phường Tân Quy', 'Phường Phú Mỹ', 'Phường Tân Thuận Đông', 'Phường Tân Thuận Tây', 'Phường Tân Kiểng', 'Phường Tân Hưng', 'Phường Bình Thuận', 'Phường Phú Thuận', 'Phường Tân Phú'] },
                    { name: 'Quận 8', wards: ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5', 'Phường 6', 'Phường 7', 'Phường 8', 'Phường 9', 'Phường 10', 'Phường 11', 'Phường 12', 'Phường 13', 'Phường 14', 'Phường 15', 'Phường 16'] },
                    { name: 'Quận 10', wards: ['Phường 1', 'Phường 2', 'Phường 4', 'Phường 5', 'Phường 6', 'Phường 7', 'Phường 8', 'Phường 9', 'Phường 10', 'Phường 11', 'Phường 12', 'Phường 13', 'Phường 14', 'Phường 15'] },
                    { name: 'Quận 11', wards: ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5', 'Phường 6', 'Phường 7', 'Phường 8', 'Phường 9', 'Phường 10', 'Phường 11', 'Phường 12', 'Phường 13', 'Phường 14', 'Phường 15', 'Phường 16'] },
                    { name: 'Quận 12', wards: ['Phường Tân Chánh Hiệp', 'Phường Tân Thới Hiệp', 'Phường Thạnh Lộc', 'Phường Thạnh Xuân', 'Phường Thới An', 'Phường An Phú Đông', 'Phường Hiệp Thành', 'Phường Đông Hưng Thuận', 'Phường Tân Hưng Thuận', 'Phường Trung Mỹ Tây', 'Phường Tân Thới Nhất'] },
                    { name: 'Bình Thạnh', wards: ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 5', 'Phường 6', 'Phường 7', 'Phường 11', 'Phường 12', 'Phường 13', 'Phường 14', 'Phường 15', 'Phường 17', 'Phường 19', 'Phường 21', 'Phường 22', 'Phường 24', 'Phường 25', 'Phường 26', 'Phường 27', 'Phường 28'] },
                    { name: 'Phú Nhuận', wards: ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5', 'Phường 7', 'Phường 8', 'Phường 9', 'Phường 10', 'Phường 11', 'Phường 13', 'Phường 15', 'Phường 17'] },
                    { name: 'Gò Vấp', wards: ['Phường 1', 'Phường 3', 'Phường 4', 'Phường 5', 'Phường 6', 'Phường 7', 'Phường 8', 'Phường 9', 'Phường 10', 'Phường 11', 'Phường 12', 'Phường 13', 'Phường 14', 'Phường 15', 'Phường 16', 'Phường 17'] },
                    { name: 'Tân Bình', wards: ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5', 'Phường 6', 'Phường 7', 'Phường 8', 'Phường 9', 'Phường 10', 'Phường 11', 'Phường 12', 'Phường 13', 'Phường 14', 'Phường 15'] },
                    { name: 'Tân Phú', wards: ['Phường Hiệp Tân', 'Phường Hòa Thạnh', 'Phường Phú Thạnh', 'Phường Phú Thọ Hòa', 'Phường Phú Trung', 'Phường Sơn Kỳ', 'Phường Tân Quý', 'Phường Tân Sơn Nhì', 'Phường Tân Thành', 'Phường Tân Thới Hòa', 'Phường Tây Thạnh'] },
                    { name: 'Bình Tân', wards: ['Phường An Lạc', 'Phường An Lạc A', 'Phường Bình Hưng Hòa', 'Phường Bình Hưng Hòa A', 'Phường Bình Hưng Hòa B', 'Phường Bình Trị Đông', 'Phường Bình Trị Đông A', 'Phường Bình Trị Đông B', 'Phường Tân Tạo', 'Phường Tân Tạo A'] },
                    { name: 'TP. Thủ Đức', wards: ['Phường Thảo Điền', 'Phường An Phú', 'Phường An Khánh', 'Phường Bình Trưng Đông', 'Phường Bình Trưng Tây', 'Phường Cát Lái', 'Phường Thạnh Mỹ Lợi', 'Phường Hiệp Phú', 'Phường Tăng Nhơn Phú A', 'Phường Tăng Nhơn Phú B', 'Phường Phước Long A', 'Phường Phước Long B', 'Phường Trường Thọ', 'Phường Linh Chiểu', 'Phường Linh Tây', 'Phường Linh Trung', 'Phường Linh Xuân', 'Phường Linh Đông', 'Phường Tam Phú', 'Phường Tam Bình', 'Phường Hiệp Bình Chánh', 'Phường Hiệp Bình Phước'] },
                    { name: 'Bình Chánh', wards: ['Thị trấn Tân Túc', 'Xã An Phú Tây', 'Xã Bình Chánh', 'Xã Bình Hưng', 'Xã Bình Lợi', 'Xã Đa Phước', 'Xã Hưng Long', 'Xã Lê Minh Xuân', 'Xã Phạm Văn Hai', 'Xã Phong Phú', 'Xã Quy Đức', 'Xã Tân Kiên', 'Xã Tân Nhựt', 'Xã Tân Quý Tây', 'Xã Vĩnh Lộc A', 'Xã Vĩnh Lộc B'] },
                    { name: 'Hóc Môn', wards: ['Thị trấn Hóc Môn', 'Xã Bà Điểm', 'Xã Đông Thạnh', 'Xã Nhị Bình', 'Xã Tân Hiệp', 'Xã Tân Thới Nhì', 'Xã Tân Xuân', 'Xã Thới Tam Thôn', 'Xã Trung Chánh', 'Xã Xuân Thới Đông', 'Xã Xuân Thới Sơn', 'Xã Xuân Thới Thượng'] },
                    { name: 'Củ Chi', wards: ['Thị trấn Củ Chi', 'Xã An Nhơn Tây', 'Xã An Phú', 'Xã Bình Mỹ', 'Xã Hòa Phú', 'Xã Nhuận Đức', 'Xã Phạm Văn Cội', 'Xã Phú Hòa Đông', 'Xã Phú Mỹ Hưng', 'Xã Tân An Hội', 'Xã Tân Thông Hội', 'Xã Thái Mỹ', 'Xã Trung An', 'Xã Trung Lập Hạ', 'Xã Trung Lập Thượng'] },
                    { name: 'Nhà Bè', wards: ['Thị trấn Nhà Bè', 'Xã Hiệp Phước', 'Xã Long Thới', 'Xã Nhơn Đức', 'Xã Phú Xuân', 'Xã Phước Kiển', 'Xã Phước Lộc'] },
                    { name: 'Cần Giờ', wards: ['Thị trấn Cần Thạnh', 'Xã An Thới Đông', 'Xã Bình Khánh', 'Xã Cần Giờ', 'Xã Long Hòa', 'Xã Lý Nhơn', 'Xã Tam Thôn Hiệp', 'Xã Thạnh An'] }
                ]
            }
        ],
        paymentMethod: 'vietqr', // 'vietqr' | 'atm' | 'visa' | 'ewallet' | 'cod'
        completedOrderNumber: '#157817',
        completedOrderDate: '27/10/2026',

        // Kho Voucher State
        voucherWalletModalOpen: false,
        voucherWalletTab: 'order', // 'shipping' | 'order'
        voucherSearchInput: '',
        appliedVouchers: {
            shipping: null, // voucher object
            order: null     // voucher object
        },
        availableVouchers: [
            {
                id: 'VOUCHER-SHIP-1',
                code: 'FREESHIP35K',
                type: 'shipping',
                title: 'Freeship Toàn Quốc 35.000đ',
                discountAmount: 35000,
                discountType: 'fixed',
                minOrder: 300000,
                description: 'Giảm 35.000đ phí giao hàng tận nơi cho đơn hàng có sản phẩm vật lý từ 300k',
                expiry: '31/12/2026',
                badge: 'Freeship'
            },
            {
                id: 'VOUCHER-SHIP-2',
                code: 'PETSHIP20K',
                type: 'shipping',
                title: 'Hỗ trợ Phí Ship 20.000đ',
                discountAmount: 20000,
                discountType: 'fixed',
                minOrder: 150000,
                description: 'Giảm 20.000đ phí giao hàng cho đơn sản phẩm vật lý từ 150k',
                expiry: '15/12/2026',
                badge: 'Hot'
            },
            {
                id: 'VOUCHER-ORD-1',
                code: 'PETCARE50K',
                type: 'order',
                title: 'Giảm 50.000đ Đơn Hàng',
                discountAmount: 50000,
                discountType: 'fixed',
                minOrder: 350000,
                description: 'Giảm 50.000đ trực tiếp cho đơn hàng sản phẩm hoặc dịch vụ từ 350k',
                expiry: '30/11/2026',
                badge: 'Bán chạy'
            },
            {
                id: 'VOUCHER-ORD-2',
                code: 'PETCARE10',
                type: 'order',
                title: 'Giảm 10% Tối Đa 50.000đ',
                discountPercent: 10,
                maxDiscount: 50000,
                discountType: 'percent',
                minOrder: 250000,
                description: 'Giảm 10% tối đa 50k - Áp dụng cho mọi giỏ hàng từ 250k',
                expiry: '31/12/2026',
                badge: 'Đặc quyền'
            },
            {
                id: 'VOUCHER-ORD-3',
                code: 'VIPCARE100K',
                type: 'order',
                title: 'Ưu Đãi VIP Khách Quen 100.000đ',
                discountAmount: 100000,
                discountType: 'fixed',
                minOrder: 800000,
                description: 'Giảm ngay 100.000đ cho đơn hàng và dịch vụ từ 800.000đ',
                expiry: '31/12/2026',
                badge: 'VIP'
            },
            {
                id: 'VOUCHER-ORD-4',
                code: 'HOTELPROMO',
                type: 'order',
                title: 'Giảm 15% Dịch Vụ Pet Hotel 5 Sao',
                discountPercent: 15,
                maxDiscount: 150000,
                discountType: 'percent',
                minOrder: 400000,
                description: 'Giảm 15% tối đa 150k cho lịch hẹn lưu trú Pet Hotel 5 Sao',
                expiry: '31/12/2026',
                badge: 'Pet Hotel',
                requiresHotel: true
            }
        ],

        // Inventory Hold & Payment Sync State
        currentPendingOrder: null,
        orderCountdownSeconds: 900,
        orderCountdownTimer: null,
        orderStockHeld: false,
        uploadedReceiptUrl: null,
        webhookSuccessReceived: false,
        
        // ==================== 8. TÀI KHOẢN SAAS DASHBOARD ====================
        accountActiveTab: 'info', // 'info' | 'tier' | 'pets' | 'addresses'
        showChangePasswordModal: false,
        changePasswordForm: { current: '', newPass: '', confirm: '' },
        showAddressModal: false,
        editingAddress: null,
        addressForm: { id: null, label: 'Nhà riêng', receiver: 'Nguyễn Hoàng Giang', phone: '0909 123 456', fullAddress: '125 Hoàng Quốc Việt, P. Nghĩa Đô, Q. Cầu Giấy, Hà Nội', isDefault: true },

        filterCategory: 'all', // 'all' | 'Thức ăn & Dinh dưỡng' | 'Phụ kiện & Vệ sinh' | 'Thuốc & Y tế'
        filterServiceCategory: 'all', // 'all' | 'Y Tế & Chăm Sóc Sức Khỏe' | 'Cấp Cứu & Điều Trị Chuyên Sâu' | 'Spa & Làm Đẹp' | 'Lưu Trú & Tiện Ích'
        serviceSearchQuery: '',
        filterArticleCat: 'all',
        searchArticleQuery: '',
        productSearchQuery: '',
        productCategoryFilter: 'all',
        appointmentSearchQuery: '',
        appointmentServiceFilter: 'all',
        orderSearchQuery: '',
        orderStatusFilter: 'all',
        petSearchQuery: '',
        customerSearchQuery: '',

        // Modals flags
        showLoginModal: false,
        loginModalOpen: false,
        showBookingDetailModal: false,
        bookingDetailModalOpen: false,
        showAddPetModal: false,
        addPetModalOpen: false,
        showEditProfileModal: false,
        editProfileModalOpen: false,
        showAddProductModal: false,
        addProductModalOpen: false,
        showRestockModal: false,
        restockModalOpen: false,
        showChatModal: false,
        chatModalOpen: false,
        showCartDrawer: false,
        cartOpen: false,
        showCheckoutModal: false,
        showLoyaltyDetailModal: false,
        loyaltyDetailModalOpen: false,
        showLegalModal: false,
        policyModalOpen: false,
        addAddressModalOpen: false,
        orderDrawerOpen: false,

        selectedServiceModal: null,
        selectedProductModal: null,
        
        // Khối Bác Sĩ Thú Y Tư Vấn (PetShare360)
        selectedArticle: null,
        vetConsultArticles: [
            {
                id: 'vet-art-1',
                title: 'Lịch tiêm phòng dại & 7 bệnh chuẩn nhất cho cún con 2026',
                doctorName: 'BS. Nguyễn Thanh Tùng',
                author: 'BS. Nguyễn Thanh Tùng',
                doctorAvatar: 'https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=150&q=80',
                coverImage: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=800&q=80',
                image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=800&q=80',
                publishDate: '26/10/2026',
                date: '26/10/2026',
                category: 'Y Khoa Dự Phòng',
                views: 3120,
                summary: 'Phác đồ tiêm chủng ngừa Dại và vắc-xin tổng hợp 7 bệnh theo khuyến cáo mới nhất từ Hiệp hội Thú y Thế giới (WSAVA), bảo vệ cún cưng toàn diện trước Parvovirus và Care.',
                fullContent: `
                    <p class="lead font-medium text-slate-700">Tiêm phòng đúng độ tuổi và đủ mũi là biện pháp duy nhất giúp cún con hình thành kháng thể chủ động, tránh nguy cơ tử vong lên đến 90% khi mắc bệnh truyền nhiễm nguy hiểm.</p>
                    <h4 class="font-extrabold text-slate-900 text-sm mt-4 mb-2 flex items-center gap-2"><i class="fa-solid fa-syringe text-teal-600"></i> Phác Đồ 3 Mũi Vắc-Xin Cơ Bản Cho Cún Con</h4>
                    <ul class="list-disc list-inside space-y-1.5 text-slate-600">
                        <li><strong>Mũi 1 (6 - 8 tuần tuổi):</strong> Vắc-xin phòng 5 bệnh cơ bản (Care, Parvo, Viêm gan truyền nhiễm, Ho cũi chó, Cúm).</li>
                        <li><strong>Mũi 2 (10 - 12 tuần tuổi):</strong> Vắc-xin phòng 7 bệnh (Bổ sung thêm 2 chủng xoắn khuẩn Leptospira lây sang người).</li>
                        <li><strong>Mũi 3 (14 - 16 tuần tuổi):</strong> Vắc-xin 7 bệnh nhắc lại kết hợp Vắc-xin phòng bệnh Dại (Rabies bắt buộc theo quy định thú y).</li>
                        <li><strong>Nhắc lại hàng năm:</strong> 01 mũi 7 bệnh và 01 mũi Dại định kỳ mỗi 12 tháng một lần suốt đời bé.</li>
                    </ul>
                    <div class="my-4 p-4 rounded-2xl bg-teal-50 border border-teal-200">
                        <h5 class="font-bold text-teal-900 text-xs mb-1 flex items-center gap-1.5"><i class="fa-solid fa-circle-exclamation text-teal-600"></i> Lưu ý đặc biệt từ Bác sĩ Tùng:</h5>
                        <p class="text-teal-800 text-xs leading-relaxed">Tuyệt đối không tắm cho cún trong vòng 7 ngày sau khi tiêm. Tránh cho bé tiếp xúc với chó lạ hoặc đi dạo nơi công cộng khi chưa hoàn thành đủ 3 mũi vắc-xin cơ sở.</p>
                    </div>
                `
            },
            {
                id: 'vet-art-2',
                title: 'Cách sơ cứu hạ thân nhiệt cho thú cưng vào mùa nóng',
                doctorName: 'BS. Vũ Mai Anh',
                author: 'BS. Vũ Mai Anh',
                doctorAvatar: 'https://images.unsplash.com/photo-1594824813583-9b2f6efd559a?auto=format&fit=crop&w=150&q=80',
                coverImage: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=800&q=80',
                image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=800&q=80',
                publishDate: '24/10/2026',
                date: '24/10/2026',
                category: 'Cấp Cứu Thường Thức',
                views: 2840,
                summary: 'Sốc nhiệt (Heatstroke) diễn ra rất nhanh ở vùng khí hậu nhiệt đới như TP.HCM. Nắm rõ các bước sơ cứu tức thì sẽ cứu sống bé cưng trong gang tấc.',
                fullContent: `
                    <p class="lead font-medium text-slate-700">Chó mèo không có tuyến mồ hôi dưới da như người mà chỉ thoát nhiệt qua hơi thở và đệm bàn chân. Khi nhiệt độ môi trường vượt quá 35°C, bé rất dễ rơi vào tình trạng suy hô hấp và trụy tim mạch.</p>
                    <h4 class="font-extrabold text-slate-900 text-sm mt-4 mb-2 flex items-center gap-2"><i class="fa-solid fa-triangle-exclamation text-amber-500"></i> Dấu Hiệu Nhận Biết Thú Cưng Bị Sốc Nhiệt</h4>
                    <ul class="list-disc list-inside space-y-1.5 text-slate-600">
                        <li>Thở dốc dữ dội, lưỡi thè dài và chuyển sang màu tím tái hoặc đỏ sẫm.</li>
                        <li>Chảy nhiều dãi nhớt, mắt đờ đẫn, đứng không vững, run rẩy co giật.</li>
                        <li>Thân nhiệt hậu môn tăng cao vượt mức 40°C.</li>
                    </ul>
                    <h4 class="font-extrabold text-slate-900 text-sm mt-4 mb-2 flex items-center gap-2"><i class="fa-solid fa-kit-medical text-rose-500"></i> 4 Bước Sơ Cứu Khẩn Cấp Tại Chỗ</h4>
                    <ol class="list-decimal list-inside space-y-1.5 text-slate-600">
                        <li><strong>Di chuyển ngay:</strong> Đưa thú cưng vào bóng râm mát, phòng điều hòa hoặc trước quạt gió.</li>
                        <li><strong>Làm mát từ từ:</strong> Dùng khăn thấm nước mát (nhiệt độ phòng) đắp lên đệm bàn chân, bụng, bẹn và nách. Tuyệt đối KHÔNG dội nước đá lạnh vì sẽ gây co mạch ngoại vi và sốc nhiệt ngược.</li>
                        <li><strong>Cấp ẩm:</strong> Thấm một ít nước mát vào môi lưỡi, KHÔNG ép bé uống nước ừng ực nếu bé đang khó thở.</li>
                        <li><strong>Chuyển viện khẩn cấp:</strong> Liên hệ ngay Hotline Cấp cứu PetCare360 24/7 (1900 6868) để được bác sĩ đón và cấp cứu kịp thời.</li>
                    </ol>
                `
            }
        ],

        // Customer Reviews & Lightbox State (PDP)
        showCustomerReviewFormModal: false,
        newReviewRating: 5,
        hoverReviewRating: 0,
        newReviewText: '',
        newReviewMediaList: [],
        showReviewLightboxModal: false,
        reviewLightboxImages: [],
        reviewLightboxIndex: 0,
        onlyWithPhotos: false,

        // Thông tin người đại diện đặt lịch & Địa chỉ PetShip (Checkout Step 2)
        checkoutBookingContactName: 'Nguyễn Phương Thảo',
        checkoutBookingContactPhone: '0988 123 456',
        checkoutBookingContactTouched: {
            name: false,
            phone: false,
            street: false,
            district: false,
            ward: false
        },
        checkoutPetShipAddress: {
            street: '',
            city: 'TP. Hồ Chí Minh',
            district: 'Quận 1',
            ward: 'Phường Đa Kao'
        },
        selectedPaymentMethod: 'vietqr',

        selectedArticleModal: null,
        selectedPetHealthModal: null,
        selectedOrder: null,

        // Login form
        loginUsername: '',
        loginPassword: '',
        loginError: '',

        // Lỗi form thêm thú cưng
        petFormError: '',

        // Hồ sơ người dùng
        customerProfile: {
            id: 1,
            name: 'Nguyễn Phương Thảo',
            phone: '0988 123 456',
            email: 'phuongthao.petcare@gmail.com',
            address: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
            avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80',
            points: 3450,
            tier: 'Thành viên Vàng',
            nextTierPoints: 7000,
            petCount: 3,
            activeBookings: 2,
            totalSpent: 18500000
        },
        get userProfile() { return this.customerProfile; },
        set userProfile(val) { this.customerProfile = val; },

        // Danh sách địa chỉ nhận hàng
        addresses: [
            { id: 1, tag: 'Nhà riêng', fullAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM', phone: '0988 123 456', isDefault: true },
            { id: 2, tag: 'Văn phòng', fullAddress: 'Tầng 18 Tòa nhà Bitexco, Số 2 Hải Triều, Bến Nghé, Quận 1, TP.HCM', phone: '0988 123 456', isDefault: false }
        ],

        // Đơn hàng của khách hàng
        customerOrders: [
            {
                id: 'ORD-8821',
                date: '2026-10-20',
                items: 'Royal Canin Mini Adult (1kg), Sữa tắm Davis 4%',
                total: 700000,
                status: 'Đã thanh toán',
                paymentMethod: 'Chuyển khoản VietQR'
            },
            {
                id: 'ORD-8710',
                date: '2026-09-15',
                items: 'Gói Spa & Grooming Cắt Tỉa Lông Toàn Diện (Bé Bơ)',
                total: 350000,
                status: 'Hoàn thành',
                paymentMethod: 'Ví MoMo'
            }
        ],

        // 3 Thú cưng chi tiết đầy đủ 4 nhóm thông tin
        pets: [
            {
                id: 1,
                name: 'Bơ (Butter)',
                type: 'Chó',
                species: 'Chó',
                breed: 'Corgi Pembroke Welsh',
                gender: 'Đực',
                age: '2 tuổi (15/04/2024)',
                weight: '11.5',
                chipId: '900118000452311',
                chip: '900118000452311',
                avatar: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80',
                image: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80',
                appearance: 'Lông vàng trắng ngắn mượt, tai to dựng đứng, đuôi cộc tròn, ngực trắng yếm đôi',
                health: 'Khỏe mạnh, vừa hoàn thành điều trị viêm kẽ móng chân',
                allergies: 'Không dị ứng thuốc, nhạy cảm với thức ăn chứa nhiều mỡ động vật',
                lastVaccine: 'Vắc-xin 7 bệnh chó Nobivac (15/01/2026)',
                nextVaccine: '15/01/2027 (Nhắc lại hàng năm)',
                diet: 'Hạt Royal Canin Mini Adult (80g/ngày), trộn 1/2 hộp Pate Monge gà tây, ăn 2 bữa/ngày',
                habits: 'Thích đi dạo công viên 17h chiều, thích bắt bóng tennis, rất quấn chủ',
                personality: 'Năng động, thân thiện, sủa cảnh giác người lạ gõ cửa, sợ tiếng máy sấy to',
                ownerName: 'Nguyễn Phương Thảo',
                ownerPhone: '0988 123 456',
                ownerAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
                ownerEmergency: '0912 345 678 (Chồng - Anh Hoàng)',
                isDefault: true,
                vaccines: [
                    { name: 'Vắc-xin 7 bệnh chó (Nobivac DHPPi + L4)', date: '15/01/2026', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '15/01/2027', status: 'Đã hoàn thành' },
                    { name: 'Phòng ngừa dại (Rabisin)', date: '15/01/2026', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '15/01/2027', status: 'Đã hoàn thành' },
                    { name: 'Xổ giun định kỳ & Nhỏ gáy Advocate', date: '01/03/2026', doctor: 'BS Đỗ Hoàng Nam', nextDate: '01/06/2026', status: 'Sắp tới hạn' }
                ],
                medicalHistory: [
                    { date: '10/02/2026', diagnosis: 'Viêm da kẽ ngón chân do ẩm ướt', treatment: 'Vệ sinh Chlorhexidine 2%, bôi kem kháng viêm 5 ngày', notes: 'Giữ chân khô ráo sau khi đi dạo' },
                    { date: '05/11/2025', diagnosis: 'Khám sức khỏe tổng quát & Siêu âm ổ bụng', treatment: 'Chỉ số gan thận bình thường, thể trạng khỏe mạnh', notes: 'Bổ sung thêm glucosamine hỗ trợ cột sống ngắn' }
                ]
            },
            {
                id: 2,
                name: 'Mochi',
                type: 'Mèo',
                species: 'Mèo',
                breed: 'Anh Lông Ngắn (Silver Shaded)',
                gender: 'Cái',
                age: '1.5 tuổi (20/10/2024)',
                weight: '4.2',
                chipId: '900118000789123',
                chip: '900118000789123',
                avatar: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=400&q=80',
                image: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=400&q=80',
                appearance: 'Lông ánh bạc silver shaded dày mịn, mắt xanh lục bảo to tròn, mũi hồng',
                health: 'Đã triệt sản nội soi, vết mổ liền đẹp, cân nặng ổn định',
                allergies: 'Dị ứng phấn hoa nhẹ, nhạy cảm với thuốc gây mê nhóm ketamine',
                lastVaccine: 'Vắc-xin 4 bệnh mèo Purevax (20/12/2025)',
                nextVaccine: '20/12/2026',
                diet: 'Hạt Royal Canin Kitten & Sterilised (60g/ngày), thưởng 1 thanh Ciao Churu lúc 20h',
                habits: 'Thích nằm sưởi nắng ban công, cào móng trên trụ đay, ngủ cùng chủ buổi tối',
                personality: 'Điềm đạm, ít kêu, thích được gãi cằm, hay trốn dưới gầm giường khi nhà có khách lạ',
                ownerName: 'Nguyễn Phương Thảo',
                ownerPhone: '0988 123 456',
                ownerAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
                ownerEmergency: '0912 345 678 (Chồng - Anh Hoàng)',
                isDefault: false,
                vaccines: [
                    { name: 'Vắc-xin 4 bệnh mèo (Purevax RCPCh)', date: '20/12/2025', doctor: 'BS Trần Thu Hà', nextDate: '20/12/2026', status: 'Đã hoàn thành' },
                    { name: 'Vắc-xin phòng dại (Rabisin)', date: '20/12/2025', doctor: 'BS Trần Thu Hà', nextDate: '20/12/2026', status: 'Đã hoàn thành' }
                ],
                medicalHistory: [
                    { date: '12/10/2025', diagnosis: 'Phẫu thuật triệt sản nội soi vi phẫu', treatment: 'Hồi phục hoàn toàn sau 48h, chỉ tự tiêu', notes: 'Đã lành sẹo đẹp, chế độ dinh dưỡng hạt Sterilised' }
                ]
            },
            {
                id: 3,
                name: 'Đậu Đậu',
                type: 'Chó',
                species: 'Chó',
                breed: 'Poodle Tiny',
                gender: 'Đực',
                age: '3 tuổi (08/06/2023)',
                weight: '3.6',
                chipId: '900118000994120',
                chip: '900118000994120',
                avatar: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=400&q=80',
                image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=400&q=80',
                appearance: 'Lông nâu đỏ xoăn tít bồng bềnh, dáng nhỏ nhắn, chân ngắn đáng yêu',
                health: 'Răng miệng sạch mảng bám, mắt sáng không bị ố vàng khóe mắt',
                allergies: 'Tiền sử dị ứng đạm thịt bò (ngứa và đỏ tai)',
                lastVaccine: 'Vắc-xin 7 bệnh Nobivac (05/08/2025)',
                nextVaccine: '05/08/2026',
                diet: 'Hạt dinh dưỡng hữu cơ không thịt bò, bổ sung rau củ tươi luộc chín',
                habits: 'Thích được bế ẵm, thích mặc áo len mùa đông, thích đuổi laser',
                personality: 'Thông minh, hoạt bát, hay làm trò xin ăn, thích chơi đùa với trẻ nhỏ',
                ownerName: 'Nguyễn Phương Thảo',
                ownerPhone: '0988 123 456',
                ownerAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
                ownerEmergency: '0912 345 678 (Chồng - Anh Hoàng)',
                isDefault: false,
                vaccines: [
                    { name: 'Vắc-xin 7 bệnh chó (Nobivac DHPPi)', date: '05/08/2025', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '05/08/2026', status: 'Đã hoàn thành' },
                    { name: 'Phòng dại Rabisin', date: '05/08/2025', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '05/08/2026', status: 'Đã hoàn thành' }
                ],
                medicalHistory: [
                    { date: '14/01/2026', diagnosis: 'Lấy cao răng siêu âm & đánh bóng răng', treatment: 'Vệ sinh vôi răng độ 2, xịt keo ong khử khuẩn', notes: 'Duy trì gặm thanh sạch răng hàng ngày' }
                ]
            }
        ],
        get allPets() { return this.pets; },
        set allPets(val) { this.pets = val; },
        get myPets() { return this.pets; },
        set myPets(val) { this.pets = val; },

        // 12 SẢN PHẨM PHÂN LOẠI CHÍNH XÁC THEO 3 DANH MỤC
        products: [
            // Danh mục 1: Thức ăn & Dinh dưỡng (6 sản phẩm)
            {
                id: 1,
                sku: 'PET-FD01',
                name: 'Thức Ăn Hạt Royal Canin Mini Adult (Chó Nhỏ)',
                variantConfig: {
                    weights: [
                        { label: '1kg', price: 185000, sub: 'Dùng thử' },
                        { label: '3kg', price: 520000, sub: 'Phổ biến nhất', tag: 'Hot' },
                        { label: '10kg', price: 1650000, sub: 'Tiết kiệm' }
                    ],
                    flavors: [
                        { label: 'Vị Cá Hồi (Dưỡng lông & Da)', id: 'salmon' },
                        { label: 'Vị Thịt Bò (Phát triển cơ bắp)', id: 'beef' }
                    ]
                },
                variants: [
                    { label: '1kg', price: 185000 },
                    { label: '3kg', price: 520000 },
                    { label: '10kg', price: 1650000 }
                ],
                brand: 'Royal Canin (Pháp)',
                price: 360000,
                rating: 4.9,
                reviews: 184,
                reviewsCount: 184,
                sold: 1420,
                stockQ1: 35,
                stockBT: 28,
                stockQ7: 42,
                q1: 35, bt: 28, q7: 42,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
                desc: 'Hạt dinh dưỡng cao cấp dành cho chó trưởng thành giống nhỏ từ 10 tháng đến 8 tuổi. Giúp duy trì cân nặng lý tưởng nhờ hàm lượng L-carnitine tối ưu và hỗ trợ sức khỏe răng miệng tối đa.',
                description: 'Hạt dinh dưỡng cao cấp dành cho chó trưởng thành giống nhỏ từ 10 tháng đến 8 tuổi.',
                ingredients: 'Protein gia cầm tách nước, bắp, bột bắp, chất béo động vật, gluten bắp, protein thực vật cô lập, lúa mì, khoáng chất, củ cải đường, dầu cá, men bia.',
                usage: 'Cho ăn theo trọng lượng: Chó 2-4kg: 40-70g/ngày; Chó 5-8kg: 80-120g/ngày.'
            },
            {
                id: 2,
                sku: 'PET-FD02',
                name: 'Hạt Royal Canin Kitten Dinh Dưỡng Toàn Diện Cho Mèo Con',
                variantConfig: {
                    weights: [
                        { label: '1kg', price: 195000, sub: 'Gói nhỏ' },
                        { label: '2kg', price: 380000, sub: 'Phổ biến nhất', tag: 'Best Seller' },
                        { label: '10kg', price: 1750000, sub: 'Bao lớn' }
                    ],
                    flavors: [
                        { label: 'Vị Cá Ngừ & Gà', id: 'tuna' },
                        { label: 'Vị Cá Hồi & Sữa', id: 'salmon' }
                    ]
                },
                variants: [
                    { label: '1kg', price: 195000 },
                    { label: '2kg', price: 380000 },
                    { label: '10kg', price: 1750000 }
                ],
                species: 'Mèo',
                productType: 'Thức ăn hạt',
                brandName: 'Royal Canin',
                originalPrice: 480000,
                discountPercent: '-18%',
                expressShip: true,
                brand: 'Royal Canin (Pháp)',
                price: 395000,
                rating: 5.0,
                reviews: 216,
                reviewsCount: 216,
                sold: 1890,
                stockQ1: 45,
                stockBT: 30,
                stockQ7: 50,
                q1: 45, bt: 30, q7: 50,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                desc: 'Công thức đặc chế cho mèo con từ 4 đến 12 tháng tuổi. Bổ sung hệ dưỡng chất tăng cường hệ miễn dịch tự nhiên, DHA phát triển não bộ và protein dễ tiêu hóa LIP.',
                description: 'Công thức đặc chế cho mèo con từ 4 đến 12 tháng tuổi.',
                ingredients: 'Protein gia cầm sấy khô, gạo, gluten lúa mì, mỡ động vật, bột ngô, men thủy phân, dầu đậu nành.',
                usage: 'Mèo con 4-6 tháng: 55-70g/ngày; Mèo con 7-12 tháng: 60-80g/ngày.'
            },
            {
                id: 3,
                sku: 'PET-FD03',
                name: 'Thức Ăn Hạt Orijen Original Biologically Appropriate',
                variantConfig: {
                    weights: [
                        { label: '1kg', price: 295000, sub: 'Gói dùng thử' },
                        { label: '2kg', price: 560000, sub: 'Phổ biến nhất', tag: 'Khuyên Dùng' },
                        { label: '6kg', price: 1550000, sub: 'Tiết kiệm' }
                    ]
                },
                variants: [
                    { label: '1kg', price: 295000 },
                    { label: '2kg', price: 560000 },
                    { label: '6kg', price: 1550000 }
                ],
                brand: 'Orijen (Canada)',
                price: 890000,
                rating: 4.9,
                reviews: 92,
                reviewsCount: 92,
                sold: 530,
                stockQ1: 18,
                stockBT: 12,
                stockQ7: 15,
                q1: 18, bt: 12, q7: 15,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?auto=format&fit=crop&w=500&q=80',
                desc: 'Dòng thức ăn sinh học chuẩn tự nhiên cao cấp bậc nhất thế giới, chứa 85% thành phần từ gia cầm thả vườn, cá hoang dã và trứng tươi nguyên quả. Không ngũ cốc.',
                description: 'Dòng thức ăn sinh học chuẩn tự nhiên cao cấp bậc nhất thế giới.',
                ingredients: 'Thịt gà tươi 13%, thịt gà tây tươi 7%, trứng nguyên quả tươi 7%, gan gà tươi 6%, cá trích tươi 6%.',
                usage: 'Thức ăn dinh dưỡng đậm đặc, nên chuyển đổi thức ăn từ từ trong vòng 7 ngày.'
            },
            {
                id: 4,
                sku: 'PET-PT01',
                name: 'Combo 12 Lon Pate Monge Hạt Bổ Dưỡng Cho Chó (Ý)',
                variantConfig: null,
                variants: [],
                species: 'Chó',
                productType: 'Pate',
                brandName: 'Monge',
                originalPrice: 520000,
                discountPercent: '-20%',
                expressShip: true,
                brand: 'Monge (Italy)',
                price: 420000,
                rating: 4.8,
                reviews: 135,
                reviewsCount: 135,
                sold: 1120,
                stockQ1: 30,
                stockBT: 25,
                stockQ7: 35,
                q1: 30, bt: 25, q7: 35,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=500&q=80',
                desc: 'Pate thịt tươi nấu chậm từ nước Ý với các vị gà tây, cá hồi, thịt bò kết hợp rau củ tươi. Không phẩm màu, không chất bảo quản hóa học.',
                description: 'Pate thịt tươi nấu chậm từ nước Ý.',
                ingredients: 'Thịt tươi nguyên miếng 80%, khoáng chất, vitamin A, D3, E tự nhiên, thảo mộc địa trung hải.',
                usage: 'Dùng ăn trực tiếp hoặc trộn cùng hạt khô để kích thích vị giác.'
            },
            {
                id: 5,
                sku: 'PET-PT02',
                name: 'Pate Ciao Churu Cá Ngừ & Sò Điệp Bổ Sung Nước Cho Mèo (Gói 20 Thanh)',
                variantConfig: null,
                variants: [],
                species: 'Mèo',
                productType: 'Pate',
                brandName: 'Ciao Churu',
                originalPrice: 280000,
                discountPercent: '-23%',
                expressShip: true,
                brand: 'Inaba Ciao (Nhật Bản)',
                price: 215000,
                rating: 5.0,
                reviews: 410,
                reviewsCount: 410,
                sold: 3400,
                stockQ1: 85,
                stockBT: 65,
                stockQ7: 95,
                q1: 85, bt: 65, q7: 95,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=500&q=80',
                desc: 'Treat dạng kem số 1 tại Nhật Bản, vị thơm ngon cuốn hút mọi chú mèo. Cung cấp nước dồi dào ngừa sỏi thận và chiết xuất trà xanh giảm mùi hôi chất thải.',
                description: 'Treat dạng kem số 1 tại Nhật Bản, vị thơm ngon cuốn hút.',
                ingredients: 'Thịt cá ngừ tươi Maguro, chiết xuất sò điệp, collagen biển, chiết xuất trà xanh.',
                usage: 'Cho ăn như món tráng miệng hoặc phần thưởng khi huấn luyện, 2-4 thanh mỗi ngày.'
            },
            {
                id: 6,
                sku: 'PET-MD03',
                name: 'Gel Dinh Dưỡng Bổ Sung Năng Lượng & Vitamin Nutri-plus Gel',
                variantConfig: null,
                variants: [],
                species: 'Chó',
                productType: 'Thuốc thú y',
                brandName: 'Virbac',
                originalPrice: 350000,
                discountPercent: '-15%',
                expressShip: true,
                brand: 'Virbac (Pháp)',
                price: 295000,
                rating: 5.0,
                reviews: 260,
                reviewsCount: 260,
                sold: 2150,
                stockQ1: 2,
                stockBT: 2,
                stockQ7: 2,
                q1: 2, bt: 2, q7: 2, // Tổng tồn kho = 6 (Dưới 10 để demo cảnh báo sắp hết hàng)
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                desc: 'Thực phẩm bổ sung năng lượng cao cấp chứa đầy đủ vitamin nhóm B, A, D, E và các khoáng chất thiết yếu cho thú cưng đang dưỡng bệnh, sau phẫu thuật hoặc mẹ mang thai/cho con bú.',
                description: 'Thực phẩm bổ sung năng lượng cao cấp chứa đầy đủ vitamin.',
                ingredients: 'Vitamin A, D3, E, B1, B2, B6, B12, Nicotinamide, Canxi Pantothenate, Axit Folic, Sắt, Mangan, Magiê.',
                usage: 'Cho ăn trực tiếp hoặc trộn vào thức ăn. Liều lượng: 1-2 muỗng cà phê/5kg thể trọng.'
            },

            // Danh mục 2: Phụ kiện & Vệ sinh (4 sản phẩm)
            {
                id: 7,
                sku: 'PET-VS01',
                name: 'Cát Đậu Nành Tofu Cature Kháng Khuẩn Tự Nhiên (Hương Trà Xanh 6L)',
                variantConfig: null,
                variants: [
                    { label: '1kg', price: 165000 },
                    { label: '3kg', price: 462000 },
                    { label: '10kg', price: 1465000 }
                ],
                species: 'Mèo',
                productType: 'Cát vệ sinh',
                brandName: 'Cature',
                originalPrice: 220000,
                discountPercent: '-25%',
                expressShip: true,
                brand: 'Cature (Mỹ)',
                price: 165000,
                rating: 4.8,
                reviews: 280,
                reviewsCount: 280,
                sold: 2890,
                stockQ1: 60,
                stockBT: 45,
                stockQ7: 75,
                q1: 60, bt: 45, q7: 75,
                category: 'Phụ kiện & Vệ sinh',
                categoryAdmin: 'Phụ kiện & Vệ sinh',
                img: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=500&q=80',
                desc: '100% bã đậu nành tự nhiên vón cục siêu tốc trong 3 giây, kiểm soát mùi hôi vượt trội, tan hoàn toàn trong nước xả bồn cầu cực kỳ tiện lợi và thân thiện môi trường.',
                description: '100% bã đậu nành tự nhiên vón cục siêu tốc trong 3 giây.',
                ingredients: 'Sợi đậu nành hữu cơ, tinh bột ngô tự nhiên, chiết xuất lá trà xanh diệt khuẩn.',
                usage: 'Đổ cát vào khay vệ sinh độ dày khoảng 5-7cm. Dọn các cục vón hàng ngày.'
            },
            {
                id: 8,
                sku: 'PET-VS02',
                name: 'Sữa Tắm Trị Nấm & Khử Mùi Hôi Cho Thú Cưng Davis Chlorhexidine 4%',
                variantConfig: null,
                variants: [],
                species: 'Chó',
                productType: 'Thuốc thú y',
                brandName: 'Davis',
                originalPrice: 420000,
                discountPercent: '-20%',
                expressShip: true,
                brand: 'Davis (Mỹ)',
                price: 340000,
                rating: 4.9,
                reviews: 145,
                reviewsCount: 145,
                sold: 980,
                stockQ1: 22,
                stockBT: 18,
                stockQ7: 25,
                q1: 22, bt: 18, q7: 25,
                category: 'Phụ kiện & Vệ sinh',
                categoryAdmin: 'Phụ kiện & Vệ sinh',
                img: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=500&q=80',
                desc: 'Sữa tắm dược liệu đặc trị viêm da, nấm da, vi khuẩn và mùi hôi khó chịu trên chó mèo. Chứa hoạt chất Chlorhexidine Gluconate 4% được các bác sĩ da liễu thú y khuyên dùng.',
                description: 'Sữa tắm dược liệu đặc trị viêm da, nấm da, vi khuẩn.',
                ingredients: 'Chlorhexidine Gluconate 4.0%, chất tạo bọt dịu nhẹ từ dừa, tinh dầu dưỡng ẩm da.',
                usage: 'Làm ướt lông, thoa dầu tắm tạo bọt và xoa bóp đều trong 5-10 phút rồi xả sạch với nước.'
            },
            {
                id: 9,
                sku: 'PET-PK01',
                name: 'Balo Phi Thuyền Vận Chuyển Thú Cưng Thông Khí Đa Chiều VIP',
                variantConfig: null,
                variants: [],
                species: 'Mèo',
                productType: 'Phụ kiện & Đồ chơi',
                brandName: 'PetCare Pro',
                originalPrice: 650000,
                discountPercent: '-25%',
                expressShip: true,
                brand: 'PetCare Pro',
                price: 490000,
                rating: 4.7,
                reviews: 86,
                reviewsCount: 86,
                sold: 620,
                stockQ1: 15,
                stockBT: 10,
                stockQ7: 12,
                q1: 15, bt: 10, q7: 12,
                category: 'Phụ kiện & Vệ sinh',
                categoryAdmin: 'Phụ kiện & Vệ sinh',
                img: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=500&q=80',
                desc: 'Balo vận chuyển thú cưng cao cấp chất liệu nhựa ABS cứng cáp chống va đập, nắp trong suốt tầm nhìn rộng, hệ thống 9 lỗ thoáng khí và đệm lót êm ái cho bé dưới 8kg.',
                description: 'Balo vận chuyển thú cưng cao cấp chất liệu nhựa ABS cứng cáp.',
                ingredients: 'Nhựa ABS an toàn thực phẩm, vải Oxford 900D chống thấm, lưới thép không gỉ.',
                usage: 'Phù hợp khi chở bé đi tiêm phòng, du lịch hoặc dạo phố an toàn tuyệt đối.'
            },
            {
                id: 10,
                sku: 'PET-PK02',
                name: 'Trụ Cào Móng Cây Cat Tree 3 Tầng Kèm Nhà Cầu Ngủ Mèo',
                variantConfig: null,
                variants: [],
                species: 'Mèo',
                productType: 'Phụ kiện & Đồ chơi',
                brandName: 'CozyPet',
                originalPrice: 850000,
                discountPercent: '-20%',
                expressShip: true,
                brand: 'CozyPet',
                price: 680000,
                rating: 4.9,
                reviews: 64,
                reviewsCount: 64,
                sold: 410,
                stockQ1: 10,
                stockBT: 8,
                stockQ7: 14,
                q1: 10, bt: 8, q7: 14,
                category: 'Phụ kiện & Vệ sinh',
                categoryAdmin: 'Phụ kiện & Vệ sinh',
                img: 'https://images.unsplash.com/photo-1545249390-6bdfa286032f?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1545249390-6bdfa286032f?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1545249390-6bdfa286032f?auto=format&fit=crop&w=500&q=80',
                desc: 'Cây cào móng cao cấp quấn dây đay sisal tự nhiên bền chắc, khung gỗ ép công nghiệp chịu lực, bọc vải nhung mềm mịn giúp mèo xả stress và bảo vệ sofa nội thất gia đình.',
                description: 'Cây cào móng cao cấp quấn dây đay sisal tự nhiên bền chắc.',
                ingredients: 'Gỗ chịu lực MDF, dây thừng Sisal tự nhiên, vải nỉ lông cừu nhân tạo.',
                usage: 'Đặt tại góc phòng khách nơi mèo thường xuyên qua lại hoặc gần cửa sổ đón nắng.'
            },

            // Danh mục 3: Thuốc & Y tế (2 sản phẩm)
            {
                id: 11,
                sku: 'PET-MD01',
                name: 'Thuốc Trị Ve Rận & Tẩy Giun NexGard Spectra (Dạng Viên Nhai Thịt Bò)',
                variantConfig: null,
                variants: [],
                species: 'Chó',
                productType: 'Thuốc thú y',
                brandName: 'Boehringer Ingelheim',
                originalPrice: 580000,
                discountPercent: '-20%',
                expressShip: true,
                brand: 'Boehringer Ingelheim (Pháp)',
                price: 460000,
                rating: 5.0,
                reviews: 320,
                reviewsCount: 320,
                sold: 2100,
                stockQ1: 30,
                stockBT: 25,
                stockQ7: 35,
                q1: 30, bt: 25, q7: 35,
                category: 'Thuốc & Y tế',
                categoryAdmin: 'Thuốc & Y tế',
                img: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=500&q=80',
                desc: 'Viên nhai vị thịt bò thơm ngon bảo vệ toàn diện 1 tháng: tiêu diệt bọ chét, ve chó, ghẻ Demodex, phòng giun tim và tẩy sạch các loại giun đường ruột.',
                description: 'Viên nhai vị thịt bò thơm ngon bảo vệ toàn diện 1 tháng.',
                ingredients: 'Afoxolaner và Milbemycin Oxime tinh khiết chuẩn dược phẩm thú y quốc tế.',
                usage: 'Cho chó nhai trực tiếp như bánh thưởng. Dùng định kỳ 1 viên/tháng cho cún từ 8 tuần tuổi.'
            },
            {
                id: 12,
                sku: 'PET-MD02',
                name: 'Tuýp Nhỏ Gáy Phòng Trị Ký Sinh Trùng Toàn Diện Cho Mèo Revolution Plus',
                variantConfig: null,
                variants: [],
                species: 'Mèo',
                productType: 'Thuốc thú y',
                brandName: 'Zoetis',
                originalPrice: 480000,
                discountPercent: '-20%',
                expressShip: true,
                brand: 'Zoetis (Mỹ)',
                price: 385000,
                rating: 4.9,
                reviews: 198,
                reviewsCount: 198,
                sold: 1650,
                stockQ1: 38,
                stockBT: 28,
                stockQ7: 42,
                q1: 38, bt: 28, q7: 42,
                category: 'Thuốc & Y tế',
                categoryAdmin: 'Thuốc & Y tế',
                img: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=500&q=80', image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=500&q=80',
                desc: 'Dược chất thế hệ mới tiêu diệt 6 loại ký sinh trùng gây hại trên mèo: bọ chét, ấu trùng bọ chét, ve, rận tai, giun tim, giun đũa và giun móc chỉ với 1 giọt nhỏ gáy.',
                description: 'Dược chất thế hệ mới tiêu diệt 6 loại ký sinh trùng trên mèo.',
                ingredients: 'Selamectin và Sarolaner nồng độ cao an toàn cho mèo từ 8 tuần tuổi.',
                usage: 'Vạch lông sau gáy mèo và bóp hết tuýp thuốc trực tiếp lên da.'
            }
        ],

        // 12 DỊCH VỤ PHÂN LOẠI CHÍNH XÁC THEO 4 DANH MỤC YÊU CẦU
        services: [
            // Nhóm 1: Y Tế & Chăm Sóc Sức Khỏe (5 dịch vụ)
            {
                id: 1,
                name: 'Khám Sức Khỏe Tổng Quát & Tầm Soát Bệnh Lý Thú Cưng',
                price: 250000,
                duration: '45 - 60 phút',
                expert: 'ThS. Bác sĩ Thú y chuyên khoa Nội',
                doctor: 'ThS. BS Nguyễn Minh Quân',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def?auto=format&fit=crop&w=600&q=80',
                desc: 'Quy trình kiểm tra toàn diện 12 cơ quan trọng yếu: tim phổi, răng miệng, mắt tai, ổ bụng, xương khớp, huyết áp và kiểm tra ký sinh trùng da lông.',
                description: 'Quy trình kiểm tra toàn diện 12 cơ quan trọng yếu.',
                rating: 4.9,
                reviewsCount: 312,
                icon: 'fa-solid fa-stethoscope',
                tags: ['12 cơ quan', 'Khám lâm sàng', 'Sổ sức khỏe'],
                steps: [
                    { title: 'Thu thập tiền sử bệnh & cân đo chỉ số sinh tồn', desc: 'Đo thân nhiệt, huyết áp, cân nặng, nhịp tim và nghe phổi bằng ống nghe chuyên dụng.' },
                    { title: 'Khám lâm sàng chi tiết mắt - tai - miệng', desc: 'Nội soi ống tai, kiểm tra giác mạc và đánh giá mức độ vôi răng hay viêm nướu.' },
                    { title: 'Sờ nắn ổ bụng & kiểm tra hệ vận động khớp', desc: 'Đánh giá gan lách thận bàng quang và phản xạ các khớp xương chi.' },
                    { title: 'Soi tươi da lông kiểm tra nấm & ghẻ Demodex', desc: 'Lấy mẫu biểu bì kiểm tra dưới kính hiển vi quang học độ phóng đại lớn.' },
                    { title: 'Tư vấn phác đồ phòng bệnh & cấp sổ theo dõi', desc: 'Bác sĩ phân tích kết quả, lập phác đồ dinh dưỡng và chế độ tiêm phòng tối ưu.' }
                ]
            },
            {
                id: 2,
                name: 'Tiêm Chủng Vắc-xin Phòng Bệnh Đa Giá Nhập Khẩu (Chó & Mèo)',
                price: 220000,
                duration: '30 phút',
                expert: 'Bác sĩ Thú y chính quy',
                doctor: 'BS Trần Thu Hà',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80',
                desc: 'Tiêm phòng vắc-xin chính hãng (Nobivac, Zoetis) phòng 7 bệnh nguy hiểm trên chó và 4 bệnh trên mèo. Được lưu trữ trong hệ thống tủ lạnh bảo quản chuẩn GSP y tế.',
                description: 'Tiêm phòng vắc-xin chính hãng lưu trữ chuẩn GSP y tế.',
                rating: 5.0,
                reviewsCount: 450,
                icon: 'fa-solid fa-syringe',
                tags: ['Chuẩn GSP', 'Khám sàng lọc', 'Bảo hiểm phản vệ'],
                steps: [
                    { title: 'Khám sàng lọc trước tiêm', desc: 'Đo thân nhiệt và xác nhận thể trạng hoàn toàn khỏe mạnh, không sốt, không ủ bệnh.' },
                    { title: 'Kiểm tra tem mã lô & hạn sử dụng vắc-xin', desc: 'Khách hàng trực tiếp đối chiếu tem niêm phong và hạn sử dụng của lọ thuốc.' },
                    { title: 'Thực hiện tiêm dưới da chuẩn kỹ thuật không đau', desc: 'Sát khuẩn kỹ càng, sử dụng kim tiêm siêu nhỏ hạn chế tối đa cảm giác nhói.' },
                    { title: 'Theo dõi phản ứng sốc phản vệ 15 phút tại chỗ', desc: 'Bé được nghỉ ngơi tại phòng chờ có điều hòa và bác sĩ túc trực quan sát.' },
                    { title: 'Dán tem vào sổ tiêm & cài đặt lịch nhắc hẹn', desc: 'Cấp chứng nhận tiêm phòng và gửi tin nhắn SMS nhắc lịch tái chủng tự động.' }
                ]
            },
            {
                id: 3,
                name: 'Xét Nghiệm Máu Tổng Quát 18 Chỉ Số & Test Nhanh Bệnh Truyền Nhiễm',
                price: 380000,
                duration: '30 - 45 phút lấy kết quả ngay',
                expert: 'Kỹ thuật viên Xét nghiệm Y khoa',
                doctor: 'KTV Xét nghiệm Thú y',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=600&q=80',
                desc: 'Hệ thống máy xét nghiệm huyết học và sinh hóa tự động IDEXX (Mỹ) cho kết quả chính xác 99.9% chỉ trong 15 phút, phát hiện sớm suy thận, viêm tụy, Care, Parvo, FIP.',
                description: 'Máy xét nghiệm sinh hóa tự động IDEXX Mỹ lấy kết quả sau 15p.',
                rating: 4.9,
                reviewsCount: 188,
                icon: 'fa-solid fa-vial-virus',
                tags: ['Máy IDEXX Mỹ', '15 phút', 'Độ chính xác 99.9%'],
                steps: [
                    { title: 'Lấy mẫu máu tĩnh mạch êm ái', desc: 'Kỹ thuật viên thao tác chuẩn xác, lượng máu lấy rất nhỏ không gây mệt cho bé.' },
                    { title: 'Chạy máy huyết học tự động 18 chỉ số (CBC)', desc: 'Kiểm tra bạch cầu (nhiễm trùng), hồng cầu (thiếu máu), tiểu cầu.' },
                    { title: 'Đo sinh hóa chức năng gan, thận và đường huyết', desc: 'Đánh giá nồng độ men gan ALT, Creatinine, BUN, Glucose máu.' },
                    { title: 'Thực hiện test nhanh kháng nguyên bệnh truyền nhiễm', desc: 'Kit test chuyên biệt phát hiện virus Parvo, Care, Giảm bạch cầu (FPV).' },
                    { title: 'Bác sĩ giải thích tường tận từng chỉ số bất thường', desc: 'Đưa ra lời khuyên dinh dưỡng hoặc phác đồ can thiệp kịp thời.' }
                ]
            },
            {
                id: 4,
                name: 'Siêu Âm Màu 4D & Chụp X-Quang Kỹ Thuật Số (DR) Tận Nơi',
                price: 300000,
                duration: '40 phút',
                expert: 'Bác sĩ Chẩn đoán Hình ảnh Thú y',
                doctor: 'BS CĐHA Thú y',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80',
                desc: 'Máy siêu âm Doppler màu hiện đại chẩn đoán thai kỳ, sỏi bàng quang, khối u và máy X-quang kỹ thuật số liều phóng xạ thấp kiểm tra xương khớp.',
                description: 'Máy siêu âm Doppler màu hiện đại và X-quang kỹ thuật số.',
                rating: 4.8,
                reviewsCount: 142,
                icon: 'fa-solid fa-x-ray',
                tags: ['Doppler màu 4D', 'X-quang DR', 'Ảnh số qua App'],
                steps: [
                    { title: 'Chuẩn bị tư thế và cạo lông vùng kiểm tra', desc: 'Vệ sinh da và bôi gel siêu âm chuyên dụng không gây kích ứng.' },
                    { title: 'Quét siêu âm Doppler đánh giá chi tiết các tạng', desc: 'Đo kích thước tim thận, kiểm tra tuần hoàn máu và đếm số lượng thai nhi.' },
                    { title: 'Chụp phim X-quang các tư thế chuẩn', desc: 'Đánh giá dị vật đường tiêu hóa, gãy xương hoặc thoát vị đĩa đệm.' },
                    { title: 'Hội chẩn hình ảnh với bác sĩ chuyên khoa', desc: 'Phân tích bất thường và lập bản báo cáo chẩn đoán hình ảnh chuẩn xác.' },
                    { title: 'Trả file ảnh kỹ thuật số chất lượng cao qua App', desc: 'Khách hàng có thể lưu trữ và xem lại hình ảnh trên hồ sơ bệnh án điện tử.' }
                ]
            },
            {
                id: 5,
                name: 'Lấy Cao Răng Siêu Âm Không Đau & Đánh Bóng Men Răng',
                price: 320000,
                duration: '60 phút',
                expert: 'Bác sĩ Nha khoa Thú y',
                doctor: 'BS Nha khoa Thú y',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80',
                desc: 'Sử dụng đầu rung siêu âm tần số cao bóc tách nhẹ nhàng mảng bám vôi răng dưới nướu, chữa dứt điểm viêm lợi và mùi hôi miệng kéo dài.',
                description: 'Đầu rung siêu âm tần số cao bóc tách mảng bám không đau.',
                rating: 4.9,
                reviewsCount: 210,
                icon: 'fa-solid fa-tooth',
                tags: ['Sóng siêu âm', 'Đánh bóng men', 'Khử hôi miệng'],
                steps: [
                    { title: 'Thăm khám mức độ viêm nướu & tiền mê nhẹ', desc: 'Tiền mê an toàn bằng khí mê Isoflurane giúp bé nằm yên không lo sợ.' },
                    { title: 'Lấy mảng bám bằng máy siêu âm nước ấm', desc: 'Làm sạch triệt để từng kẽ răng và túi nha chu mà không mòn men răng.' },
                    { title: 'Đánh bóng bề mặt răng bằng paste nha khoa', desc: 'Tạo bề mặt nhẵn bóng ngăn ngừa thức ăn và vi khuẩn tái bám dính.' },
                    { title: 'Xịt gel kháng khuẩn sinh học thảo dược', desc: 'Làm dịu mô nướu, hỗ trợ tái tạo niêm mạc miệng tổn thương.' },
                    { title: 'Hướng dẫn chủ nuôi chăm sóc răng tại nhà', desc: 'Tư vấn loại gel đánh răng enzym và đồ gặm làm sạch mảng bám.' }
                ]
            },

            // Nhóm 2: Cấp Cứu & Điều Trị Chuyên Sâu (3 dịch vụ)
            {
                id: 6,
                name: 'Cấp Cứu Thú Y 24/7 & Hồi Sức Tích Cực (ICU)',
                price: 500000,
                duration: 'Phục vụ 24/24h',
                expert: 'Đội ngũ Bác sĩ Cấp cứu & Ngoại khoa thường trực',
                doctor: 'BS Đỗ Hoàng Nam (Đội trưởng ICU)',
                category: 'Cấp Cứu & Điều Trị Chuyên Sâu',
                img: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80',
                desc: 'Phòng cấp cứu vô trùng trang bị máy thở oxy cao áp, máy sốc tim, monitor theo dõi huyết động học và đội xe cấp cứu cơ động đón tận nhà bất kể ngày đêm.',
                description: 'Phòng cấp cứu vô trùng trang bị máy thở oxy cao áp 24/7.',
                rating: 5.0,
                reviewsCount: 165,
                icon: 'fa-solid fa-truck-medical',
                tags: ['Trực 24/7', 'Thở oxy cao áp', 'Monitor ICU'],
                steps: [
                    { title: 'Tiếp nhận khẩn cấp & phân loại bệnh tình (Triage)', desc: 'Xác định nhanh tình trạng suy hô hấp, xuất huyết, ngộ độc hay đa chấn thương.' },
                    { title: 'Thiết lập đường truyền tĩnh mạch & hỗ trợ oxy', desc: 'Đặt catheter ven ngay lập tức, truyền dịch cân bằng điện giải và thở oxy buồng kín.' },
                    { title: 'Xét nghiệm cấp cứu tại giường & Chụp X-quang/Siêu âm', desc: 'Đọc kết quả khí máu và hình ảnh chẩn đoán trong vòng 5-10 phút.' },
                    { title: 'Phẫu thuật khẩn cấp hoặc điều trị nội trú ICU', desc: 'Chuyển thẳng vào phòng mổ áp lực dương hoặc lồng hồi sức kiểm soát nhiệt ẩm.' },
                    { title: 'Báo cáo diễn tiến sức khỏe liên tục cho gia đình', desc: 'Cập nhật tình trạng qua Zalo/Camera giám sát lồng bệnh 24/24.' }
                ]
            },
            {
                id: 7,
                name: 'Phẫu Thuật Triệt Sản Nội Soi An Toàn Vi Phẫu (Chó & Mèo)',
                price: 650000,
                duration: '120 phút',
                expert: 'Bác sĩ Ngoại khoa trưởng ca',
                doctor: 'BS Ngoại khoa Thú y',
                category: 'Cấp Cứu & Điều Trị Chuyên Sâu',
                img: 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80',
                desc: 'Phương pháp vi phẫu đường mổ siêu nhỏ (dưới 1cm) hạn chế đau đớn, không chảy máu, khâu thẩm mỹ chỉ tự tiêu không cần quay lại cắt chỉ.',
                description: 'Phương pháp vi phẫu đường mổ siêu nhỏ chỉ tự tiêu.',
                rating: 5.0,
                reviewsCount: 280,
                icon: 'fa-solid fa-kit-medical',
                tags: ['Vi phẫu < 1cm', 'Chỉ tự tiêu', 'Gây mê Isoflurane'],
                steps: [
                    { title: 'Xét nghiệm máu kiểm tra đông máu & chức năng gan thận', desc: 'Đảm bảo bé đủ điều kiện chịu mê an toàn tuyệt đối 100%.' },
                    { title: 'Gây mê đa mô thức bằng máy thở Isoflurane hiện đại', desc: 'Theo dõi nhịp tim, nồng độ oxy trong máu liên tục suốt ca mổ.' },
                    { title: 'Tiến hành phẫu thuật trong phòng vô trùng tuyệt đối', desc: 'Dụng cụ tiệt trùng Autoclave, bác sĩ phẫu thuật mặc áo vô khuẩn.' },
                    { title: 'Khâu chỉ thẩm mỹ tự tiêu giấu vết mổ', desc: 'Không để lại vết sẹo lồi, thú cưng không cần đeo vòng chống liếm quá lâu.' },
                    { title: 'Hồi tỉnh tại phòng chăm sóc hậu phẫu êm dịu', desc: 'Tiêm thuốc giảm đau 24h và cấp thuốc uống chống viêm tại nhà.' }
                ]
            },
            {
                id: 8,
                name: 'Vật Lý Trị Liệu & Phục Hồi Chức Năng Cột Sống - Khớp',
                price: 300000,
                duration: '60 phút',
                expert: 'Bác sĩ Phục hồi Chức năng Thú y',
                doctor: 'BS PHCN Thú y',
                category: 'Cấp Cứu & Điều Trị Chuyên Sâu',
                img: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                desc: 'Liệu trình vật lý trị liệu laser giảm đau sâu, thủy trị liệu bồn bơi nước ấm và châm cứu phục hồi phản xạ thần kinh cho các bé bị liệt 2 chân sau, thoái hóa khớp.',
                description: 'Laser giảm đau sâu, thủy trị liệu và châm cứu phục hồi khớp.',
                rating: 4.8,
                reviewsCount: 95,
                icon: 'fa-solid fa-bone',
                tags: ['Laser trị liệu', 'Thủy trị liệu', 'Phục hồi khớp'],
                steps: [
                    { title: 'Đánh giá thang điểm đau & mức độ vận động', desc: 'Kiểm tra phản xạ cơ bắp, độ co duỗi khớp và mức độ tổn thương thần kinh.' },
                    { title: 'Chiếu tia Laser cường độ thấp giảm viêm sâu', desc: 'Tăng cường tuần hoàn máu nuôi dưỡng mô sụn và cắt đứt cơn đau cơ.' },
                    { title: 'Thủy trị liệu (Hydrotherapy) trên máy chạy bộ dưới nước', desc: 'Nước nâng đỡ trọng lượng cơ thể giúp bé tập bước đi mà không áp lực lên xương.' },
                    { title: 'Xoa bóp nắn chỉnh cơ và kéo giãn nhẹ nhàng', desc: 'Chống teo cơ, duy trì độ dẻo dai của gân dây chằng.' },
                    { title: 'Bài tập phục hồi tại nhà cùng chủ nuôi', desc: 'Hướng dẫn các động tác mát-xa và dụng cụ hỗ trợ xe lăn nếu cần thiết.' }
                ]
            },

            // Nhóm 3: Spa & Làm Đẹp (2 dịch vụ)
            {
                id: 9,
                name: 'Gói Spa & Grooming Cắt Tỉa Lông Tạo Kiểu Toàn Diện',
                price: 350000,
                duration: '120 - 150 phút',
                expert: 'Master Groomer & Kỹ thuật viên cao cấp',
                doctor: 'Master Groomer & KTV cao cấp',
                category: 'Spa & Làm Đẹp',
                img: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80',
                desc: 'Gói chăm sóc sắc đẹp đẳng cấp nhất cho bé cưng: tắm sục ozone thải độc da, sấy chải bông phồng, cắt móng mài góc tròn, vệ sinh nhổ lông tai và cắt tỉa lông tạo kiểu theo chuẩn dáng giống loài.',
                description: 'Gói chăm sóc sắc đẹp đẳng cấp nhất cho bé cưng.',
                rating: 5.0,
                reviewsCount: 520,
                icon: 'fa-solid fa-scissors',
                tags: ['Chuẩn 5 bước', 'Bồn sục Ozone', 'Tạo kiểu dáng chuẩn'],
                steps: [
                    { title: 'Kiểm tra da lông & tư vấn form dáng', desc: 'Kiểm tra tình trạng búi lông, ve rận, nấm và tư vấn dáng cắt tỉa phù hợp.' },
                    { title: 'Vệ sinh sơ bộ chuyên sâu', desc: 'Cắt mài móng không chảy máu, nhổ sạch lông tai, cạo lông đệm chân và vệ sinh hậu môn.' },
                    { title: 'Tắm bồn sục Ozone thư giãn 2 lần', desc: 'Dùng dầu gội hữu cơ nhập khẩu khử mùi, massage giải tỏa căng thẳng và ủ xả phục hồi lông.' },
                    { title: 'Sấy ion âm & chải tơi lông chuyên nghiệp', desc: 'Sấy gió ấm bảo vệ da, chải gỡ rối hoàn toàn và đánh bông lớp lông lót.' },
                    { title: 'Cắt tỉa tạo kiểu nghệ thuật & xịt tinh dầu', desc: 'Master Groomer tỉa thủ công từng góc cạnh sắc sảo và xịt tinh dầu dưỡng lông.' }
                ]
            },
            {
                id: 10,
                name: 'Tắm Trị Liệu Trị Nấm & Viêm Da Chuyên Sâu Bằng Dược Thảo',
                price: 280000,
                duration: '90 phút',
                expert: 'Kỹ thuật viên Da liễu Thú y',
                doctor: 'KTV Da liễu Thú y',
                category: 'Spa & Làm Đẹp',
                img: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=600&q=80',
                desc: 'Phác đồ điều trị dứt điểm các bệnh lý da liễu: nấm Microsporum, viêm da Demodex, viêm nang lông có mủ và vảy gàu ngứa ngáy dữ dội.',
                description: 'Phác đồ điều trị dứt điểm các bệnh lý da liễu và nấm ngứa.',
                rating: 4.9,
                reviewsCount: 175,
                icon: 'fa-solid fa-shower',
                tags: ['Davis 4%', 'Giảm ngứa tức thì', 'Diệt bào tử nấm'],
                steps: [
                    { title: 'Cạo sạch vùng lông tổn thương khu trú', desc: 'Tạo sự thông thoáng để thuốc tiếp xúc trực tiếp vào ổ nấm/vi khuẩn.' },
                    { title: 'Tắm xả bằng nước ấm ion hóa loại bỏ tế bào chết', desc: 'Làm mềm vảy gàu và rửa trôi chất nhờn tích tụ trên bề mặt da.' },
                    { title: 'Ủ dầu tắm dược liệu trị nấm Davis Chlorhexidine 15 phút', desc: 'Hoạt chất thấm sâu tiêu diệt bào tử nấm và vi khuẩn gây mủ.' },
                    { title: 'Ngâm bồn thảo dược phục hồi hàng rào bảo vệ da', desc: 'Chiết xuất yến mạch và tràm trà giúp giảm ngứa tức thì.' },
                    { title: 'Sấy khô bằng lồng sấy gió nhẹ & xịt dưỡng ẩm', desc: 'Không làm khô rát da, phục hồi nang lông mọc lại nhanh chóng.' }
                ]
            },

            // Nhóm 4: Lưu Trú & Tiện Ích (2 dịch vụ)
            {
                id: 11,
                name: 'Khách Sạn Thú Cưng Pet Hotel Đẳng Cấp 5 Sao (Có Camera 24/7)',
                price: 200000,
                duration: 'Tính theo ngày (24 giờ)',
                expert: 'Quản gia thú cưng & Bác sĩ túc trực',
                doctor: 'KTV Quản gia Pet Hotel',
                category: 'Lưu Trú & Tiện Ích',
                img: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=600&q=80',
                desc: 'Phòng lưu trú riêng biệt máy lạnh 24/7, lọc không khí ion âm diệt khuẩn. Khách hàng có tài khoản xem camera riêng của phòng bé bất kỳ lúc nào.',
                description: 'Phòng lưu trú riêng biệt máy lạnh 24/7 kèm camera xem trực tiếp.',
                rating: 4.9,
                reviewsCount: 340,
                icon: 'fa-solid fa-hotel',
                tags: ['Camera 24/7', 'Điều hòa riêng', 'Dinh dưỡng 3 bữa'],
                steps: [
                    { title: 'Tiếp nhận & kiểm tra sức khỏe ban đầu', desc: 'Xác nhận sổ tiêm ngừa, kiểm tra ve rận và lập thực đơn ăn uống theo thói quen của bé.' },
                    { title: 'Nhận phòng VIP riêng biệt khử khuẩn bằng tia UV', desc: 'Trang bị nệm êm ái, khay cát riêng biệt và đồ chơi yêu thích.' },
                    { title: 'Chế độ dinh dưỡng 3 bữa tiêu chuẩn quốc tế', desc: 'Phục vụ hạt cao cấp Royal Canin/Orijen kèm pate tươi nấu trong ngày.' },
                    { title: 'Giờ vận động vui chơi sân vườn 2 lần/ngày', desc: 'Nhân viên dắt bé dạo chơi và tương tác tại khu vận động trong nhà sạch sẽ.' },
                    { title: 'Báo cáo video & nhật ký chăm sóc hàng ngày', desc: 'Gửi clip ăn uống, sinh hoạt và tặng gói tắm sấy trước khi check-out đón về.' }
                ]
            },
            {
                id: 12,
                name: 'Đưa Đón Thú Cưng Khám Bệnh & Spa Tận Cửa Bằng Xe Chuyên Dụng (Pet Taxi)',
                price: 150000,
                duration: 'Theo lịch hẹn khách đặt',
                expert: 'Tài xế chuyên trách & Nhân viên an toàn thú cưng',
                doctor: 'Đội xe Pet Taxi Cơ Động',
                category: 'Lưu Trú & Tiện Ích',
                img: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=600&q=80', image: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=600&q=80',
                desc: 'Xe ô tô cứu thương & đưa đón thú cưng chuyên dụng, khoang xe rộng rãi có điều hòa mát lạnh, lồng vận chuyển êm ái, dây an toàn chuyên dụng và tài xế am hiểu tâm lý động vật.',
                description: 'Xe ô tô chuyên dụng đưa đón thú cưng tận nhà an toàn chu đáo.',
                rating: 4.8,
                reviewsCount: 160,
                icon: 'fa-solid fa-taxi',
                tags: ['Đón tận cửa', 'Lồng chuyên dụng', 'Bật nhạc thiền thư giãn'],
                steps: [
                    { title: 'Nhận lịch hẹn & xác nhận địa chỉ đón trả', desc: 'Hệ thống gửi định vị xe và thời gian tài xế có mặt chuẩn xác từng phút.' },
                    { title: 'Đón bé tận cửa và kiểm tra dây đeo an toàn', desc: 'Nhân viên đưa bé vào lồng vận chuyển chuyên dụng êm ái và sạch sẽ.' },
                    { title: 'Di chuyển êm ái với điều hòa khoang riêng', desc: 'Bật nhạc thiền tần số thấp giúp thú cưng thư giãn, không bị say xe.' },
                    { title: 'Bàn giao trực tiếp cho Bác sĩ / Groomer tại viện', desc: 'Gửi video check-in khi bé đã đến nơi an toàn để phụ huynh an tâm.' },
                    { title: 'Đưa bé về tận nhà sau khi hoàn thành dịch vụ', desc: 'Bàn giao kèm sổ sức khỏe, quà tặng và dặn dò của bác sĩ.' }
                ]
            }
        ],
        get servicesList() { return this.services; },
        set servicesList(val) { this.services = val; },

        // 6 Bài viết PetShare360 do Admin đăng tải
        articles: [
            {
                id: 1,
                title: 'Cẩm Nang Dinh Dưỡng Vàng Cho Cún Con Từ 2 Đến 6 Tháng Tuổi',
                author: 'ThS.BS Nguyễn Minh Quân (Viện Trưởng PetCare360)',
                date: '18/10/2026',
                category: 'Dinh dưỡng thú cưng',
                views: 2450,
                likes: 318,
                image: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                summary: 'Giai đoạn 2-6 tháng tuổi là "thời kỳ vàng" để hoàn thiện khung xương, hệ miễn dịch và phát triển não bộ của cún con. Một chế độ ăn sai lầm có thể dẫn đến dị tật xương suốt đời.',
                content: `
                    <p class="lead font-medium text-slate-700">Trong giai đoạn từ 2 đến 6 tháng tuổi, tốc độ phát triển thể chất của cún con diễn ra nhanh gấp 12 lần so với con người. Đây chính là lúc cơ thể bé cần nguồn năng lượng, canxi và kháng thể tối ưu nhất.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Tỷ lệ dinh dưỡng chuẩn cho cún con đang lớn</h4>
                    <p>Khẩu phần ăn của cún con cần đạt hàm lượng protein thô từ 28% - 32% (nguồn protein dễ hấp thu từ thịt gà, cá hồi hoặc trứng gà), chất béo tốt từ 14% - 18% và tỷ lệ Canxi : Photpho lý tưởng là 1.2 : 1.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Số bữa ăn và lượng thức ăn theo từng tháng tuổi</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>Từ 2 - 3 tháng tuổi:</strong> Chia làm 4 bữa nhỏ mỗi ngày. Ngâm mềm với sữa dinh dưỡng KMR.</li>
                        <li><strong>Từ 4 - 6 tháng tuổi:</strong> Giảm xuống 3 bữa/ngày, tập cho bé ăn hạt khô nguyên hạt để sạch răng.</li>
                    </ul>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">3. Những thực phẩm TUYỆT ĐỐI CẤM kỵ</h4>
                    <p class="text-rose-600 font-semibold">Sô cô la, hành tỏi, nho tươi/nho khô, xương ống động vật đã nấu chín và chất ngọt nhân tạo Xylitol.</p>
                `
            },
            {
                id: 2,
                title: 'Nhận Biết Dấu Hiệu Trầm Cảm & Căng Thẳng Ở Mèo Nuôi Trong Nhà',
                author: 'BS Trần Thu Hà (Chuyên gia Hành vi Động vật)',
                date: '15/10/2026',
                category: 'Hành vi & Tâm lý',
                views: 1890,
                likes: 245,
                image: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=600&q=80',
                summary: 'Mèo là bậc thầy giấu giếm cảm xúc và cơn đau. Nếu không chú ý các biểu hiện tinh tế, chủ nuôi có thể bỏ qua tình trạng stress nặng dẫn đến chứng viêm bàng quang vô căn nguy hiểm.',
                content: `
                    <p class="lead font-medium text-slate-700">Nhiều người nghĩ rằng mèo sống trong nhà kín là hoàn toàn an toàn và thoải mái. Tuy nhiên, sự nhàm chán hoặc thiếu không gian vận động theo chiều dọc có thể khiến mèo bị căng thẳng trầm trọng.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Các dấu hiệu cảnh báo mèo đang stress</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>Liếm lông quá mức:</strong> Bé liếm đến mức rụng trụi lông ở bụng hoặc mặt trong hai chân sau.</li>
                        <li><strong>Đi vệ sinh ngoài khay:</strong> Tiểu bậy lên giường, ghế sofa hoặc góc tường dù trước đó dùng khay ngoan.</li>
                        <li><strong>Thay đổi thói quen ăn uống:</strong> Bỏ ăn hoặc ăn ít hơn 50% khẩu phần bình thường.</li>
                        <li><strong>Thu mình trốn tránh:</strong> Trốn dưới gầm giường, gừ khè khi vuốt ve.</li>
                    </ul>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Giải pháp giải tỏa căng thẳng hiệu quả</h4>
                    <p>Bổ sung thêm trụ cào móng cây cao cạnh cửa sổ, dành 15-20 phút chơi đùa cần câu lông vũ mỗi ngày và xịt pheromone làm dịu (Feliway).</p>
                `
            },
            {
                id: 3,
                title: 'Lịch Tiêm Phòng Vắc-xin & Tẩy Giun Định Kỳ Chuẩn Y Khoa 2026',
                author: 'ThS.BS Nguyễn Minh Quân (Viện Trưởng PetCare360)',
                date: '12/10/2026',
                category: 'Y tế & Phòng bệnh',
                views: 3120,
                likes: 480,
                image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80',
                summary: 'Tiêm chủng đầy đủ là bức tường thành vững chắc nhất bảo vệ thú cưng trước những dịch bệnh truyền nhiễm nguy hiểm gây tử vong cao như Parvovirus, Care hay Dại.',
                content: `
                    <p class="lead font-medium text-slate-700">Rất nhiều chủ nuôi thắc mắc tại sao cún mèo đã tiêm 1 mũi vẫn bị mắc bệnh. Nguyên nhân chính là do chưa hoàn thành đủ phác đồ mũi tiêm cơ sở để hình thành nồng độ kháng thể bảo hộ.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Lịch tiêm chuẩn cho Chó con</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>6 - 8 tuần tuổi:</strong> Mũi 1 - Vắc-xin phòng 5 bệnh.</li>
                        <li><strong>10 - 12 tuần tuổi:</strong> Mũi 2 - Vắc-xin phòng 7 bệnh.</li>
                        <li><strong>14 - 16 tuần tuổi:</strong> Mũi 3 - Vắc-xin 7 bệnh nhắc lại + Vắc-xin Dại (bắt buộc).</li>
                        <li><strong>Định kỳ hàng năm:</strong> Nhắc lại 01 mũi 7 bệnh và 01 mũi Dại mỗi 12 tháng.</li>
                    </ul>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Lịch tiêm chuẩn cho Mèo</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>8 tuần tuổi:</strong> Mũi 1 - Vắc-xin 4 bệnh mèo.</li>
                        <li><strong>12 tuần tuổi:</strong> Mũi 2 - Vắc-xin 4 bệnh nhắc lại + Vắc-xin Dại.</li>
                        <li><strong>Định kỳ hàng năm:</strong> Nhắc lại 01 mũi 4 bệnh và 01 mũi Dại.</li>
                    </ul>
                `
            },
            {
                id: 4,
                title: 'Kỹ Thuật Chăm Sóc Lông Chống Vón Cục & Bệnh Nấm Da Vào Mùa Mưa',
                author: 'Master Groomer Lê Thanh Hằng',
                date: '08/10/2026',
                category: 'Spa & Chăm sóc lông',
                views: 1640,
                likes: 198,
                image: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80',
                summary: 'Độ ẩm không khí tăng cao vào mùa mưa là điều kiện thuận lợi nhất để vi nấm và vi khuẩn sinh sôi, gây ngứa ngáy dữ dội và vón rối lông ở các giống chó lông dài như Poodle, Corgi, Samoyed.',
                content: `
                    <p class="lead font-medium text-slate-700">Khi lông bị ẩm ướt kết hợp với bụi bẩn, các sợi lông sẽ bện chặt lại tạo thành các búi lông rối sát da. Dưới lớp búi lông này, da bị bí khí, ẩm mốc và phát sinh nấm da rất nhanh chóng.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Nguyên tắc sấy khô tuyệt đối sau khi dạo mưa</h4>
                    <p>Mỗi khi bé đi dạo dính mưa về, phải lau sạch 4 bàn chân bằng khăn khô và dùng máy sấy ấm sấy kỹ phần đệm chân, bụng và nách. Tuyệt đối không để lông tự khô tự nhiên.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Cách chải lông đúng kỹ thuật</h4>
                    <p>Dùng lược ghim (Slicker Brush) chải từng lớp lông mỏng từ trong chân lông ra ngoài. Dùng xịt gỡ rối chuyên dụng trước khi chải để không làm rách da bé.</p>
                `
            },
            {
                id: 5,
                title: 'Sơ Cứu Khẩn Cấp Tại Nhà Khi Thú Cưng Bị Hóc Dị Vật Hoặc Ngộ Độc',
                author: 'BS Đỗ Hoàng Nam (Đội Trưởng Cấp Cứu 24/7)',
                date: '03/10/2026',
                category: 'Cấp cứu & An toàn',
                views: 2980,
                likes: 512,
                image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80',
                summary: 'Thời gian vàng cứu sống thú cưng khi bị tắc nghẽn đường thở chỉ tính bằng vài phút. Hãy ghi nhớ thủ thuật Heimlich dành riêng cho thú cưng để xử trí kịp thời trước khi đến bệnh viện.',
                content: `
                    <p class="lead font-medium text-slate-700">Thú cưng thường có thói quen gặm nhấm đồ chơi nhỏ, xương hoặc tò mò liếm phải hóa chất lau sàn. Biết cách xử lý sơ cứu tại chỗ sẽ quyết định tính mạng của bé.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Thủ thuật Heimlich khi thú cưng bị hóc dị vật khó thở</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>Dành cho cún/mèo nhỏ:</strong> Bế bé dốc đầu xuống 45 độ, dùng lòng bàn tay vỗ dứt khoát 4-5 lần vào giữa hai xương bả vai.</li>
                        <li><strong>Dành cho cún lớn:</strong> Ôm vòng qua eo, nắm một tay thành nắm đấm đặt ngay dưới xương sườn (vùng cơ hoành), ép chặt và giật mạnh hướng lên trên ngực.</li>
                    </ul>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Khi nghi ngờ bé ngộ độc hóa chất</h4>
                    <p class="text-rose-600 font-semibold">GỌI NGAY HOTLINE CẤP CỨU 24/7 (1900 6868). Giữ lại bao bì hóa chất mang theo, KHÔNG tự ý gây nôn nếu bé đã bất tỉnh.</p>
                `
            },
            {
                id: 6,
                title: 'Hướng Dẫn Huấn Luyện Cún Đi Vệ Sinh Đúng Chỗ Trong Vòng 7 Ngày',
                author: 'HLV Huỳnh Anh Tuấn (Trung Tâm Huấn Luyện K9)',
                date: '28/09/2026',
                category: 'Huấn luyện & Kỹ năng',
                views: 2150,
                likes: 367,
                image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80',
                summary: 'Bí quyết dạy cún đi vệ sinh đúng khay vệ sinh hoặc bồn cầu cực kỳ nhẹ nhàng bằng phương pháp củng cố tích cực (Positive Reinforcement), tuyệt đối không la mắng hay đánh đập.',
                content: `
                    <p class="lead font-medium text-slate-700">Nhiều người có thói quen dí mũi cún vào bãi tiểu khi bé đi sai chỗ để trừng phạt. Hành động này hoàn toàn sai khoa học và chỉ khiến cún sợ hãi, lén lút đi vệ sinh vào góc khuất.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Bắt trúng "khung giờ vàng" đi vệ sinh của cún</h4>
                    <p>Cún có nhu cầu đi vệ sinh vào 3 thời điểm: Ngay sau khi ngủ dậy, trong vòng 15-20 phút sau khi ăn no, và sau khi nô đùa mệt mỏi.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Các bước thực hiện trong 7 ngày</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>Bước 1:</strong> Bố trí khay cố định, thấm một chút nước tiểu của bé vào tấm lót tạo mùi quen thuộc.</li>
                        <li><strong>Bước 2:</strong> Vào thời điểm vàng, dẫn cún đến khay với khẩu lệnh ngắn ("Đi tè đi").</li>
                        <li><strong>Bước 3:</strong> Khen thưởng tức thì! Thưởng ngay 1 viên bánh thưởng thơm ngon khi bé đi đúng chỗ.</li>
                    </ul>
                `
            }
        ],
        get petshareArticles() { return this.articles; },
        set petshareArticles(val) { this.articles = val; },

        // 5 Câu hỏi FAQ chi tiết
        faqs: [
            {
                q: 'Quy trình đặt lịch dịch vụ tại PetCare360 diễn ra như thế nào và tôi có thể hủy hoặc đổi giờ hẹn không?',
                question: 'Quy trình đặt lịch dịch vụ tại PetCare360 diễn ra như thế nào và tôi có thể hủy hoặc đổi giờ hẹn không?',
                a: 'Quý khách có thể dễ dàng đặt lịch trực tuyến ngay trên WebApp PetCare360: chọn dịch vụ mong muốn, chọn bé cưng, ngày và khung giờ thuận tiện. Hệ thống sẽ lập tức gửi xác nhận qua SMS và phân bổ phòng dịch vụ vô khuẩn cùng bác sĩ chuyên trách. Trong trường hợp có việc bận đột xuất, quý khách hoàn toàn có thể đổi giờ hoặc hủy lịch hẹn trước ít nhất 02 giờ mà không mất bất kỳ chi phí nào.',
                answer: 'Quý khách có thể dễ dàng đặt lịch trực tuyến ngay trên WebApp PetCare360: chọn dịch vụ mong muốn, chọn bé cưng, ngày và khung giờ thuận tiện. Hệ thống sẽ lập tức gửi xác nhận qua SMS và phân bổ phòng dịch vụ vô khuẩn cùng bác sĩ chuyên trách. Trong trường hợp có việc bận đột xuất, quý khách hoàn toàn có thể đổi giờ hoặc hủy lịch hẹn trước ít nhất 02 giờ mà không mất bất kỳ chi phí nào.'
            },
            {
                q: 'Các bé cưng có biểu hiện hung dữ hoặc quá sợ hãi thì PetCare360 có nhận dịch vụ Spa và khám chữa bệnh không?',
                question: 'Các bé cưng có biểu hiện hung dữ hoặc quá sợ hãi thì PetCare360 có nhận dịch vụ Spa và khám chữa bệnh không?',
                a: 'PetCare360 hoàn toàn có năng lực tiếp nhận các bé có tâm lý nhạy cảm, sợ hãi hoặc phòng thủ cao. Đội ngũ bác sĩ và chuyên viên Spa tại PetCare360 đều được đào tạo bài bản chứng chỉ Fear Free quốc tế (chăm sóc không sang chấn tâm lý). Chúng tôi áp dụng kỹ thuật xoa bóp trấn an, sử dụng pheromone làm dịu và bánh thưởng chuyên dụng. Trong trường hợp bắt buộc phải can thiệp y tế khẩn cấp, bác sĩ sẽ tư vấn tiền mê nhẹ an toàn để bé không phải trải qua hoảng loạn.',
                answer: 'PetCare360 hoàn toàn có năng lực tiếp nhận các bé có tâm lý nhạy cảm, sợ hãi hoặc phòng thủ cao. Đội ngũ bác sĩ và chuyên viên Spa tại PetCare360 đều được đào tạo bài bản chứng chỉ Fear Free quốc tế (chăm sóc không sang chấn tâm lý). Chúng tôi áp dụng kỹ thuật xoa bóp trấn an, sử dụng pheromone làm dịu và bánh thưởng chuyên dụng. Trong trường hợp bắt buộc phải can thiệp y tế khẩn cấp, bác sĩ sẽ tư vấn tiền mê nhẹ an toàn để bé không phải trải qua hoảng loạn.'
            },
            {
                q: 'Chính sách bảo hành y tế và cam kết an toàn khi gửi thú cưng tại khách sạn Pet Hotel như thế nào?',
                question: 'Chính sách bảo hành y tế và cam kết an toàn khi gửi thú cưng tại khách sạn Pet Hotel như thế nào?',
                a: 'Mọi thú cưng khi lưu trú tại Pet Hotel đều được kiểm tra sức khỏe ban đầu miễn phí, ở phòng riêng biệt có điều hòa 24/7 và camera giám sát trực tiếp. PetCare360 cam kết bảo hiểm sức khỏe 100% trong suốt thời gian lưu trú: nếu bé có bất kỳ dấu hiệu bỏ ăn hay mệt mỏi, bác sĩ thú y sẽ thăm khám và chăm sóc ngay lập tức với sự đồng ý của phụ huynh mà không phát sinh phụ phí khám.',
                answer: 'Mọi thú cưng khi lưu trú tại Pet Hotel đều được kiểm tra sức khỏe ban đầu miễn phí, ở phòng riêng biệt có điều hòa 24/7 và camera giám sát trực tiếp. PetCare360 cam kết bảo hiểm sức khỏe 100% trong suốt thời gian lưu trú: nếu bé có bất kỳ dấu hiệu bỏ ăn hay mệt mỏi, bác sĩ thú y sẽ thăm khám và chăm sóc ngay lập tức với sự đồng ý của phụ huynh mà không phát sinh phụ phí khám.'
            },
            {
                q: 'Sản phẩm thức ăn và thuốc thú y trên hệ thống PetCare360 có đảm bảo chính hãng và nguồn gốc rõ ràng không?',
                question: 'Sản phẩm thức ăn và thuốc thú y trên hệ thống PetCare360 có đảm bảo chính hãng và nguồn gốc rõ ràng không?',
                a: '100% sản phẩm trên PetCare360 (từ hạt khô, pate dinh dưỡng đến thuốc thú y đặc trị) đều được nhập khẩu chính ngạch từ các tập đoàn thú y hàng đầu thế giới như Royal Canin (Pháp), Orijen (Canada), Zoetis (Mỹ), Boehringer Ingelheim (Đức). Mỗi sản phẩm đều có đầy đủ hóa đơn VAT, tem phụ tiếng Việt, mã vạch truy xuất nguồn gốc và hạn sử dụng dài hạn. Chúng tôi cam kết đền bù gấp 10 lần nếu phát hiện hàng giả, hàng nhái.',
                answer: '100% sản phẩm trên PetCare360 (từ hạt khô, pate dinh dưỡng đến thuốc thú y đặc trị) đều được nhập khẩu chính ngạch từ các tập đoàn thú y hàng đầu thế giới như Royal Canin (Pháp), Orijen (Canada), Zoetis (Mỹ), Boehringer Ingelheim (Đức). Mỗi sản phẩm đều có đầy đủ hóa đơn VAT, tem phụ tiếng Việt, mã vạch truy xuất nguồn gốc và hạn sử dụng dài hạn. Chúng tôi cam kết đền bù gấp 10 lần nếu phát hiện hàng giả, hàng nhái.'
            },
            {
                q: 'Tôi ở xa hoặc vào ban đêm khi phòng khám đóng cửa, nếu thú cưng gặp tình trạng khẩn cấp thì phải làm sao?',
                question: 'Tôi ở xa hoặc vào ban đêm khi phòng khám đóng cửa, nếu thú cưng gặp tình trạng khẩn cấp thì phải làm sao?',
                a: 'PetCare360 duy trì hệ thống Cấp cứu Thú y 24/7/365 và tổng đài Bác sĩ trực tuyến miễn phí (1900 6868). Quý khách chỉ cần nhấn nút "Chat" trên góc phải màn hình WebApp hoặc gọi hotline cấp cứu, bác sĩ chuyên khoa hồi sức sẽ hướng dẫn sơ cứu tức thì qua video call và điều động xe cứu thương Pet Ambulance chuyên dụng đến tận nơi đón bé trong vòng 15-30 phút.',
                answer: 'PetCare360 duy trì hệ thống Cấp cứu Thú y 24/7/365 và tổng đài Bác sĩ trực tuyến miễn phí (1900 6868). Quý khách chỉ cần nhấn nút "Chat" trên góc phải màn hình WebApp hoặc gọi hotline cấp cứu, bác sĩ chuyên khoa hồi sức sẽ hướng dẫn sơ cứu tức thì qua video call và điều động xe cứu thương Pet Ambulance chuyên dụng đến tận nơi đón bé trong vòng 15-30 phút.'
            }
        ],
        faqActive: 0,
        get faqList() { return this.faqs; },
        set faqList(val) { this.faqs = val; },

        // 8 Lịch hẹn Admin phong phú
        appointments: [
            {
                id: 'APT-1089',
                customerName: 'Nguyễn Phương Thảo',
                customerPhone: '0988 123 456',
                petName: 'Bơ (Butter)',
                petType: 'Cún Corgi',
                serviceName: 'Gói Spa & Grooming Cắt Tỉa Lông Tạo Kiểu Toàn Diện',
                date: '2026-10-21',
                time: '09:30',
                branch: 'Chi nhánh Quận 7',
                status: 'Đã đặt hẹn',
                notes: 'Bé sợ tiếng sấy to, cần vệ sinh kẽ ngón chân cẩn thận do vừa mới khỏi viêm da.'
            },
            {
                id: 'APT-1088',
                customerName: 'Trần Văn Hoàng',
                customerPhone: '0912 345 678',
                petName: 'Kem Mút',
                petType: 'Mèo ALN',
                serviceName: 'Khám Sức Khỏe Tổng Quát & Tầm Soát Bệnh Lý Thú Cưng',
                date: '2026-10-21',
                time: '10:30',
                branch: 'Chi nhánh Cầu Giấy',
                status: 'Đang tiếp khách',
                notes: 'Bé có dấu hiệu uống nhiều nước hơn bình thường, nhờ bác sĩ kiểm tra chức năng thận.'
            },
            {
                id: 'APT-1087',
                customerName: 'Lê Thị Mai',
                customerPhone: '0977 888 999',
                petName: 'Lu Lu',
                petType: 'Cún Poodle',
                serviceName: 'Tiêm Chủng Vắc-xin Phòng Bệnh Đa Giá Nhập Khẩu',
                date: '2026-10-20',
                time: '14:00',
                branch: 'Chi nhánh Bình Thạnh',
                status: 'Hoàn thành',
                notes: 'Tiêm mũi nhắc lại hàng năm, kiểm tra mắt có ghèn.'
            },
            {
                id: 'APT-1086',
                customerName: 'Phạm Quốc Bảo',
                customerPhone: '0903 555 777',
                petName: 'Miu Miu',
                petType: 'Mèo Ba Tư',
                serviceName: 'Lấy Cao Răng Siêu Âm Không Đau & Đánh Bóng Men Răng',
                date: '2026-10-20',
                time: '16:00',
                branch: 'Chi nhánh Quận 7',
                status: 'Đã đặt hẹn',
                notes: 'Bé khó tính khi đụng vào miệng, cần tiền mê nhẹ an toàn.'
            },
            {
                id: 'APT-1085',
                customerName: 'Đặng Tuấn Anh',
                customerPhone: '0933 222 111',
                petName: 'Rocky',
                petType: 'Chó Golden',
                serviceName: 'Cấp Cứu Thú Y 24/7 & Hồi Sức Tích Cực (ICU)',
                date: '2026-10-20',
                time: '21:15',
                branch: 'Chi nhánh Quận 1',
                status: 'Hoàn thành',
                notes: 'Bé bị sốc nhiệt sau khi chạy bộ, đã hạ sốt và truyền dịch ổn định.'
            },
            {
                id: 'APT-1084',
                customerName: 'Hoàng Minh Đức',
                customerPhone: '0903 111 222',
                petName: 'Bông Lan',
                petType: 'Mèo Xiêm',
                serviceName: 'Khách Sạn Thú Cưng Pet Hotel Đẳng Cấp 5 Sao',
                date: '2026-10-22',
                time: '08:00',
                branch: 'Chi nhánh Quận 7',
                status: 'Đã đặt hẹn',
                notes: 'Gửi bé 3 ngày, cho ăn pate Ciao vị cá ngừ mỗi tối, gửi clip camera hàng ngày.'
            },
            {
                id: 'APT-1083',
                customerName: 'Vũ Thùy Linh',
                customerPhone: '0944 666 888',
                petName: 'Milu',
                petType: 'Chó Pug',
                serviceName: 'Tắm Trị Liệu Trị Nấm & Viêm Da Chuyên Sâu',
                date: '2026-10-19',
                time: '15:00',
                branch: 'Chi nhánh Bình Thạnh',
                status: 'Hoàn thành',
                notes: 'Vùng nách và nếp gấp mặt bị đỏ ngứa, dùng dầu tắm Davis 4%.'
            },
            {
                id: 'APT-1082',
                customerName: 'Đỗ Thị Hạnh',
                customerPhone: '0918 999 123',
                petName: 'Lucky',
                petType: 'Chó Samoyed',
                serviceName: 'Đưa Đón Thú Cưng Khám Bệnh & Spa (Pet Taxi)',
                date: '2026-10-19',
                time: '08:30',
                branch: 'Chi nhánh Quận 1',
                status: 'Hủy hẹn',
                notes: 'Khách bận công tác đột xuất, đã hẹn dời sang tuần sau.'
            }
        ],

        // 8 Đơn hàng Admin
        orders: [
            {
                id: 'ORD-8821',
                customer: 'Nguyễn Phương Thảo',
                date: '2026-10-20',
                items: 'Royal Canin Mini Adult (1kg), Sữa tắm Davis 4%',
                total: 700000,
                totalAmount: 700000,
                paymentMethod: 'Chuyển khoản VietQR',
                status: 'Đã thanh toán',
                branch: 'Q7'
            },
            {
                id: 'ORD-8820',
                customer: 'Hoàng Minh Đức',
                date: '2026-10-20',
                items: 'Orijen Original (2kg), Pate Ciao Churu (gói 20 thanh)',
                total: 1105000,
                totalAmount: 1105000,
                paymentMethod: 'Ví MoMo',
                status: 'Đang vận chuyển',
                branch: 'HN'
            },
            {
                id: 'ORD-8819',
                customer: 'Vũ Thùy Linh',
                date: '2026-10-19',
                items: 'Cát Đậu Nành Cature 6L (x2), Balo Phi Thuyền VIP',
                total: 820000,
                totalAmount: 820000,
                paymentMethod: 'COD khi nhận hàng',
                status: 'Hoàn thành',
                branch: 'BT'
            },
            {
                id: 'ORD-8818',
                customer: 'Trần Văn Hoàng',
                date: '2026-10-19',
                items: 'Viên nhai NexGard Spectra, Hạt Royal Canin Kitten',
                total: 855000,
                totalAmount: 855000,
                paymentMethod: 'Chuyển khoản VietQR',
                status: 'Đã thanh toán',
                branch: 'Q1'
            },
            {
                id: 'ORD-8817',
                customer: 'Lê Thị Mai',
                date: '2026-10-18',
                items: 'Trụ Cào Móng Cat Tree 3 Tầng, Pate Ciao Churu',
                total: 895000,
                totalAmount: 895000,
                paymentMethod: 'Ví MoMo',
                status: 'Hoàn thành',
                branch: 'Q7'
            },
            {
                id: 'ORD-8816',
                customer: 'Phạm Quốc Bảo',
                date: '2026-10-18',
                items: 'Tuýp nhỏ gáy Revolution Plus, Gel dinh dưỡng Virbac',
                total: 680000,
                totalAmount: 680000,
                paymentMethod: 'COD khi nhận hàng',
                status: 'Hoàn thành',
                branch: 'BT'
            },
            {
                id: 'ORD-8815',
                customer: 'Đặng Tuấn Anh',
                date: '2026-10-17',
                items: 'Combo 12 Lon Pate Monge, Cát Cature 6L',
                total: 585000,
                totalAmount: 585000,
                paymentMethod: 'Chuyển khoản VietQR',
                status: 'Hoàn thành',
                branch: 'Q1'
            },
            {
                id: 'ORD-8814',
                customer: 'Đỗ Thị Hạnh',
                date: '2026-10-17',
                items: 'Thức Ăn Hạt Orijen Original (2kg)',
                total: 890000,
                totalAmount: 890000,
                paymentMethod: 'Ví VNPay',
                status: 'Đang vận chuyển',
                branch: 'Q7'
            }
        ],

        // 6 Khách hàng Admin với cột Thú Cưng Đang Nuôi chi tiết
        customers: [
            {
                id: 1,
                name: 'Nguyễn Phương Thảo',
                phone: '0988 123 456',
                email: 'phuongthao.petcare@gmail.com',
                tier: 'Thành viên Vàng',
                petCount: 3,
                pets: 'Bơ (Corgi), Mochi (Mèo ALN), Đậu Đậu (Poodle)',
                petsList: [
                    { name: 'Bơ', breed: 'Corgi', type: 'Chó' },
                    { name: 'Mochi', breed: 'Mèo ALN', type: 'Mèo' },
                    { name: 'Đậu Đậu', breed: 'Poodle', type: 'Chó' }
                ],
                spent: 18500000,
                totalSpent: 18500000,
                points: 3450,
                avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80',
                createdAt: '15/01/2025'
            },
            {
                id: 2,
                name: 'Hoàng Minh Đức',
                phone: '0903 111 222',
                email: 'minhduc.dev@gmail.com',
                tier: 'Thành viên Kim Cương',
                petCount: 2,
                pets: 'Bông Lan (Mèo Xiêm), Sushi (Chó Shiba)',
                petsList: [
                    { name: 'Bông Lan', breed: 'Mèo Xiêm', type: 'Mèo' },
                    { name: 'Sushi', breed: 'Shiba Inu', type: 'Chó' }
                ],
                spent: 32400000,
                totalSpent: 32400000,
                points: 8200,
                avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=300&q=80',
                createdAt: '10/08/2024'
            },
            {
                id: 3,
                name: 'Lê Thị Mai',
                phone: '0977 888 999',
                email: 'maile.design@gmail.com',
                tier: 'Thành viên Bạc',
                petCount: 1,
                pets: 'Lu Lu (Poodle)',
                petsList: [
                    { name: 'Lu Lu', breed: 'Poodle', type: 'Chó' }
                ],
                spent: 4500000,
                totalSpent: 4500000,
                points: 1250,
                avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=300&q=80',
                createdAt: '05/06/2025'
            },
            {
                id: 4,
                name: 'Trần Văn Hoàng',
                phone: '0912 345 678',
                email: 'hoang.tran@gmail.com',
                tier: 'Thành viên Vàng',
                petCount: 2,
                pets: 'Kem Mút (Mèo ALN), Milo (Pug)',
                petsList: [
                    { name: 'Kem Mút', breed: 'Mèo ALN', type: 'Mèo' },
                    { name: 'Milo', breed: 'Pug', type: 'Chó' }
                ],
                spent: 14800000,
                totalSpent: 14800000,
                points: 2900,
                avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=300&q=80',
                createdAt: '12/11/2024'
            },
            {
                id: 5,
                name: 'Phạm Quốc Bảo',
                phone: '0903 555 777',
                email: 'bao.pham@vietin.vn',
                tier: 'Thành viên Bạc',
                petCount: 1,
                pets: 'Miu Miu (Mèo Ba Tư)',
                petsList: [
                    { name: 'Miu Miu', breed: 'Mèo Ba Tư', type: 'Mèo' }
                ],
                spent: 6200000,
                totalSpent: 6200000,
                points: 1540,
                avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=300&q=80',
                createdAt: '22/02/2025'
            },
            {
                id: 6,
                name: 'Đặng Tuấn Anh',
                phone: '0933 222 111',
                email: 'tuananh.dang@gmail.com',
                tier: 'Thành viên Kim Cương',
                petCount: 2,
                pets: 'Rocky (Golden Retriever), Tom (Mèo Mướp)',
                petsList: [
                    { name: 'Rocky', breed: 'Golden', type: 'Chó' },
                    { name: 'Tom', breed: 'Mèo Mướp', type: 'Mèo' }
                ],
                spent: 28900000,
                totalSpent: 28900000,
                points: 7450,
                avatar: 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=300&q=80',
                createdAt: '18/09/2024'
            }
        ],

        // MOCK DATA 6 THÁNG GẦN NHẤT CHO BIỂU ĐỒ DOANH THU (TRIỆU VNĐ)
        revenueMonthlyMock: [
            { month: 'Tháng 5', ecommerceRevenue: 135000000, serviceRevenue: 152000000 },
            { month: 'Tháng 6', ecommerceRevenue: 148000000, serviceRevenue: 168000000 },
            { month: 'Tháng 7', ecommerceRevenue: 162000000, serviceRevenue: 185000000 },
            { month: 'Tháng 8', ecommerceRevenue: 175000000, serviceRevenue: 198000000 },
            { month: 'Tháng 9', ecommerceRevenue: 190000000, serviceRevenue: 220000000 },
            { month: 'Tháng 10', ecommerceRevenue: 215000000, serviceRevenue: 245000000 }
        ],

        // Doanh thu chi tiết theo ngành hàng
        analyticsRevenueCommerce: [
            { category: 'Thức ăn hạt khô', revenue: 145000000, share: 42, growth: '+18.5%' },
            { category: 'Pate & Treats dinh dưỡng', revenue: 68000000, share: 20, growth: '+24.2%' },
            { category: 'Thuốc & Y tế đặc trị', revenue: 55000000, share: 16, growth: '+12.0%' },
            { category: 'Vệ sinh & Cát đậu nành', revenue: 42000000, share: 12, growth: '+8.4%' },
            { category: 'Phụ kiện & Balo đồ chơi', revenue: 35000000, share: 10, growth: '+15.1%' }
        ],
        analyticsRevenueService: [
            { category: 'Spa & Cắt tỉa Grooming', revenue: 168000000, share: 45, growth: '+28.4%' },
            { category: 'Khám chữa bệnh & Nội trú', revenue: 95000000, share: 25, growth: '+14.2%' },
            { category: 'Khách sạn thú cưng Pet Hotel', revenue: 52000000, share: 14, growth: '+35.0%' },
            { category: 'Tiêm chủng & Phòng dịch', revenue: 38000000, share: 10, growth: '+9.8%' },
            { category: 'Cấp cứu 24/7 & Xe đưa đón', revenue: 22000000, share: 6, growth: '+19.6%' }
        ],

        // Giỏ hàng & Booking flow
        cart: [],
        bookingItem: null,
        prodModalQty: 1,

        // Form thêm thú cưng mới (Có hỗ trợ tải ảnh và xác thực đỏ)
        newPetData: {
            name: '',
            type: 'Chó',
            breed: '',
            gender: 'Đực',
            age: '',
            weight: '',
            avatar: '',
            appearance: '',
            allergies: '',
            diet: '',
            habits: '',
            personality: '',
            ownerName: 'Nguyễn Phương Thảo',
            ownerPhone: '0988 123 456',
            ownerAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
            ownerEmergency: '0912 345 678 (Chồng)'
        },

        newProdForm: {
            sku: '',
            name: '',
            brand: '',
            price: null,
            stockQ1: 20,
            stockBT: 15,
            stockQ7: 25,
            category: 'Thức ăn & Dinh dưỡng',
            img: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
            desc: ''
        },

        restockForm: {
            productId: '',
            branch: 'Q1',
            quantity: 50,
            costPrice: null,
            supplier: '',
            notes: ''
        },

        checkoutForm: {
            name: 'Nguyễn Hoàng Giang',
            phone: '0909123456',
            address: '125 Hoàng Quốc Việt, Cầu Giấy, Hà Nội',
            paymentMethod: 'momo'
        },
        momoQrImage: 'momo_qr.jpg',

        // Live Chat Box
        chatMessages: [
            {
                sender: 'bot',
                text: 'Xin chào quý khách! Bác sĩ thú y và Đội ngũ CSKH PetCare360 rất hân hạnh được đồng hành cùng bạn và bé cưng. Bạn đang cần hỗ trợ dịch vụ nào ạ?',
                time: 'Vừa xong'
            }
        ],
        newChatMessage: '',

        // COMPUTED & GETTERS
        get cartItemsCount() {
            return this.cart.reduce((sum, item) => sum + (item.qty || 1), 0);
        },

        get cartTotal() {
            return this.cart.reduce((sum, item) => sum + (item.price * (item.qty || 1)), 0);
        },

        // Lọc sản phẩm theo 3 danh mục chính xác
        get filteredProducts() {
            return this.products.filter(p => {
                const cat = this.filterCategory || 'all';
                const matchCat = (cat === 'all') || (p.category === cat);
                const query = (this.searchQuery || this.productSearchQuery || '').toLowerCase().trim();
                const matchSearch = !query || p.name.toLowerCase().includes(query) || (p.brand && p.brand.toLowerCase().includes(query));
                return matchCat && matchSearch;
            });
        },

        // Lọc dịch vụ theo 4 danh mục chính xác
        get filteredServices() {
            return this.services.filter(s => {
                const cat = this.filterServiceCategory || 'all';
                const matchCat = (cat === 'all') || (s.category === cat);
                const query = (this.serviceSearchQuery || this.searchQuery || '').toLowerCase().trim();
                const matchSearch = !query || s.name.toLowerCase().includes(query) || (s.desc && s.desc.toLowerCase().includes(query));
                return matchCat && matchSearch;
            });
        },

        get filteredArticles() {
            return this.articles.filter(art => {
                const cat = (this.filterArticleCat || 'all');
                const matchCat = cat === 'all' || art.category.toLowerCase().includes(cat.toLowerCase());
                const query = (this.searchArticleQuery || this.searchQuery || '').toLowerCase();
                const matchSearch = !query || art.title.toLowerCase().includes(query) || art.summary.toLowerCase().includes(query);
                return matchCat && matchSearch;
            });
        },

        get filteredAppointments() {
            return this.appointments.filter(apt => {
                const q = (this.appointmentSearchQuery || '').toLowerCase();
                const matchQ = !q || apt.customerName.toLowerCase().includes(q) || apt.petName.toLowerCase().includes(q) || apt.id.toLowerCase().includes(q);
                const matchServ = (this.appointmentServiceFilter || 'all') === 'all' || apt.serviceName.includes(this.appointmentServiceFilter);
                const matchBranch = (this.globalBranch || 'all') === 'all' || apt.branch.includes(this.getBranchLabel(this.globalBranch));
                return matchQ && matchServ && matchBranch;
            });
        },

        get filteredAdminOrders() {
            return this.orders.filter(ord => {
                const q = (this.orderSearchQuery || '').toLowerCase();
                const matchQ = !q || ord.customer.toLowerCase().includes(q) || ord.id.toLowerCase().includes(q);
                const matchStatus = (this.orderStatusFilter || 'all') === 'all' || ord.status === this.orderStatusFilter;
                const matchBranch = (this.globalBranch || 'all') === 'all' || (ord.branch === this.globalBranch);
                return matchQ && matchStatus && matchBranch;
            });
        },

        get filteredOrdersByBranch() {
            return this.filteredAdminOrders;
        },

        get filteredProductsInventory() {
            return this.products.filter(p => {
                const q = (this.productSearchQuery || '').toLowerCase();
                const matchQ = !q || p.name.toLowerCase().includes(q) || p.sku.toLowerCase().includes(q);
                const totalStock = this.getSafeTotalStock(p);
                const matchLow = !this.showLowStockOnly || totalStock <= 10;
                return matchQ && matchLow;
            });
        },

        get filteredAdminPets() {
            return this.pets.filter(p => {
                const q = (this.petSearchQuery || '').toLowerCase();
                return !q || p.name.toLowerCase().includes(q) || p.breed.toLowerCase().includes(q) || (p.chipId && p.chipId.includes(q)) || (p.ownerName && p.ownerName.toLowerCase().includes(q));
            });
        },

        get filteredAdminCustomers() {
            return this.customers.filter(c => {
                const q = (this.customerSearchQuery || '').toLowerCase();
                return !q || c.name.toLowerCase().includes(q) || c.phone.includes(q) || c.email.toLowerCase().includes(q) || (c.pets && c.pets.toLowerCase().includes(q));
            });
        },

        // TÍNH TOÁN AN TOÀN TRÁNH NaN DOANH THU
        get unreadNotificationsCount() {
            return (this.adminNotifications || []).filter(n => !n.read).length;
        },

        get totalEcommerceRevenue() {
            const list = this.revenueMonthlyMock || [];
            return list.reduce((sum, item) => sum + (Number(item.ecommerceRevenue) || 0), 0);
        },

        get totalServiceRevenue() {
            const list = this.revenueMonthlyMock || [];
            return list.reduce((sum, item) => sum + (Number(item.serviceRevenue) || 0), 0);
        },

        get totalRevenueFiltered() {
            if (this.adminTimeFilter === 'today') return 18500000;
            if (this.adminTimeFilter === '7days') return 112000000;
            if (this.adminTimeFilter === 'month') return 460000000;
            if (this.adminTimeFilter === 'quarter') return 1380000000;
            return this.totalEcommerceRevenue + this.totalServiceRevenue;
        },

        get pendingOrdersCount() {
            return this.orders.filter(o => o.status !== 'Hoàn thành').length;
        },

        get inProgressAppointmentsCount() {
            return this.appointments.filter(a => a.status === 'Đang tiếp khách' || a.status === 'Đã đặt hẹn').length;
        },

        get lowStockCount() {
            return this.products.filter(p => this.getSafeTotalStock(p) <= 10).length;
        },

        get urgentTasksCount() {
            return this.pendingOrdersCount + this.inProgressAppointmentsCount;
        },

        // Helper tính tổng tồn kho an toàn tuyệt đối tránh NaN
        getSafeTotalStock(p) {
            const q1 = Number(p.stockQ1 !== undefined ? p.stockQ1 : (p.q1 !== undefined ? p.q1 : 0)) || 0;
            const bt = Number(p.stockBT !== undefined ? p.stockBT : (p.bt !== undefined ? p.bt : 0)) || 0;
            const q7 = Number(p.stockQ7 !== undefined ? p.stockQ7 : (p.q7 !== undefined ? p.q7 : 0)) || 0;
            return q1 + bt + q7;
        },

        // Helper label formatters
        formatCurrency(amount) {
            const num = Number(amount);
            if (isNaN(num) || (!num && num !== 0)) return '0 đ';
            return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(num);
        },

        formatMoney(amount) {
            return this.formatCurrency(amount);
        },

        getBranchLabel(code) {
            if (code === 'HN' || code === 'Q1') return 'Quận 1';
            if (code === 'Q7') return 'Quận 7';
            if (code === 'BT') return 'Bình Thạnh';
            return 'Toàn Hệ Thống';
        },

        getTimeFilterLabel(code) {
            if (code === 'today') return 'Hôm nay';
            if (code === '7days') return '7 ngày qua';
            if (code === 'month') return 'Tháng này';
            if (code === 'quarter') return 'Quý này';
            return 'Toàn bộ thời gian';
        },

        formatAppointmentStatus(status) {
            return status || 'Đã đặt hẹn';
        },

        formatOrderStatusLabel(status) {
            if (status === 'deposit_paid' || status === 'Đã cọc' || status === 'Đã cọc 50%') return 'Đã cọc 50%';
            if (status === 'PENDING' || status === 'pending') return 'Chờ xác nhận';
            if (status === 'PREPARING') return 'Đang xử lý';
            if (status === 'DELIVERING') return 'Đang giao hàng';
            if (status === 'COMPLETED') return 'Hoàn thành';
            if (status === 'CANCELLED') return 'Đã hủy';
            return status || 'Đã ghi nhận';
        },

        // Khởi tạo app & vẽ biểu đồ doanh thu Chart.js
        initApp() {
            console.log('PetCare360 Unified SuperApp Initialized!');
            if (this.customerProfile && (!this.customerProfile.pets || this.customerProfile.pets.length === 0)) {
                this.customerProfile.pets = this.pets;
            }
            if (this.serviceBookingForm && this.serviceBookingForm.petId) {
                this.syncPetBookingDetails(this.serviceBookingForm.petId);
            }
            if (window.lucide) {
                window.lucide.createIcons();
            }
            this.$nextTick(() => {
                this.renderRevenueChart();
            });
        },

        // VẼ BIỂU ĐỒ DOANH THU 6 THÁNG GẦN NHẤT BẰNG CHART.JS
        renderRevenueChart() {
            const canvas = document.getElementById('revenueChart');
            if (!canvas) return;

            // Xóa instance cũ nếu tồn tại
            if (window.petcareRevenueChartInstance) {
                window.petcareRevenueChartInstance.destroy();
                window.petcareRevenueChartInstance = null;
            }

            const data = this.revenueMonthlyMock || [];
            if (data.length === 0) return;

            const labels = data.map(d => d.month);
            // Quy đổi sang Triệu VNĐ: Math.round(revenue / 1000000)
            const ecomData = data.map(d => Math.round((Number(d.ecommerceRevenue) || 0) / 1000000));
            const servData = data.map(d => Math.round((Number(d.serviceRevenue) || 0) / 1000000));

            const ctx = canvas.getContext('2d');
            window.petcareRevenueChartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Sản phẩm E-Commerce (Triệu VNĐ)',
                            data: ecomData,
                            backgroundColor: '#0d9488', // teal-600
                            borderColor: '#0f766e',
                            borderWidth: 1,
                            borderRadius: 6
                        },
                        {
                            label: 'Dịch vụ Y tế & Spa (Triệu VNĐ)',
                            data: servData,
                            backgroundColor: '#6366f1', // indigo-500
                            borderColor: '#4f46e5',
                            borderWidth: 1,
                            borderRadius: 6
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'top',
                            labels: {
                                boxWidth: 14,
                                font: { size: 12, weight: 'bold' }
                            }
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.dataset.label + ': ' + context.parsed.y + ' Triệu VNĐ';
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: { display: false },
                            ticks: { font: { size: 11, weight: 'bold' } }
                        },
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Doanh thu (Triệu VNĐ)',
                                font: { size: 11, weight: 'bold' }
                            },
                            ticks: {
                                callback: function(value) {
                                    return value + ' tr';
                                }
                            }
                        }
                    }
                }
            });
        },

        // Điều hướng & Auth
        openLoginModal() {
            this.loginUsername = '';
            this.loginPassword = '';
            this.loginError = '';
            this.showLoginModal = true;
            this.loginModalOpen = true;
        },

        handleLogin() {
            const user = (this.loginUsername || '').trim();
            const pass = (this.loginPassword || '').trim();

            if (!user || !pass) {
                this.loginError = 'Tên đăng nhập hoặc mật khẩu không đúng.';
                return;
            }

            if (user === 'teamnhonho' && pass === 'noletdtu$2006') {
                this.isLoggedIn = true;
                this.currentRole = 'admin';
                this.activeAdminTab = 'dashboard';
                this.showLoginModal = false;
                this.loginModalOpen = false;
                this.loginError = '';
                alert('Đăng nhập thành công với quyền Quản Trị Viên (Admin PetCare360)!');
                this.$nextTick(() => {
                    this.renderRevenueChart();
                });
            } else {
                this.isLoggedIn = true;
                this.currentRole = 'customer';
                this.showLoginModal = false;
                this.loginModalOpen = false;
                this.loginError = '';
                alert('Đăng nhập thành công tài khoản Khách Hàng: ' + user + '!');
            }
        },

        logout() {
            this.isLoggedIn = false;
            this.currentRole = 'customer';
            this.activeCustomerTab = 'home';
            alert('Bạn đã đăng xuất tài khoản thành công.');
        },

        handleLogout() {
            this.logout();
        },

        switchAdminTab(tab) {
            this.activeAdminTab = tab;
            if (tab === 'dashboard' || tab === 'analytics') {
                this.$nextTick(() => {
                    this.renderRevenueChart();
                });
            }
        },

        applyTimeFilter(period) {
            this.adminTimeFilter = period;
            alert('Đã cập nhật bộ lọc thời gian: ' + this.getTimeFilterLabel(period));
            this.$nextTick(() => {
                this.renderRevenueChart();
            });
        },

        // Quản lý thông báo Admin
        toggleAdminNotifications() {
            this.showAdminNotifications = !this.showAdminNotifications;
        },

        markNotificationRead(id) {
            const notif = (this.adminNotifications || []).find(n => n.id === id);
            if (notif) notif.read = true;
        },

        markAllNotificationsRead() {
            this.adminNotifications.forEach(n => n.read = true);
            alert('Đã đánh dấu đọc tất cả thông báo!');
        },

        // Modal triggers
        openProductDetail(product) {
            this.selectedProductModal = product;
            this.prodModalQty = 1;
        },

        openServiceDetail(service) {
            this.selectedServiceModal = service;
        },

        openArticleDetail(article) {
            this.selectedArticle = article;
            this.selectedArticleModal = article;
        },

        openPetHealthModal(pet) {
            this.selectedPetHealthModal = pet;
        },

        openPolicyModal(type) {
            this.showLegalModal = true;
            this.policyModalOpen = true;
        },

        openAddProductModal() {
            this.showAddProductModal = true;
            this.addProductModalOpen = true;
        },

        openRestockModal(product) {
            this.showRestockModal = true;
            this.restockModalOpen = true;
            if (product) {
                this.restockForm.productId = product.id;
            }
        },

        openCustomerSupportChat() {
            this.showChatModal = true;
            this.chatModalOpen = true;
        },

        openChatWithCustomer(customerName) {
            this.showChatModal = true;
            this.chatModalOpen = true;
        },

        openNewAppointmentModal() {
            alert('Để tạo lịch hẹn mới cho khách, vui lòng chọn dịch vụ trong danh mục Dịch Vụ.');
            this.activeCustomerTab = 'booking';
        },

        openOrderDetail(order) {
            this.selectedOrder = order;
            this.orderDrawerOpen = true;
        },

        // Thao tác giỏ hàng & Đặt lịch
        addToCart(product, qty = 1) {
            const existing = this.cart.find(item => item.id === product.id && !item.isService);
            const validImg = product.image || product.img || this.getItemImage(product);
            if (existing) {
                existing.qty += qty;
                existing.quantity = existing.qty;
                if (!existing.image) existing.image = validImg;
                if (!existing.img) existing.img = validImg;
            } else {
                this.cart.push({
                    id: product.id,
                    name: product.name,
                    price: product.price,
                    img: validImg,
                    image: validImg,
                    qty: qty,
                    quantity: qty,
                    isService: false
                });
            }
            this.showCartDrawer = true;
            this.cartOpen = true;
        },

        buyNow(product, qty = 1) {
            this.addToCart(product, qty);
        },

        removeFromCart(index) {
            this.cart.splice(index, 1);
        },

        openBookingModalForService(service) {
            let cartService = this.cart.find(i => i.id === service.id && i.isService);
            if (!cartService) {
                const sImg = service.image || service.img || this.getItemImage(service);
                cartService = {
                    id: service.id,
                    name: service.name,
                    price: service.price,
                    img: sImg,
                    image: sImg,
                    qty: 1,
                    quantity: 1,
                    isService: true,
                    selectedPet: this.pets.length > 0 ? this.pets[0].name : '',
                    bookingDate: new Date(Date.now() + 86400000).toISOString().split('T')[0],
                    bookingTime: '09:30',
                    bookingBranch: 'Chi nhánh Quận 7 (450 Nguyễn Thị Thập, P. Tân Quy, Q7, TP.HCM)',
                    bookingNotes: ''
                };
                this.cart.push(cartService);
            }
            this.bookingItem = cartService;
            this.showBookingDetailModal = true;
            this.bookingDetailModalOpen = true;
        },

        saveBookingDetails() {
            if (!this.bookingItem.selectedPet || !this.bookingItem.bookingDate) {
                alert('Vui lòng chọn thú cưng và ngày hẹn!');
                return;
            }
            this.showBookingDetailModal = false;
            this.bookingDetailModalOpen = false;
            this.showCartDrawer = true;
            this.cartOpen = true;
            alert('Đã cập nhật thông tin đặt lịch chi tiết cho bé ' + this.bookingItem.selectedPet + ' thành công!');
        },

        // VALIDATION: Bắt buộc điền đủ đặt lịch chi tiết cho dịch vụ trước khi thanh toán
        checkAndOpenCheckout() {
            if (this.cart.length === 0) {
                alert('Giỏ hàng của bạn đang trống! Vui lòng chọn sản phẩm hoặc dịch vụ.');
                return;
            }

            const incompleteService = this.cart.find(item => item.isService && (!item.bookingDate || !item.selectedPet) && (!item.bookingDetails || !item.bookingDetails.date));
            if (incompleteService) {
                alert('⚠️ NHẮC NHỞ: Bạn chưa điền đầy đủ thông tin "Đặt lịch chi tiết" (chọn thú cưng và ngày hẹn) cho dịch vụ: "' + incompleteService.name + '". Vui lòng hoàn tất thông tin trước khi thanh toán!');
                this.openBookingModalForService(incompleteService);
                return;
            }

            if (!this.checkoutForm.name || this.checkoutForm.name === 'Nguyễn Phương Thảo') {
                this.checkoutForm.name = this.checkoutShippingForm.name || (this.customerProfile ? this.customerProfile.name : 'Nguyễn Hoàng Giang');
                this.checkoutForm.phone = this.checkoutShippingForm.phone || (this.customerProfile ? this.customerProfile.phone : '0909123456');
                this.checkoutForm.address = this.checkoutShippingForm.address ? (this.checkoutShippingForm.address + ', ' + this.checkoutShippingForm.ward + ', ' + this.checkoutShippingForm.district + ', ' + this.checkoutShippingForm.city) : ((this.customerProfile ? this.customerProfile.address : '') || '125 Hoàng Quốc Việt, Cầu Giấy, Hà Nội');
            }
            if (!this.checkoutForm.paymentMethod) {
                this.checkoutForm.paymentMethod = 'momo';
            }
            if (!this.checkoutForm.orderCode) {
                this.checkoutForm.orderCode = 'DH' + Math.floor(100000 + Math.random() * 900000);
            }

            // Đồng bộ thông tin người nhận sang form nhận hàng & thanh toán
            if (!this.checkoutShippingForm.name || this.checkoutShippingForm.name === 'Nguyễn Phương Thảo') {
                this.checkoutShippingForm.name = (this.customerProfile ? this.customerProfile.name : '') || 'Nguyễn Hoàng Giang';
                this.checkoutShippingForm.phone = (this.customerProfile ? this.customerProfile.phone : '') || '0909123456';
                this.checkoutShippingForm.address = (this.customerProfile ? this.customerProfile.address : '') || '125 Hoàng Quốc Việt';
            }

            // Đóng sidebar giỏ hàng và chuyển thẳng sang màn hình "2. Thông tin nhận hàng & Lịch hẹn" (bỏ qua modal Xác nhận đơn hàng & Dịch Vụ)
            this.showCartDrawer = false;
            this.cartOpen = false;
            this.showCheckoutModal = false;
            this.activeCustomerTab = 'cart';
            this.cartStep = 2;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },
        // HÀM TIỆN ÍCH LẤY ẢNH CHUẨN XÁC CHO SẢN PHẨM & DỊCH VỤ (FIX LỖI HIỂN THỊ ẢNH)
        getItemImage(item) {
            if (!item) return 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80';
            if (item.image && typeof item.image === 'string' && item.image.trim() !== '') return item.image;
            if (item.img && typeof item.img === 'string' && item.img.trim() !== '') return item.img;
            
            // Tìm theo danh mục sản phẩm nếu có id hoặc tên
            if (this.products && this.products.length > 0) {
                const p = this.products.find(prod => (item.id && prod.id === item.id) || (item.name && (prod.name === item.name || item.name.includes(prod.name) || prod.name.includes(item.name))));
                if (p && (p.image || p.img)) return p.image || p.img;
            }
            
            // Map theo từ khóa tên sản phẩm / dịch vụ
            const n = (item.name || '').toLowerCase();
            if (n.includes('hotel') || n.includes('khách sạn') || n.includes('lưu trú')) {
                return 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('grooming') || n.includes('spa') || n.includes('tắm') || n.includes('cắt tỉa') || n.includes('shave')) {
                return 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('tiêm') || n.includes('vắc-xin') || n.includes('khám') || n.includes('bác sĩ') || n.includes('xét nghiệm')) {
                return 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('nexgard') || n.includes('ve rận') || n.includes('tẩy giun')) {
                return 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('cat tree') || n.includes('trụ cào') || n.includes('cào móng')) {
                return 'https://images.unsplash.com/photo-1545249390-6bdfa286032f?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('balo') || n.includes('phi thuyền') || n.includes('vận chuyển')) {
                return 'https://images.unsplash.com/photo-1522276498395-f4e0795392e6?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('pate') || n.includes('churu') || n.includes('ciao') || n.includes('monge')) {
                return 'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('hạt') || n.includes('royal canin') || n.includes('orijen') || n.includes('thức ăn')) {
                return 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('cát') || n.includes('tofu') || n.includes('cature')) {
                return 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('gel') || n.includes('nutri')) {
                return 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=400&q=80';
            }
            if (n.includes('sữa tắm') || n.includes('davis')) {
                return 'https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=400&q=80';
            }
            return 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=300&q=80';
        },


        confirmOrderAndPay() {
            if (!this.isModalCheckoutValid) {
                alert('⚠️ Vui lòng điền đầy đủ Họ tên, Số điện thoại hợp lệ (10 số VN) và Địa chỉ nhận hàng!');
                return;
            }

            // Khóa tạm tồn kho cho sản phẩm
            this.holdStockForCart();

            let paymentType = 'product_only';
            if (this.hasProduct && this.hasService) {
                paymentType = 'mixed_cart';
            } else if (this.hasHotel) {
                paymentType = 'hotel_deposit';
            } else if (this.hasOtherService) {
                paymentType = 'service_full';
            }

            const newOrderCode = this.checkoutForm.orderCode ? ('#' + this.checkoutForm.orderCode.replace('#', '')) : ('#' + Math.floor(100000 + Math.random() * 900000));
            const newOrderId = 'ORD-' + Math.floor(1000 + Math.random() * 9000);
            const todayStr = new Date().toLocaleDateString('vi-VN');

            const order = {
                id: newOrderId,
                orderCode: newOrderCode,
                date: todayStr,
                status: 'PENDING_PAYMENT',
                statusText: 'Chờ thanh toán (Giữ chỗ 15p)',
                badgeColor: 'bg-amber-100 text-amber-800 border-amber-200',
                payment_type: paymentType,
                has_mixed_cart: this.hasProduct && this.hasService,
                amount_paid: this.currentPayment,
                balance_due: this.remainingBalance,
                total: this.grandTotal,
                grandTotal: this.grandTotal,
                currentPayment: this.currentPayment,
                remainingBalance: this.remainingBalance,
                subtotal: this.cartSubtotal,
                totalProduct: this.totalProduct,
                totalOtherService: this.totalOtherService,
                totalHotel: this.totalHotel,
                hotelDeposit: this.hotelDeposit,
                shippingFee: this.effectiveShippingFee,
                shippingDiscount: this.shippingDiscount,
                orderDiscount: this.orderDiscount,
                totalDiscount: this.totalDiscount,
                paymentMethod: this.checkoutForm.paymentMethod,
                paymentMethodLabel: this.checkoutForm.paymentMethod === 'momo' ? 'Ví điện tử MoMo' : (this.checkoutForm.paymentMethod === 'vietqr' ? 'Chuyển khoản VietQR MB Bank' : 'Thanh toán COD'),
                paymentStatus: 'unpaid',
                recipient: {
                    name: this.checkoutForm.name,
                    phone: this.checkoutForm.phone,
                    address: this.checkoutForm.address
                },
                items: this.cart.map(i => ({ ...i, img: i.img || i.image || this.getItemImage(i), image: i.image || i.img || this.getItemImage(i) })),
                holdStockExpiresAt: Date.now() + 15 * 60 * 1000
            };

            this.completedOrderNumber = newOrderCode;
            this.completedOrderDate = todayStr;
            this.currentPendingOrder = order;
            this.customerOrdersEnhanced.unshift(order);
            this.orders.unshift(order);

            // Đồng bộ sang Admin Lịch hẹn nếu có dịch vụ
            const serviceItems = this.cart.filter(item => item.isService);
            serviceItems.forEach(serv => {
                this.appointments.unshift({
                    id: 'APT-' + Math.floor(1000 + Math.random() * 9000),
                    customerName: this.checkoutBookingContactName || this.checkoutShippingForm.name || this.customerProfile.name,
                    customerPhone: this.checkoutBookingContactPhone || this.checkoutShippingForm.phone || this.customerProfile.phone,
                    petship_address: this.hasPetShip ? (this.checkoutPetShipAddress.street + ', ' + this.checkoutPetShipAddress.ward + ', ' + this.checkoutPetShipAddress.district + ', TP. Hồ Chí Minh') : null,
                    payment_method: this.paymentMethod,
                    petName: serv.selectedPet || 'Bé cưng',
                    petType: 'Thú cưng khách chọn',
                    serviceName: serv.name,
                    date: serv.bookingDate || (serv.bookingDetails ? serv.bookingDetails.date : todayStr),
                    time: serv.bookingTime || (serv.bookingDetails ? serv.bookingDetails.slot : '09:00'),
                    branch: 'Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Q1, TPHCM',
                    status: 'Đã đặt hẹn',
                    notes: (this.servicePetShipAddress ? ('PetShip đón tại: ' + this.servicePetShipAddress) : 'Khách tự đưa đón tại cơ sở 88 NTMK')
                });
            });

            const earnedPoints = Math.floor(this.currentPayment / 10000);
            if (this.customerProfile) {
                this.customerProfile.points = (this.customerProfile.points || 0) + earnedPoints;
            }

            this.startOrderCountdown();
            this.webhookSuccessReceived = false;
            this.uploadedReceiptUrl = null;

            this.showCheckoutModal = false;
            this.cart = [];
            this.activeCustomerTab = 'cart';
            this.cartStep = 4;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        // XỬ LÝ TẢI ẢNH THÚ CƯNG TỪ THIẾT BỊ (FILEREADER)
        handlePetPhotoUpload(event) {
            const file = event.target.files && event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.newPetData.avatar = e.target.result;
                    this.petFormError = '';
                };
                reader.readAsDataURL(file);
            }
        },

        // LƯU HỒ SƠ THÚ CƯNG MỚI (KIỂM TRA CẢNH BÁO ĐỎ NẾU CHƯA ĐỦ THÔNG TIN HOẶC CHƯA TẢI ẢNH)
        saveNewPet() {
            // Kiểm tra bắt buộc: Phải có ảnh thú cưng, tên, loài, giống, cân nặng
            if (!this.newPetData.avatar || !this.newPetData.avatar.trim()) {
                this.petFormError = '⚠️ Vui lòng tải ảnh thú cưng lên để hoàn tất nhận diện bé cưng!';
                return;
            }

            if (!this.newPetData.name || !this.newPetData.name.trim() || !this.newPetData.breed || !this.newPetData.weight) {
                this.petFormError = '⚠️ Vui lòng điền đầy đủ các thông tin bắt buộc (Tên bé, loài, giống loài, cân nặng)!';
                return;
            }

            this.petFormError = '';
            const newId = this.pets.length + 1;
            const newPet = {
                id: newId,
                name: this.newPetData.name.trim(),
                type: this.newPetData.type || 'Chó',
                species: this.newPetData.type || 'Chó',
                breed: this.newPetData.breed.trim() || 'Chưa cập nhật',
                gender: this.newPetData.gender || 'Đực',
                age: this.newPetData.age.trim() || 'Mới nhận nuôi',
                weight: String(this.newPetData.weight).trim(),
                chipId: '900118000' + Math.floor(100000 + Math.random() * 900000),
                chip: '900118000' + Math.floor(100000 + Math.random() * 900000),
                avatar: this.newPetData.avatar,
                image: this.newPetData.avatar,
                appearance: this.newPetData.appearance.trim() || 'Ngoại hình khỏe mạnh, đặc điểm nhận dạng đặc trưng',
                health: 'Đã hoàn tất kiểm tra lâm sàng ban đầu',
                allergies: this.newPetData.allergies.trim() || 'Không ghi nhận tiền sử dị ứng thuốc hay thực phẩm',
                diet: this.newPetData.diet.trim() || 'Thức ăn hạt dinh dưỡng theo độ tuổi, nước uống sạch đầy đủ',
                habits: this.newPetData.habits.trim() || 'Thích vui chơi, thói quen sinh hoạt ổn định',
                personality: this.newPetData.personality.trim() || 'Thân thiện, nghe lời chủ nuôi',
                ownerName: this.newPetData.ownerName.trim() || this.customerProfile.name,
                ownerPhone: this.newPetData.ownerPhone.trim() || this.customerProfile.phone,
                ownerAddress: this.newPetData.ownerAddress.trim() || this.customerProfile.address,
                ownerEmergency: this.newPetData.ownerEmergency.trim() || '1900 6868 (Hotline Cấp cứu)',
                isDefault: false,
                lastVaccine: 'Khám lâm sàng ban đầu (' + new Date().toLocaleDateString('vi-VN') + ')',
                nextVaccine: 'Nhắc lại sau 1 tháng',
                vaccines: [
                    { name: 'Khám lâm sàng ban đầu & Sổ tiêm', date: new Date().toLocaleDateString('vi-VN'), doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: 'Hẹn 1 tháng sau', status: 'Đã hoàn thành' }
                ],
                medicalHistory: [
                    { date: new Date().toLocaleDateString('vi-VN'), diagnosis: 'Tạo hồ sơ thú cưng mới trên hệ thống PetCare360', treatment: 'Khám sàng lọc và tư vấn dinh dưỡng ban đầu', notes: 'Bé ngoan, thể trạng ổn định.' }
                ]
            };

            this.pets.push(newPet);
            this.customerProfile.petCount = this.pets.length;
            this.showAddPetModal = false;
            this.addPetModalOpen = false;

            // Reset form
            this.newPetData = {
                name: '',
                type: 'Chó',
                breed: '',
                gender: 'Đực',
                age: '',
                weight: '',
                avatar: '',
                appearance: '',
                allergies: '',
                diet: '',
                habits: '',
                personality: '',
                ownerName: this.customerProfile.name,
                ownerPhone: this.customerProfile.phone,
                ownerAddress: this.customerProfile.address,
                ownerEmergency: '0912 345 678'
            };

            alert('🎉 ĐÃ LƯU HỒ SƠ BÉ CƯNG! Hồ sơ bé ' + newPet.name + ' cùng ảnh chụp đã được hệ thống lưu trữ vĩnh viễn và đồng bộ sang dữ liệu Microchip toàn quốc.');
        },

        deletePet(id) {
            if (confirm('Bạn có chắc muốn xóa hồ sơ thú cưng này không?')) {
                this.pets = this.pets.filter(p => p.id !== id);
                this.customerProfile.petCount = this.pets.length;
                alert('Đã xóa hồ sơ bé thành công.');
            }
        },

        setDefaultPet(id) {
            this.pets.forEach(p => p.isDefault = (p.id === id));
            alert('Đã đặt làm bé cưng mặc định cho các dịch vụ tiếp theo.');
        },

        saveUserProfile() {
            this.showEditProfileModal = false;
            this.editProfileModalOpen = false;
            alert('Thông tin tài khoản và Avatar đại diện của bạn đã được cập nhật thành công!');
        },

        deleteAddress(id) {
            this.addresses = this.addresses.filter(a => a.id !== id);
            alert('Đã xóa địa chỉ thành công.');
        },

        setDefaultAddress(id) {
            this.addresses.forEach(a => a.isDefault = (a.id === id));
            alert('Đã đổi địa chỉ mặc định thành công.');
        },

        // Admin actions
        updateAppointmentStatusDirect(apt, status) {
            apt.status = status;
            alert('Đã cập nhật trạng thái lịch hẹn ' + apt.id + ' sang: "' + status + '"');
        },

        updateOrderStatus(order, status) {
            order.status = status;
            alert('Đã cập nhật trạng thái đơn hàng ' + order.id + ' sang: "' + status + '"');
        },

        adminSaveNewProduct() {
            if (!this.newProdForm.name || !this.newProdForm.price) {
                alert('Vui lòng điền đầy đủ tên sản phẩm và giá bán!');
                return;
            }
            const q1 = Number(this.newProdForm.stockQ1) || 20;
            const bt = Number(this.newProdForm.stockBT) || 15;
            const q7 = Number(this.newProdForm.stockQ7) || 25;
            this.products.unshift({
                id: this.products.length + 1,
                sku: this.newProdForm.sku || 'SKU-' + Math.floor(1000 + Math.random() * 9000),
                name: this.newProdForm.name,
                brand: this.newProdForm.brand || 'PetCare Brand',
                price: parseInt(this.newProdForm.price),
                rating: 5.0,
                reviews: 1,
                reviewsCount: 1,
                sold: 0,
                stockQ1: q1,
                stockBT: bt,
                stockQ7: q7,
                q1: q1, bt: bt, q7: q7,
                category: this.newProdForm.category || 'Thức ăn & Dinh dưỡng',
                categoryAdmin: this.newProdForm.category || 'Thức ăn & Dinh dưỡng',
                img: this.newProdForm.img || 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
                image: this.newProdForm.img || 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
                desc: this.newProdForm.desc || 'Sản phẩm mới nhập kho chính hãng.',
                description: this.newProdForm.desc || 'Sản phẩm mới nhập kho chính hãng.',
                ingredients: 'Nguyên liệu đạt tiêu chuẩn kiểm nghiệm an toàn thú y quốc tế.',
                usage: 'Sử dụng theo hướng dẫn chi tiết in trên bao bì sản phẩm.'
            });
            this.showAddProductModal = false;
            this.addProductModalOpen = false;
            alert('Đã thêm sản phẩm "' + this.newProdForm.name + '" vào kho hệ thống!');
        },

        adminSaveRestock() {
            if (!this.restockForm.productId) {
                alert('Vui lòng chọn sản phẩm cần nhập thêm!');
                return;
            }
            const prod = this.products.find(p => p.id == this.restockForm.productId);
            if (prod) {
                const addQty = parseInt(this.restockForm.quantity) || 50;
                if (this.restockForm.branch === 'Q1' || this.restockForm.branch === 'HN') {
                    prod.stockQ1 = (Number(prod.stockQ1 || prod.q1) || 0) + addQty;
                    prod.q1 = prod.stockQ1;
                } else if (this.restockForm.branch === 'Q7') {
                    prod.stockQ7 = (Number(prod.stockQ7 || prod.q7) || 0) + addQty;
                    prod.q7 = prod.stockQ7;
                } else {
                    prod.stockBT = (Number(prod.stockBT || prod.bt) || 0) + addQty;
                    prod.bt = prod.stockBT;
                }

                this.showRestockModal = false;
                this.restockModalOpen = false;
                alert('Đã nhập thêm ' + addQty + ' sản phẩm "' + prod.name + '" vào chi nhánh thành công! Tổng tồn kho mới: ' + this.getSafeTotalStock(prod));
            }
        },

        // Chat CSKH
        sendChatMessage() {
            const text = (this.newChatMessage || '').trim();
            if (!text) return;

            this.chatMessages.push({
                sender: 'user',
                text: text,
                time: new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' })
            });
            this.newChatMessage = '';

            setTimeout(() => {
                const box = document.getElementById('chat-messages-box');
                if (box) box.scrollTop = box.scrollHeight;
            }, 50);

            setTimeout(() => {
                let reply = 'Cảm ơn quý khách đã liên hệ! Bác sĩ thú y trực ban đã ghi nhận tình trạng của bé và sẽ phản hồi chi tiết trong ít phút.';
                const lower = text.toLowerCase();
                if (lower.includes('tiêm') || lower.includes('vắc xin') || lower.includes('vaccine')) {
                    reply = 'Dạ về lịch tiêm phòng, PetCare360 hiện có sẵn đầy đủ vắc-xin 7 bệnh chó và 4 bệnh mèo nhập khẩu từ Pháp và Mỹ. Bác sĩ luôn khám sàng lọc miễn phí trước khi tiêm. Bạn có thể đặt lịch ngay trong mục Dịch Vụ nhé!';
                } else if (lower.includes('spa') || lower.includes('tắm') || lower.includes('tỉa')) {
                    reply = 'Dạ gói Spa Cắt Tỉa Lông chuẩn 5 bước tại PetCare360 đang có ưu đãi tặng sấy ion âm dưỡng lông và vệ sinh tai móng trọn gói. Bạn muốn đặt lịch cho bé vào ngày nào ạ?';
                } else if (lower.includes('cấp cứu') || lower.includes('khẩn cấp') || lower.includes('ngộ độc')) {
                    reply = '🚨 BÁC SĨ CẤP CỨU ĐANG KẾT NỐI: Vui lòng giữ bình tĩnh, đặt bé nằm nghiêng nơi thoáng mát. Đội xe cấp cứu PetCare360 có thể đón bé ngay qua hotline khẩn cấp 1900 6868!';
                }

                this.chatMessages.push({
                    sender: 'bot',
                    text: reply,
                    time: new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' })
                });

                setTimeout(() => {
                    const box = document.getElementById('chat-messages-box');
                    if (box) box.scrollTop = box.scrollHeight;
                }, 50);
            }, 600);
        },

        sendQuickChat(promptText) {
            this.newChatMessage = promptText;
            this.sendChatMessage();
        },

        setOrderTypeFilter(type) {
            this.currentOrderTypeTab = type;
        },

        showToast(msg) {
            if (!this.toastNotification) {
                this.toastNotification = { show: false, message: '' };
            }
            this.toastNotification.message = msg;
            this.toastNotification.show = true;
            if (this._toastTimer) clearTimeout(this._toastTimer);
            this._toastTimer = setTimeout(() => {
                if (this.toastNotification) this.toastNotification.show = false;
            }, 2800);
            console.log('[PetCare360 Toast]:', msg);
        },

        toggleDarkMode() {
            // Deprecated as per user request
        },

        refreshChart() {
            alert('Đã cập nhật số liệu biểu đồ phân tích thời gian thực!');
            this.renderRevenueChart();
        },

        
        // ==================== METHOD HELPERS MỚI ====================
        
        // 1. SẢN PHẨM DETAIL HELPERS
        selectProductForDetail(prod) {
            this.selectedProductDetailId = prod.id;
            this.mainProductImage = prod.image || prod.img;
            this.productDetailQty = 1;
            this.activeCustomerTab = 'shop';
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        get currentProductDetail() {
            return this.products.find(p => p.id === this.selectedProductDetailId) || this.products[0];
        },

        get currentProductDetailPrice() {
            return this.currentPrice;
        },

        // PDP VARIANT & PRICING ENGINE
        get selectedVariant() {
            const prod = this.currentProductDetail;
            if (prod && prod.variantConfig && prod.variantConfig.weights && prod.variantConfig.weights.length > 0) {
                const found = prod.variantConfig.weights.find(w => w.label === this.selectedWeight);
                if (found) return found;
                return prod.variantConfig.weights[0];
            }
            return { label: 'Tiêu chuẩn', price: (prod ? prod.price : 395000) };
        },

        get currentPrice() {
            return this.selectedVariant ? this.selectedVariant.price : (this.currentProductDetail?.price || 395000);
        },

        get currentProductDetailTotalPrice() {
            return this.currentPrice * (Number(this.productDetailQty) || 1);
        },

        selectProductWeight(w) {
            this.selectedWeight = w.label;
        },

        // CART ITEM QUANTITY ENGINE (Realtime update & badge reactivity)
        updateCartItemQuantity(id, variantLabel, newQty) {
            const item = this.cart.find(i => i.id === id || (i.productId === id && (i.variantLabel === variantLabel || i.variant === variantLabel)));
            if (!item) return;
            const targetQty = Number(newQty);
            if (targetQty <= 0) {
                if (confirm('Bạn có chắc muốn xóa sản phẩm "' + item.name + '" khỏi giỏ hàng?')) {
                    this.cart = this.cart.filter(i => i !== item);
                }
            } else {
                item.qty = targetQty;
                item.quantity = targetQty;
            }
        },

        // PDP CUSTOMER REVIEW & LIGHTBOX ACTIONS
        openProductReviewModal() {
            this.showCustomerReviewFormModal = true;
            this.newReviewRating = 5;
            this.hoverReviewRating = 0;
            this.newReviewText = '';
            this.newReviewMediaList = [];
        },

        handleReviewMediaUpload(e) {
            const files = e.target.files;
            if (!files || files.length === 0) return;
            for (let i = 0; i < files.length; i++) {
                const file = files[i];
                const reader = new FileReader();
                reader.onload = (event) => {
                    this.newReviewMediaList.push(event.target.result);
                };
                reader.readAsDataURL(file);
            }
        },

        removeReviewMedia(index) {
            this.newReviewMediaList.splice(index, 1);
        },

        submitCustomerReview() {
            if (this.newReviewRating === 0 || !this.newReviewText.trim()) return;
            const newRev = {
                id: Date.now(),
                author: this.customerProfile?.name || 'Nguyễn Phương Thảo',
                user: this.customerProfile?.name || 'Nguyễn Phương Thảo',
                avatar: this.customerProfile?.avatar || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80',
                rating: this.newReviewRating,
                stars: Array.from({ length: this.newReviewRating }, (_, i) => i + 1),
                date: 'Hôm nay',
                variant: this.currentProductDetail?.variantConfig ? (this.selectedWeight || '3kg') : 'Tiêu chuẩn',
                comment: this.newReviewText.trim(),
                photos: [...this.newReviewMediaList],
                photo: this.newReviewMediaList[0] || '',
                verified: true,
                likes: 0,
                isLiked: false,
                showReplyInput: false,
                newReplyText: '',
                replies: []
            };
            this.productReviewsList.unshift(newRev);
            this.showCustomerReviewFormModal = false;
            alert('🎉 Cảm ơn bạn đã gửi đánh giá sản phẩm thành công!');
        },

        openReviewPhotosLightbox() {
            const allPhotos = [];
            (this.productReviewsList || []).forEach(r => {
                if (r.photos && r.photos.length) {
                    r.photos.forEach(p => { if (p && !allPhotos.includes(p)) allPhotos.push(p); });
                } else if (r.photo && !allPhotos.includes(r.photo)) {
                    allPhotos.push(r.photo);
                }
            });
            if (allPhotos.length === 0) {
                allPhotos.push(this.mainProductImage || this.currentProductDetail?.image || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=800&q=80');
            }
            this.reviewLightboxImages = allPhotos;
            this.reviewLightboxIndex = 0;
            this.showReviewLightboxModal = true;
        },

        openSingleReviewLightbox(photos, idx) {
            if (photos && photos.length) {
                this.reviewLightboxImages = photos;
                this.reviewLightboxIndex = idx || 0;
            } else {
                this.reviewLightboxImages = [this.mainProductImage];
                this.reviewLightboxIndex = 0;
            }
            this.showReviewLightboxModal = true;
        },

        reviewLightboxPrev() {
            if (!this.reviewLightboxImages.length) return;
            this.reviewLightboxIndex = (this.reviewLightboxIndex - 1 + this.reviewLightboxImages.length) % this.reviewLightboxImages.length;
        },

        reviewLightboxNext() {
            if (!this.reviewLightboxImages.length) return;
            this.reviewLightboxIndex = (this.reviewLightboxIndex + 1) % this.reviewLightboxImages.length;
        },

        toggleReviewLike(rev) {
            rev.isLiked = !rev.isLiked;
            rev.likes = (rev.likes || 0) + (rev.isLiked ? 1 : -1);
        },

        addReviewReply(rev) {
            if (!rev.newReplyText || !rev.newReplyText.trim()) return;
            if (!rev.replies) rev.replies = [];
            rev.replies.push({
                author: this.customerProfile?.name || 'Khách hàng',
                isAdmin: false,
                date: 'Vừa xong',
                content: rev.newReplyText.trim()
            });
            rev.newReplyText = '';
            rev.showReplyInput = false;
        },

        getRatingLabel(r) {
            const labels = { 1: 'Rất tệ (1 sao)', 2: 'Không hài lòng (2 sao)', 3: 'Bình thường (3 sao)', 4: 'Hài lòng (4 sao)', 5: 'Tuyệt vời (5 sao)' };
            return labels[r] || 'Chọn mức đánh giá';
        },

        // CHECKOUT STEP 2 BOOKING & PETSHIP VALIDATION GETTERS
        get isCheckoutBookingFormValid() {
            if (!this.hasService) return true;
            const name = (this.checkoutBookingContactName || '').trim();
            const phone = (this.checkoutBookingContactPhone || '').trim().replace(/\s/g, '');
            const vnPhoneRegex = /^(0[35789])[0-9]{8}$/;
            if (name.length < 2) return false;
            if (!phone || !vnPhoneRegex.test(phone)) return false;
            if (this.hasPetShip) {
                const addr = this.checkoutPetShipAddress;
                if (!addr.street || addr.street.trim().length < 5) return false;
                if (!addr.district || !addr.district.trim()) return false;
                if (!addr.ward || !addr.ward.trim()) return false;
            }
            return true;
        },

        get isStep2CheckoutValid() {
            return this.isCheckoutShippingFormValid && this.isCheckoutBookingFormValid;
        },


        get currentProductOriginalPrice() {
            return Math.round(this.currentProductDetailPrice * 1.25);
        },

        incProductQty() {
            this.productDetailQty++;
        },

        decProductQty() {
            if (this.productDetailQty > 1) this.productDetailQty--;
        },

        addProductDetailToCart() {
            const prod = this.currentProductDetail;
            const hasVariants = prod.variantConfig && prod.variantConfig.weights && prod.variantConfig.weights.length > 0;
            const variantLabel = hasVariants ? (this.selectedWeight + (this.selectedFlavor && prod.variantConfig.flavors ? (' - ' + (prod.variantConfig.flavors.find(f => f.id === this.selectedFlavor)?.label || this.selectedFlavor)) : '')) : 'Tiêu chuẩn';
            const unitPrice = this.currentPrice;
            const qty = Math.max(1, Number(this.productDetailQty) || 1);

            const item = {
                id: 'PD-' + prod.id + '-' + variantLabel.replace(/[\s\W]+/g, '_'),
                productId: prod.id,
                name: prod.name,
                variantLabel: variantLabel,
                variant: variantLabel,
                unitPrice: unitPrice,
                price: unitPrice,
                quantity: qty,
                qty: qty,
                img: this.mainProductImage || prod.image || prod.img,
                image: this.mainProductImage || prod.image || prod.img,
                isProduct: true,
                isService: false
            };
            const existing = this.cart.find(i => i.id === item.id);
            if (existing) {
                existing.qty += qty;
                existing.quantity = (existing.quantity || 0) + qty;
            } else {
                this.cart.push(item);
            }
            alert('🎉 Đã thêm ' + qty + ' sản phẩm "' + item.name + ' (' + item.variantLabel + ')" vào giỏ hàng!');
        },

        buyNowProductDetail() {
            this.addProductDetailToCart();
            this.activeCustomerTab = 'cart';
            this.cartStep = 2;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        // SHOP CATALOG METHODS & GETTERS
        openProductDetailPage(prod) {
            if (!prod) return;
            this.selectedProductDetailId = prod.id;
            this.mainProductImage = prod.image || prod.img;
            this.productThumbnails = [
                prod.image || prod.img,
                'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=400&q=80',
                'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?auto=format&fit=crop&w=400&q=80',
                'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=400&q=80'
            ];
            this.shopViewMode = 'detail';
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        // CAROUSEL NAVIGATION SCROLL METHODS
        scrollBestSellerLeft() {
            const el = document.getElementById('homepage-bestseller-carousel');
            if (el) el.scrollBy({ left: -320, behavior: 'smooth' });
        },
        scrollBestSellerRight() {
            const el = document.getElementById('homepage-bestseller-carousel');
            if (el) el.scrollBy({ left: 320, behavior: 'smooth' });
        },
        scrollSimilarLeft() {
            const el = document.getElementById('product-detail-similar-carousel');
            if (el) el.scrollBy({ left: -320, behavior: 'smooth' });
        },
        scrollSimilarRight() {
            const el = document.getElementById('product-detail-similar-carousel');
            if (el) el.scrollBy({ left: 320, behavior: 'smooth' });
        },

        // HELPER MAP GIÁ KHÁCH SẠN THEO CÂN NẶNG (ĐỐI CHIẾU CHÍNH XÁC 7 MỐC SIZE BẢNG GIÁ)
        getPetHotelPriceByWeight(weight) {
            const w = parseFloat(weight) || 5;
            if (w < 2) return 200000;
            if (w <= 5) return 250000;
            if (w <= 8) return 300000;
            if (w <= 12) return 350000;
            if (w <= 18) return 400000;
            if (w <= 25) return 450000;
            return 500000;
        },

        getPetHotelWeightLabel(weight) {
            const w = parseFloat(weight) || 5;
            if (w < 2) return 'Dưới 2kg';
            if (w <= 5) return '2kg - 5kg';
            if (w <= 8) return '5kg - 8kg';
            if (w <= 12) return '8kg - 12kg';
            if (w <= 18) return '12kg - 18kg';
            if (w <= 25) return '18kg - 25kg';
            return 'Trên 25kg';
        },

        getGroomingWeightTier(weight) {
            const w = parseFloat(weight) || 5;
            if (w < 2) return '< 2kg';
            if (w <= 5) return '2kg-5kg';
            if (w <= 8) return '5kg-8kg';
            if (w <= 12) return '8kg-12kg';
            if (w <= 18) return '12kg-18kg';
            if (w <= 25) return '18kg-25kg';
            if (w <= 35) return '25kg-35kg';
            return '> 35kg';
        },

        getHotelWeightTier(weight) {
            const w = parseFloat(weight) || 5;
            if (w < 2) return 'Dưới 2kg';
            if (w <= 5) return '2kg - 5kg';
            if (w <= 8) return '5kg - 8kg';
            if (w <= 12) return '8kg - 12kg';
            if (w <= 18) return '12kg - 18kg';
            if (w <= 25) return '18kg - 25kg';
            return 'Trên 25kg';
        },

        isGroomingCellSelected(weight, type) {
            if (this.currentPetGroomingTier !== weight) return false;
            if (type === 'spa') return this.groomingIncludeSpa;
            if (type === 'grooming') return this.groomingCutType === 'grooming';
            if (type === 'shave') return this.groomingCutType === 'shave';
            return false;
        },

        toggleGroomingSpa() {
            this.groomingIncludeSpa = !this.groomingIncludeSpa;
            // Bắt buộc chọn 1 nếu không chọn Spa
            if (!this.groomingIncludeSpa && (!this.groomingCutType || this.groomingCutType === 'none')) {
                this.groomingCutType = 'grooming';
            }
            this.recalcGroomingService();
        },

        setGroomingCutType(type) {
            if (type === 'none' && !this.groomingIncludeSpa) {
                this.groomingIncludeSpa = true;
            }
            this.groomingCutType = type;
            this.recalcGroomingService();
        },

        recalcGroomingService() {
            const row = this.groomingPriceList.find(r => r.weight === this.currentPetGroomingTier) || this.groomingPriceList[2];
            let price = 0;
            let labelParts = [];

            if (this.groomingIncludeSpa) {
                labelParts.push('Spa Tắm Sấy');
            }
            if (this.groomingCutType === 'grooming') {
                labelParts.push('Cắt Tỉa Lông (Grooming)');
            } else if (this.groomingCutType === 'shave') {
                labelParts.push('Cạo Lông (Shave)');
            }

            if (this.groomingIncludeSpa && this.groomingCutType === 'grooming') {
                price = row.grooming;
            } else if (this.groomingIncludeSpa && this.groomingCutType === 'shave') {
                price = row.shave;
            } else if (this.groomingIncludeSpa && (!this.groomingCutType || this.groomingCutType === 'none')) {
                price = row.spa;
            } else if (!this.groomingIncludeSpa && this.groomingCutType === 'grooming') {
                price = Math.max(150000, row.grooming - row.spa);
            } else if (!this.groomingIncludeSpa && this.groomingCutType === 'shave') {
                price = Math.max(120000, row.shave - row.spa);
            } else {
                price = row.spa;
            }

            this.baseServicePrice = price;
            this.selectedBaseService = {
                id: 'grooming_' + (this.groomingCutType || 'spa') + '_' + row.weight,
                name: 'Grooming & Spa: ' + labelParts.join(' + ') + ' (' + row.weight + ')',
                category: 'grooming',
                type: this.groomingCutType || 'spa',
                weightTier: row.weight,
                price: price,
                duration: (this.groomingIncludeSpa && this.groomingCutType && this.groomingCutType !== 'none') ? '90 - 120 phút' : '45 - 60 phút'
            };
            this.serviceBookingForm.serviceName = this.selectedBaseService.name;
        },

        selectGroomingCell(row, type) {
            this.currentPetGroomingTier = row.weight;
            this.selectedWeightSize = row.weight;
            if (type === 'spa') {
                this.toggleGroomingSpa();
            } else if (type === 'grooming') {
                if (this.groomingCutType === 'grooming' && this.groomingIncludeSpa) {
                    this.groomingCutType = 'none';
                } else {
                    this.groomingCutType = 'grooming';
                }
                this.recalcGroomingService();
            } else if (type === 'shave') {
                if (this.groomingCutType === 'shave' && this.groomingIncludeSpa) {
                    this.groomingCutType = 'none';
                } else {
                    this.groomingCutType = 'shave';
                }
                this.recalcGroomingService();
            }
            const bookingBox = document.getElementById('pet-service-booking-box');
            if (bookingBox) {
                bookingBox.scrollIntoView({ behavior: 'smooth' });
            }
        },

        selectHotelOption(plan, optionType) {
            const isOvernight = (optionType === 'overnight');
            const price = isOvernight ? plan.price : (plan.daycarePrice || Math.round(plan.price * 0.7));
            const duration = isOvernight ? 'Lưu trú theo ngày (24h)' : 'Bán trú trong ngày (09:00 - 19:00)';
            const label = isOvernight ? 'Lưu Trú Qua Đêm (24h)' : 'Bán Trú Daycare (09:00 - 19:00)';
            this.currentPetHotelTier = plan.size;
            this.selectedBaseService = {
                id: 'hotel_' + optionType + '_' + plan.size,
                name: 'Khách Sạn Thú Cưng 5 Sao (' + label + ' - Size ' + plan.size + ')',
                category: 'hotel',
                type: optionType,
                weightTier: plan.size,
                price: price,
                duration: duration
            };
            this.baseServicePrice = price;
            this.selectedWeightSize = plan.size;
            this.serviceBookingForm.serviceName = this.selectedBaseService.name;
            this.hotelPopupRow = null;
            const bookingBox = document.getElementById('pet-service-booking-box');
            if (bookingBox) {
                bookingBox.scrollIntoView({ behavior: 'smooth' });
            }
        },

        selectVaccineRow(vac) {
            this.selectedBaseService = {
                id: 'vaccine_' + vac.name,
                name: vac.name,
                category: 'vaccine',
                type: 'vaccine',
                weightTier: 'Tất cả kích thước',
                price: vac.price,
                duration: vac.duration || '30 phút'
            };
            this.baseServicePrice = vac.price;
            this.serviceBookingForm.serviceName = vac.name;
            const bookingBox = document.getElementById('pet-service-booking-box');
            if (bookingBox) {
                bookingBox.scrollIntoView({ behavior: 'smooth' });
            }
        },

        syncPetBookingDetails(petId) {
            const id = Number(petId);
            const pet = this.pets.find(p => p.id === id) || this.pets[0];
            if (pet) {
                this.serviceBookingForm.petId = pet.id;
                this.petBookingDetail.petId = pet.id;
                this.petBookingDetail.name = pet.name;
                this.petBookingDetail.species = pet.species || pet.type || 'Chó';
                this.petBookingDetail.breed = pet.breed || 'Corgi';
                this.petBookingDetail.weight = parseFloat(pet.weight) || 5;
                this.petBookingDetail.age = pet.age || '2 tuổi';
                this.petBookingDetail.gender = pet.gender || 'Đực';
                this.petBookingDetail.allergies = pet.allergies || 'Không dị ứng';
                this.petBookingDetail.diet = pet.diet || 'Ăn hạt tiêu chuẩn';
                this.petBookingDetail.vaccinePhoto = pet.avatar || pet.image;

                // Tự động map mốc cân nặng sang Grooming & Hotel
                const w = this.petBookingDetail.weight;
                this.currentPetGroomingTier = this.getGroomingWeightTier(w);
                this.currentPetHotelTier = this.getHotelWeightTier(w);
                this.selectedWeightSize = this.currentPetHotelTier;

                if (this.servicePricingTab === 'hotel') {
                    const hotelPrice = this.getPetHotelPriceByWeight(w);
                    this.baseServicePrice = hotelPrice;
                    this.selectedBaseService = {
                        id: 'hotel_overnight_' + this.currentPetHotelTier,
                        name: 'Khách Sạn Thú Cưng Tiêu Chuẩn 5 Sao (Lưu Trú Qua Đêm 24h - ' + this.currentPetHotelTier + ')',
                        category: 'hotel',
                        type: 'overnight',
                        weightTier: this.currentPetHotelTier,
                        price: hotelPrice,
                        duration: 'Lưu trú theo ngày (24h)'
                    };
                    this.serviceBookingForm.serviceName = this.selectedBaseService.name;
                } else if (this.servicePricingTab === 'grooming' || this.servicePricingTab === 'spa') {
                    this.recalcGroomingService();
                } else if (this.servicePricingTab === 'vaccine') {
                    if (!this.selectedBaseService || this.selectedBaseService.category !== 'vaccine') {
                        this.selectVaccineRow(this.vaccinePriceList[0]);
                    }
                }
            }
        },

        selectPetHotelWeightPlan(plan) {
            this.baseServicePrice = Number(plan.price) || 200000;
            this.selectedWeightSize = plan.size;
            this.serviceBookingForm.serviceName = 'Khách Sạn Thú Cưng Tiêu Chuẩn 5 Sao (' + plan.size + ')';
            const bookingBox = document.getElementById('pet-service-booking-box');
            if (bookingBox) {
                bookingBox.scrollIntoView({ behavior: 'smooth' });
            }
        },

        backToShopCatalog() {
            this.shopViewMode = 'catalog';
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        resetShopFilters() {
            this.shopCategory = '';
            this.shopSpecies = '';
            this.shopProductType = '';
            this.shopBrand = '';
            this.shopMaxPrice = 1500000;
            this.shopExpressShip = false;
            this.shopSortBy = 'newest';
            this.searchQuery = '';
            this.shopCurrentPage = 1;
        },

        scrollToCatalogGrid() {
            const el = document.getElementById('shopCatalogSection');
            if (el) el.scrollIntoView({ behavior: 'smooth' });
        },

        get filteredCatalogProducts() {
            let list = [...this.products];
            if (this.shopCategory) {
                list = list.filter(p => p.category === this.shopCategory);
            }
            if (this.shopSpecies) {
                list = list.filter(p => p.species === this.shopSpecies || (this.shopSpecies === 'Thỏ' && (p.category.includes('Phụ kiện') || p.category.includes('Dinh dưỡng'))));
            }
            if (this.shopProductType) {
                list = list.filter(p => p.productType === this.shopProductType);
            }
            if (this.shopBrand) {
                list = list.filter(p => p.brandName === this.shopBrand || (p.brand && p.brand.toLowerCase().includes(this.shopBrand.toLowerCase())));
            }
            if (this.shopMaxPrice) {
                list = list.filter(p => p.price <= this.shopMaxPrice);
            }
            if (this.shopExpressShip) {
                list = list.filter(p => p.expressShip === true);
            }
            if (this.searchQuery && this.searchQuery.trim()) {
                const q = this.searchQuery.toLowerCase().trim();
                list = list.filter(p => p.name.toLowerCase().includes(q) || (p.brand && p.brand.toLowerCase().includes(q)) || (p.category && p.category.toLowerCase().includes(q)));
            }
            if (this.shopSortBy === 'bestseller') {
                list.sort((a, b) => (b.sold || 0) - (a.sold || 0));
            } else if (this.shopSortBy === 'price_asc') {
                list.sort((a, b) => a.price - b.price);
            } else if (this.shopSortBy === 'price_desc') {
                list.sort((a, b) => b.price - a.price);
            } else {
                list.sort((a, b) => b.id - a.id);
            }
            return list;
        },

        get shopTotalPages() {
            return Math.max(1, Math.ceil(this.filteredCatalogProducts.length / this.shopPageSize));
        },

        get paginatedCatalogProducts() {
            const start = (this.shopCurrentPage - 1) * this.shopPageSize;
            return this.filteredCatalogProducts.slice(start, start + this.shopPageSize);
        },

        // GETTERS CHO CAROUSEL HOMEPAGE VÀ PRODUCT DETAIL
        get bestSellingProducts() {
            if (!this.products || this.products.length === 0) return this.fallbackRelatedProducts;
            return [...this.products].sort((a, b) => (b.sold || 0) - (a.sold || 0)).slice(0, 8);
        },

        get similarProductsList() {
            if (!this.products || this.products.length === 0) return this.fallbackRelatedProducts;
            const curId = this.selectedProductDetailId;
            const cur = this.currentProductDetail;
            let list = this.products.filter(p => p.id !== curId);
            if (cur && cur.category) {
                const sameCat = list.filter(p => p.category === cur.category);
                const diffCat = list.filter(p => p.category !== cur.category);
                list = [...sameCat, ...diffCat];
            }
            if (list.length < 4) {
                list = [...list, ...this.fallbackRelatedProducts];
            }
            return list.slice(0, 8);
        },

        // 2. DỊCH VỤ MATRIX & BOOKING HELPERS
        get hotelTotalDays() {
            if (!this.serviceBookingForm.hotelCheckInDate || !this.serviceBookingForm.hotelCheckOutDate) return 1;
            const d1 = new Date(this.serviceBookingForm.hotelCheckInDate);
            const d2 = new Date(this.serviceBookingForm.hotelCheckOutDate);
            const diffTime = d2.getTime() - d1.getTime();
            const diffDays = Math.round(diffTime / (1000 * 3600 * 24));
            return diffDays > 0 ? diffDays : 1;
        },

        get hotelFee() {
            const base = (this.baseServicePrice !== undefined && this.baseServicePrice !== null) 
                ? Number(this.baseServicePrice) 
                : this.getPetHotelPriceByWeight(this.petBookingDetail.weight || 5);
            return base * this.hotelTotalDays;
        },

        get totalAddonsCost() {
            let cost = 0;
            if (this.serviceBookingForm.addOnMassage || (Array.isArray(this.serviceBookingForm.addons) && this.serviceBookingForm.addons.includes('massage'))) cost += 50000;
            if (this.serviceBookingForm.addOnFurDetangle || (Array.isArray(this.serviceBookingForm.addons) && this.serviceBookingForm.addons.includes('detangle'))) cost += 80000;
            if (this.serviceBookingForm.addOnWalk || (Array.isArray(this.serviceBookingForm.addons) && this.serviceBookingForm.addons.includes('walk'))) cost += 40000;
            return cost;
        },

        get petShipCost() {
            return (this.serviceBookingForm.usePetShip || this.serviceBookingForm.needPetShip) ? 60000 : 0;
        },

        get totalServiceCost() {
            if (this.servicePricingTab === 'hotel') {
                return this.hotelFee + this.totalAddonsCost + this.petShipCost;
            } else {
                const base = (this.baseServicePrice !== undefined && this.baseServicePrice !== null) 
                    ? Number(this.baseServicePrice) 
                    : 380000;
                return base + this.totalAddonsCost + this.petShipCost;
            }
        },

        get depositAmount() {
            if (this.servicePricingTab === 'hotel') {
                return Math.round(this.totalServiceCost / 2);
            }
            return 0; // Grooming & Vaccine không tính cọc
        },

        get remainingAmount() {
            if (this.servicePricingTab === 'hotel') {
                return this.totalServiceCost - this.depositAmount;
            }
            return 0;
        },

        get currentServiceBookingCost() {
            return this.totalServiceCost;
        },

        toggleServiceAddon(addonId) {
            const idx = this.serviceBookingForm.addons.indexOf(addonId);
            if (idx > -1) this.serviceBookingForm.addons.splice(idx, 1);
            else this.serviceBookingForm.addons.push(addonId);
        },

        submitServiceBooking(isDirectCheckout = false) {
            const pet = this.pets.find(p => p.id === Number(this.serviceBookingForm.petId)) || this.pets[0];
            const petWeight = pet ? (parseFloat(pet.weight) || 5) : (parseFloat(this.petBookingDetail.weight) || 5);
            const isHotel = (this.servicePricingTab === 'hotel');
            const totalCost = this.totalServiceCost;
            const deposit = isHotel ? this.depositAmount : totalCost;
            const remaining = isHotel ? this.remainingAmount : 0;
            const paymentType = isHotel ? 'deposit_50' : 'full';

            const bookingItem = {
                id: 'SERV-BOOK-' + Date.now(),
                name: (this.selectedBaseService ? this.selectedBaseService.name : (this.serviceBookingForm.serviceName || 'Dịch Vụ Thú Cưng PetCare360')),
                variant: (pet ? pet.name : 'Bé cưng') + ' (' + (isHotel ? (this.serviceBookingForm.hotelCheckInDate + ' -> ' + this.serviceBookingForm.hotelCheckOutDate) : (this.serviceBookingForm.date + ' ' + (this.serviceBookingForm.timeSlot || '09:30'))) + ')',
                price: deposit,
                depositPaid: deposit,
                depositAmount: isHotel ? deposit : 0,
                totalCost: totalCost,
                remainingBalance: remaining,
                paymentStatus: isHotel ? 'deposit_paid' : 'unpaid',
                statusText: isHotel ? 'Đã cọc 50%' : 'Chờ thanh toán',
                payment_type: paymentType,
                img: isHotel ? 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=400&q=80' : 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=400&q=80',
                image: isHotel ? 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=400&q=80' : 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=400&q=80',
                qty: 1,
                quantity: 1,
                isService: true,
                bookingDetails: {
                    petName: pet ? pet.name : 'Bơ',
                    petWeight: petWeight,
                    sizeTier: isHotel ? this.currentPetHotelTier : this.currentPetGroomingTier,
                    payment_type: paymentType,
                    basePrice: this.baseServicePrice,
                    totalCost: totalCost,
                    depositAmount: isHotel ? deposit : 0,
                    remainingBalance: remaining,
                    paymentStatus: isHotel ? 'deposit_paid' : 'unpaid',
                    branch: 'Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Quận 1, TPHCM',
                    date: isHotel ? this.serviceBookingForm.hotelCheckInDate : this.serviceBookingForm.date,
                    checkInDate: isHotel ? this.serviceBookingForm.hotelCheckInDate : null,
                    checkOutDate: isHotel ? this.serviceBookingForm.hotelCheckOutDate : null,
                    checkInTime: isHotel ? this.serviceBookingForm.hotelCheckInTime : null,
                    checkOutTime: isHotel ? this.serviceBookingForm.hotelCheckOutTime : null,
                    totalDays: isHotel ? this.hotelTotalDays : 1,
                    slot: isHotel ? (this.serviceBookingForm.hotelCheckInTime + ' -> ' + this.serviceBookingForm.hotelCheckOutTime) : (this.serviceBookingForm.timeSlot || this.serviceBookingForm.slot),
                    addons: [
                        ...(this.serviceBookingForm.addOnMassage ? ['Tắm massage sục khí bọt Nano (+50.000đ)'] : []),
                        ...(this.serviceBookingForm.addOnFurDetangle ? ['Gỡ rối lông & Phục hồi keratin (+80.000đ)'] : []),
                        ...(this.serviceBookingForm.addOnWalk ? ['Dắt đi dạo sân cỏ tự nhiên 30p (+40.000đ)'] : [])
                    ],
                    needPetShip: !!(this.serviceBookingForm.usePetShip || this.serviceBookingForm.needPetShip),
                    petShipAddress: this.serviceBookingForm.petShipAddress,
                    notes: this.serviceBookingForm.specialNotes
                }
            };

            this.cart.push(bookingItem);

            const newOrderCode = '#' + Math.floor(100000 + Math.random() * 900000);
            const newOrderId = 'ORD-' + Math.floor(1000 + Math.random() * 9000);
            const todayStr = new Date().toLocaleDateString('vi-VN');

            const serviceOrder = {
                id: newOrderId,
                orderCode: newOrderCode,
                date: todayStr,
                status: 'pending',
                statusText: isHotel ? 'Đã cọc 50%' : 'Chờ thanh toán',
                payment_type: paymentType,
                badgeColor: isHotel ? 'bg-orange-100 text-orange-800 border-orange-200' : 'bg-blue-100 text-blue-800 border-blue-200',
                paymentMethod: isHotel ? 'Chuyển khoản / Cọc 50%' : 'Thanh toán trực tuyến 100%',
                paymentMethodLabel: isHotel ? ('Đã cọc 50% (' + this.formatCurrency(deposit) + ')') : 'Thanh toán 100%',
                paymentStatus: isHotel ? 'deposit_paid' : 'unpaid',
                total: totalCost,
                totalAmount: totalCost,
                depositAmount: isHotel ? deposit : 0,
                remainingBalance: remaining,
                customer: this.customerProfile.name,
                phone: this.customerProfile.phone,
                summary: bookingItem.name + (isHotel ? (' - Cọc: ' + this.formatCurrency(deposit) + ' (Còn: ' + this.formatCurrency(remaining) + ')') : (' - ' + this.formatCurrency(totalCost))),
                branch: 'Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Quận 1, TPHCM',
                recipient: {
                    receiver: this.customerProfile.name,
                    phone: this.customerProfile.phone,
                    address: this.serviceBookingForm.petShipAddress || this.customerProfile.address
                },
                items: [bookingItem]
            };

            this.customerOrdersEnhanced.unshift(serviceOrder);
            this.orders.unshift(serviceOrder);

            this.appointments.unshift({
                id: 'APT-' + Math.floor(1000 + Math.random() * 9000),
                customer: this.customerProfile.name,
                customerName: this.customerProfile.name,
                customerPhone: this.customerProfile.phone,
                pet: pet ? pet.name : 'Bơ',
                petName: pet ? pet.name : 'Bơ',
                petType: pet ? (pet.species || pet.type) : 'Chó',
                service: bookingItem.name,
                serviceName: bookingItem.name,
                date: isHotel ? this.serviceBookingForm.hotelCheckInDate : this.serviceBookingForm.date,
                time: isHotel ? (this.serviceBookingForm.hotelCheckInTime + ' - ' + this.serviceBookingForm.hotelCheckOutTime) : (this.serviceBookingForm.timeSlot || '09:30'),
                branch: 'Cơ sở Chính: 88 Nguyễn Thị Minh Khai, Quận 1, TPHCM',
                status: 'CONFIRMED',
                paymentStatus: isHotel ? 'deposit_paid' : 'full_paid',
                depositAmount: isHotel ? deposit : 0,
                remainingBalance: remaining,
                note: isHotel ? ('Đã cọc 50% (' + this.formatCurrency(deposit) + '). Còn thu: ' + this.formatCurrency(remaining) + ' khi trả pet.') : 'Thanh toán 100% dịch vụ.'
            });

            if (isDirectCheckout) {
                this.activeCustomerTab = 'cart';
                this.cartStep = 2;
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else {
                alert('🛒 Đã thêm dịch vụ ' + bookingItem.name + ' vào giỏ hàng thành công! Bạn có thể tiếp tục mua sắm hoặc xem các dịch vụ khác.');
            }
        },

        addServiceBookingToCart() {
            this.submitServiceBooking(true);
        },

        openPetBookingDetailModal(petId) {
            const pet = this.pets.find(p => p.id === petId) || this.pets[0];
            if (pet) {
                this.petBookingDetail.petId = pet.id;
                this.petBookingDetail.name = pet.name;
                this.petBookingDetail.species = pet.species || pet.type || 'Chó';
                this.petBookingDetail.breed = pet.breed || 'Corgi';
                this.petBookingDetail.age = pet.age || '2 tuổi';
                this.petBookingDetail.gender = pet.gender || 'Đực';
                this.petBookingDetail.isNeutered = true;
                this.petBookingDetail.weight = Number(pet.weight) || 5.8;
                this.onPetWeightChange();
                this.petBookingDetail.conditions = pet.health || 'Khỏe mạnh bình thường';
                this.petBookingDetail.allergies = pet.allergies || 'Không dị ứng';
            }
            this.showPetBookingDetailModal = true;
        },

        onPetWeightChange() {
            const w = Number(this.petBookingDetail.weight) || 0;
            if (w < 5) this.petBookingDetail.suggestedCage = 'Size S (Phù hợp cún/mèo dưới 5kg, chuồng 60x45x50cm)';
            else if (w <= 10) this.petBookingDetail.suggestedCage = 'Size M (Phù hợp cún 5-10kg, chuồng 80x60x70cm)';
            else if (w <= 20) this.petBookingDetail.suggestedCage = 'Size L (Phù hợp cún 10-20kg, chuồng 100x75x85cm)';
            else this.petBookingDetail.suggestedCage = 'Size XL (Phù hợp cún lớn trên 20kg, phòng Penthouse 120x90x100cm)';
        },

        togglePersonalityTag(tag) {
            const idx = this.petBookingDetail.personalityTags.indexOf(tag);
            if (idx > -1) this.petBookingDetail.personalityTags.splice(idx, 1);
            else this.petBookingDetail.personalityTags.push(tag);
        },

        savePetBookingDetail() {
            this.showPetBookingDetailModal = false;
            alert('🎉 ĐÃ CẬP NHẬT PHIẾU THÔNG TIN THÚ CƯNG! Hồ sơ dịch vụ của bé ' + this.petBookingDetail.name + ' (' + this.petBookingDetail.suggestedCage + ') đã được đồng bộ vào đơn hàng.');
        },

        // 4. PETSHARE360 SOCIAL HELPERS
        handlePostMediaSelect(event) {
            const files = event.target.files;
            if (!files || files.length === 0) return;
            Array.from(files).forEach(file => {
                const isVideo = file.type.startsWith('video');
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.newPostMediaList.push({
                        url: e.target.result,
                        type: isVideo ? 'video' : 'image',
                        name: file.name
                    });
                    this.newPostMedia = this.newPostMediaList[0]?.url || '';
                };
                reader.readAsDataURL(file);
            });
        },

        removePostMedia(index) {
            this.newPostMediaList.splice(index, 1);
            this.newPostMedia = this.newPostMediaList[0]?.url || '';
        },

        selectTaggedPet(pet) {
            this.selectedTaggedPet = pet;
            this.newPostPetId = pet ? pet.id : null;
        },

        insertEmoji(emoji) {
            this.newPostText = (this.newPostText || '') + emoji;
        },

        createSocialPost() {
            const text = (this.newPostText || '').trim();
            const hasMedia = this.newPostMediaList && this.newPostMediaList.length > 0;
            if (!text && !hasMedia) {
                alert('Vui lòng nhập nội dung hoặc thêm ảnh/video bài viết!');
                return;
            }
            const pet = this.selectedTaggedPet || this.pets.find(p => p.id === Number(this.newPostPetId)) || this.pets[0];
            const mediaUrls = hasMedia
                ? this.newPostMediaList.map(m => m.url)
                : (this.newPostMedia ? [this.newPostMedia] : []);

            const post = {
                id: Date.now(),
                authorId: this.customerProfile.id || 1,
                author: this.customerProfile.name,
                petName: pet ? pet.name : 'Bé Cưng',
                breed: pet ? pet.breed : 'Thú cưng',
                avatar: this.customerProfile.avatar,
                time: 'Vừa xong',
                content: this.newPostText,
                images: mediaUrls,
                likes: 0,
                isLiked: false,
                isSaved: false,
                likeAnimating: false,
                shares: 0,
                comments: []
            };
            this.socialPosts.unshift(post);
            this.newPostText = '';
            this.newPostMediaList = [];
            this.newPostMedia = '';
            this.selectedTaggedPet = null;
            this.newPostPetId = null;
            this.tagPetPopoverOpen = false;
            this.emojiPickerOpen = false;
            if (this.$refs && this.$refs.postFileInput) {
                this.$refs.postFileInput.value = '';
            }
            this.showToast('🎉 Đăng bài viết lên PetShare360 thành công!');
        },

        toggleLikePost(postId) {
            const p = this.socialPosts.find(item => item.id === postId);
            if (p) {
                p.isLiked = !p.isLiked;
                p.likes += p.isLiked ? 1 : -1;
                p.likeAnimating = true;
                setTimeout(() => { p.likeAnimating = false; }, 400);
            }
        },

        addCommentToPost(postId, commentInputEl) {
            let text = '';
            if (typeof commentInputEl === 'string') {
                text = commentInputEl.trim();
            } else if (commentInputEl && commentInputEl.value !== undefined) {
                text = commentInputEl.value.trim();
            } else if (this.quickCommentText && this.quickCommentText[postId]) {
                text = this.quickCommentText[postId].trim();
            }
            if (!text) return;
            const p = this.socialPosts.find(item => item.id === postId);
            if (p) {
                if (!p.comments) p.comments = [];
                p.comments.push({
                    id: Date.now(),
                    user: this.customerProfile.name,
                    avatar: this.customerProfile.avatar,
                    text: text,
                    time: 'Vừa xong'
                });
                if (commentInputEl && commentInputEl.value !== undefined) {
                    commentInputEl.value = '';
                }
                if (this.quickCommentText) {
                    this.quickCommentText[postId] = '';
                }
                this.showToast('💬 Đã gửi bình luận của bạn!');
            }
        },

        copyPostLink(postId) {
            const p = this.socialPosts.find(item => item.id === postId);
            if (p) p.shares++;
            const url = window.location.origin + window.location.pathname + '#post-' + postId;
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(url).catch(() => {});
            }
            this.openShareMenuPostId = null;
            this.openPostOptionsId = null;
            this.showToast('📋 Đã sao chép liên kết bài viết vào bộ nhớ tạm!');
        },

        shareViaDevice(post) {
            const url = window.location.origin + window.location.pathname + '#post-' + post.id;
            if (navigator.share) {
                navigator.share({
                    title: 'PetShare360 - Bài viết từ ' + post.author,
                    text: (post.content || '').slice(0, 100) + '...',
                    url: url
                }).then(() => {
                    post.shares++;
                }).catch(() => {});
            } else {
                this.copyPostLink(post.id);
            }
            this.openShareMenuPostId = null;
        },

        toggleSavePost(postId) {
            const p = this.socialPosts.find(item => item.id === postId);
            if (p) {
                p.isSaved = !p.isSaved;
                this.openPostOptionsId = null;
                this.showToast(p.isSaved ? '🔖 Đã lưu bài viết vào bộ sưu tập!' : 'Đã bỏ lưu bài viết.');
            }
        },

        reportPost(postId) {
            this.openPostOptionsId = null;
            this.showToast('🚩 Đã ghi nhận báo cáo. Đội ngũ kiểm duyệt PetCare360 sẽ rà soát bài viết này!');
        },

        deleteSocialPost(postId) {
            this.openPostOptionsId = null;
            if (confirm('Bạn có chắc chắn muốn xóa bài viết này không?')) {
                this.socialPosts = this.socialPosts.filter(p => p.id !== postId);
                this.showToast('🗑️ Đã xóa bài viết khỏi PetShare360.');
            }
        },

        openLightbox(images, startIndex = 0) {
            if (!images || images.length === 0) return;
            this.lightboxImages = images;
            this.lightboxActiveIndex = startIndex || 0;
            this.showLightboxModal = true;
        },

        closeLightbox() {
            this.showLightboxModal = false;
        },

        lightboxNext() {
            if (!this.lightboxImages || this.lightboxImages.length === 0) return;
            this.lightboxActiveIndex = (this.lightboxActiveIndex + 1) % this.lightboxImages.length;
        },

        lightboxPrev() {
            if (!this.lightboxImages || this.lightboxImages.length === 0) return;
            this.lightboxActiveIndex = (this.lightboxActiveIndex - 1 + this.lightboxImages.length) % this.lightboxImages.length;
        },

        loadMorePosts() {
            if (this.isLoadingMorePosts) return;
            if (this.feedVisibleCount >= this.socialPosts.length) return;
            this.isLoadingMorePosts = true;
            setTimeout(() => {
                this.feedVisibleCount += 2;
                this.isLoadingMorePosts = false;
            }, 600);
        },

        handleFeedScroll() {
            if (this.activeCustomerTab !== 'petshare') return;
            const scrollY = window.scrollY || window.pageYOffset;
            const totalHeight = document.documentElement.scrollHeight;
            const windowHeight = window.innerHeight;
            if (scrollY + windowHeight >= totalHeight - 350) {
                this.loadMorePosts();
            }
        },

        toggleStreakCheckItem(task) {
            task.completed = !task.completed;
            if (task.completed) {
                this.showToast('🎉 Tuyệt vời! Bạn nhận được +' + task.points + ' PetPoints từ nhiệm vụ chăm sóc!');
            } else {
                this.showToast('Đã hủy hoàn thành nhiệm vụ.');
            }
        },

        redeemStreakReward(title, points) {
            if (confirm('Bạn có muốn dùng ' + points + ' PetPoints để đổi ưu đãi: "' + title + '" không?')) {
                this.showToast('🎁 Đổi quà thành công! Mã voucher đã được lưu vào Ví Voucher của bạn.');
            }
        },

        // 5. PETSHOW360 CAMERA HELPERS
        takeLiveSnapshot() {
            alert('📸 ĐÃ CHỤP KHOẢNH KHẮC BÉ! Ảnh chụp chất lượng 1080p đã được tự động lưu vào Thư viện kỷ niệm bé trên PetCare360.');
        },

        toggleLiveCameraAngle() {
            this.liveCameraAngle = (this.liveCameraAngle + 90) % 360;
            alert('🔄 Đã xoay góc camera 360° sang hướng ' + this.liveCameraAngle + '°');
        },

        sendStaffMessage(promptMsg) {
            const msg = prompt('Nhập lời nhắn gửi đến nhân viên chăm sóc bé:', promptMsg || '');
            if (msg) {
                alert('✅ Đã gửi tin nhắn đến KTV ca trực: "' + msg + '". Nhân viên sẽ phản hồi qua Zalo / ứng dụng trong 5 phút.');
            }
        },

        // 6. ORDERS DASHBOARD HELPERS
        get filteredCustomerOrdersList() {
            if (this.orderFilterStatus === 'all') return this.customerOrdersEnhanced;
            return this.customerOrdersEnhanced.filter(o => o.status === this.orderFilterStatus);
        },

        openOrderCheckoutSummary(ord) {
            this.selectedOrderForDetail = ord;
            this.showOrderSummaryModal = true;
        },

        reorderItems(ord) {
            if (ord.items && ord.items.length > 0) {
                ord.items.forEach(it => {
                    const rImg = it.image || it.img || this.getItemImage(it);
                    this.cart.push({
                        id: 'REORD-' + Date.now() + '-' + Math.random(),
                        name: it.name,
                        variant: it.variant || 'Tiêu chuẩn',
                        price: it.price,
                        qty: it.qty,
                        quantity: it.qty,
                        img: rImg,
                        image: rImg,
                        isService: false
                    });
                });
                this.activeCustomerTab = 'cart';
                this.cartStep = 2;
                alert('🎉 Đã thêm lại toàn bộ ' + ord.items.length + ' sản phẩm vào giỏ hàng và chuyển đến trang thanh toán!');
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        },

        openReviewModal(ord) {
            this.reviewOrderData = {
                orderId: ord.id,
                productName: ord.items[0] ? ord.items[0].name : 'Sản phẩm PetCare360',
                rating: 5,
                comment: '',
                photos: []
            };
            this.showReviewModal = true;
        },

        submitReview() {
            this.showReviewModal = false;
            alert('⭐ Cảm ơn bạn đã đánh giá ' + this.reviewOrderData.rating + ' sao cho đơn hàng ' + this.reviewOrderData.orderId + '! Bạn được cộng 50 điểm thưởng Loyalty.');
        },

        openRefundModal(ord) {
            this.refundOrderData = {
                orderId: ord.id,
                reason: 'Sản phẩm lỗi/hư hỏng khi vận chuyển',
                details: '',
                evidence: ''
            };
            this.showRefundModal = true;
        },

        submitRefund() {
            this.showRefundModal = false;
            alert('📩 Đã gửi yêu cầu Trả hàng / Hoàn tiền cho đơn ' + this.refundOrderData.orderId + '. Bộ phận CSKH sẽ liên hệ xác minh trong 2 giờ làm việc.');
        },

        openPODModal(ord) {
            this.currentPOD = {
                photo: ord.podPhoto || 'https://images.unsplash.com/photo-1549465220-1a8b9238cd48?auto=format&fit=crop&w=600&q=80',
                shipper: ord.shipper ? ord.shipper.name : 'Shipper PetShip360',
                phone: ord.shipper ? ord.shipper.phone : '0988 777 666',
                time: ord.date + ' 14:35'
            };
            this.showPODModal = true;
        },

        // 7. GIỎ HÀNG 5 BƯỚC & CHECKOUT LOGIC HELPERS
        goToCartStep(step) {
            this.cartStep = step;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        // Item classification
        isProductItem(item) {
            return !!(item && !item.isService);
        },

        isHotelItem(item) {
            if (!item || !item.isService) return false;
            if (item.serviceType === 'hotel' || item.serviceCategory === 'hotel') return true;
            if (item.payment_type === 'deposit_50' || item.bookingDetails?.payment_type === 'deposit_50') return true;
            const n = ((item.name || '') + ' ' + (item.serviceName || '')).toLowerCase();
            return n.includes('hotel') || n.includes('khách sạn') || n.includes('lưu trú') || n.includes('daycare');
        },

        isOtherServiceItem(item) {
            if (!item || !item.isService) return false;
            return !this.isHotelItem(item);
        },

        // State Analysis Getters (Requirement 1.1)
        get hasProduct() {
            return this.cart.some(it => this.isProductItem(it));
        },

        get hasHotel() {
            return this.cart.some(it => this.isHotelItem(it));
        },

        get hasOtherService() {
            return this.cart.some(it => this.isOtherServiceItem(it));
        },

        get hasService() {
            return this.hasHotel || this.hasOtherService;
        },

        get isMixedCart() {
            return this.hasProduct && this.hasService;
        },

        get serviceCartItems() {
            return this.cart.filter(it => it.isService);
        },

        get servicePetShipAddress() {
            const srv = this.cart.find(it => it.isService && (it.bookingDetails?.needPetShip || it.needPetShip));
            if (srv) {
                return srv.bookingDetails?.petShipAddress || srv.petShipAddress || this.checkoutShippingForm.address || 'Địa chỉ khách hàng yêu cầu';
            }
            return null;
        },

        // Checkout Math (Requirement 1.3 & 1.4)
        get totalProduct() {
            return this.cart
                .filter(it => this.isProductItem(it))
                .reduce((sum, it) => sum + ((Number(it.price) || 0) * (Number(it.qty || it.quantity) || 1)), 0);
        },

        get totalOtherService() {
            return this.cart
                .filter(it => this.isOtherServiceItem(it))
                .reduce((sum, it) => {
                    const cost = Number(it.totalCost || it.bookingDetails?.totalCost || it.price) || 0;
                    const qty = Number(it.qty || it.quantity) || 1;
                    return sum + (cost * qty);
                }, 0);
        },

        get totalHotel() {
            return this.cart
                .filter(it => this.isHotelItem(it))
                .reduce((sum, it) => {
                    let cost = Number(it.totalCost || it.bookingDetails?.totalCost) || 0;
                    if (!cost) {
                        cost = (it.payment_type === 'deposit_50' || it.bookingDetails?.payment_type === 'deposit_50') ? (Number(it.price) * 2) : Number(it.price);
                    }
                    const qty = Number(it.qty || it.quantity) || 1;
                    return sum + (cost * qty);
                }, 0);
        },

        get hotelDeposit() {
            return Math.round(this.totalHotel / 2);
        },

        get effectiveShippingFee() {
            // Biến shippingFee CHỈ được cộng vào nếu hasProduct = true VÀ user chọn "Giao tận nơi".
            // Tuyệt đối KHÔNG gộp phí PetShip vào biến shippingFee này.
            if (this.hasProduct && this.deliveryMethod === 'door') {
                return this.baseShippingFee || 35000;
            }
            return 0;
        },

        get shippingFee() {
            return this.effectiveShippingFee;
        },

        get cartSubtotal() {
            return this.totalProduct + this.totalOtherService + this.totalHotel;
        },

        // Voucher Stacking & Discounts (Requirement 3.3)
        get shippingDiscount() {
            if (!this.appliedVouchers.shipping || this.effectiveShippingFee === 0) return 0;
            const v = this.appliedVouchers.shipping;
            if (v.discountType === 'fixed') {
                return Math.min(this.effectiveShippingFee, Number(v.discountAmount) || 0);
            }
            return 0;
        },

        get orderDiscount() {
            if (!this.appliedVouchers.order) return 0;
            const v = this.appliedVouchers.order;
            const base = this.cartSubtotal;
            if (v.discountType === 'fixed') {
                return Math.min(base, Number(v.discountAmount) || 0);
            } else if (v.discountType === 'percent') {
                let val = Math.round(base * ((Number(v.discountPercent) || 0) / 100));
                if (v.maxDiscount) val = Math.min(val, Number(v.maxDiscount));
                return Math.min(base, val);
            }
            return 0;
        },

        get totalDiscount() {
            return this.shippingDiscount + this.orderDiscount;
        },

        get grandTotal() {
            const sum = this.totalProduct + this.totalOtherService + this.totalHotel + this.effectiveShippingFee;
            return Math.max(0, sum - this.totalDiscount);
        },

        get currentPayment() {
            // Số tiền thực tế phải trả ngay: totalProduct + totalOtherService + hotelDeposit + shippingFee - discounts
            const upfront = this.totalProduct + this.totalOtherService + this.hotelDeposit + this.effectiveShippingFee;
            return Math.max(0, upfront - this.totalDiscount);
        },

        get remainingBalance() {
            // Số tiền thu sau tại cơ sở: totalHotel - hotelDeposit
            return Math.max(0, this.totalHotel - this.hotelDeposit);
        },

        get finalCartTotal() {
            return this.currentPayment;
        },

        // Voucher Wallet Methods (Requirement 3.1 & 3.2)
        get hasAppliedVouchers() {
            return !!(this.appliedVouchers.shipping || this.appliedVouchers.order);
        },

        openVoucherWallet() {
            this.voucherWalletModalOpen = true;
            this.voucherSearchInput = '';
        },

        isVoucherEligible(v) {
            if (!v) return { eligible: false, reason: 'Voucher không tồn tại' };
            if (v.type === 'shipping') {
                if (!this.hasProduct) {
                    return { eligible: false, reason: 'Chỉ áp dụng cho đơn có Sản phẩm vật lý' };
                }
                if (this.deliveryMethod !== 'door') {
                    return { eligible: false, reason: 'Chỉ áp dụng khi chọn Giao hàng tận nơi' };
                }
                if (this.totalProduct < (v.minOrder || 0)) {
                    return { eligible: false, reason: 'Đơn sản phẩm chưa đạt tối thiểu ' + this.formatCurrency(v.minOrder) };
                }
                return { eligible: true };
            } else {
                if (v.requiresHotel && !this.hasHotel) {
                    return { eligible: false, reason: 'Chỉ áp dụng cho đơn có Pet Hotel 5 Sao' };
                }
                if (this.cartSubtotal < (v.minOrder || 0)) {
                    return { eligible: false, reason: 'Chưa đạt giá trị đơn tối thiểu ' + this.formatCurrency(v.minOrder) };
                }
                return { eligible: true };
            }
        },

        applyVoucher(v) {
            const check = this.isVoucherEligible(v);
            if (!check.eligible) {
                alert('Không thể áp dụng: ' + check.reason);
                return;
            }
            if (v.type === 'shipping') {
                this.appliedVouchers.shipping = v;
            } else {
                this.appliedVouchers.order = v;
            }
        },

        removeVoucher(type) {
            if (type === 'shipping') this.appliedVouchers.shipping = null;
            else if (type === 'order') this.appliedVouchers.order = null;
        },

        applyManualVoucherCode() {
            const code = (this.voucherSearchInput || '').trim().toUpperCase();
            if (!code) return;
            const v = this.availableVouchers.find(it => it.code.toUpperCase() === code);
            if (v) {
                const check = this.isVoucherEligible(v);
                if (!check.eligible) {
                    alert('Mã ' + code + ' chưa thỏa mãn điều kiện: ' + check.reason);
                } else {
                    this.applyVoucher(v);
                    alert('🎉 Áp dụng thành công voucher ' + code + '!');
                    this.voucherSearchInput = '';
                }
            } else {
                if (code === 'PET360' || code === 'GIAM50K') {
                    const customV = {
                        code: code,
                        type: 'order',
                        title: 'Mã giảm giá ' + code,
                        discountAmount: 50000,
                        discountType: 'fixed',
                        minOrder: 200000,
                        description: 'Giảm 50.000đ cho đơn từ 200k',
                        expiry: '31/12/2026'
                    };
                    this.appliedVouchers.order = customV;
                    alert('🎉 Áp dụng thành công mã giảm 50.000đ!');
                    this.voucherSearchInput = '';
                } else {
                    alert('Mã khuyến mãi "' + code + '" không tồn tại hoặc đã hết hạn.');
                }
            }
        },

        applyCoupon() {
            this.voucherSearchInput = this.couponCode;
            this.applyManualVoucherCode();
        },

        // Form Validation Methods (Requirement 2.1)
        onCityChange() {
            const prov = this.vnProvinces.find(p => p.name === this.checkoutShippingForm.city);
            if (prov && prov.districts && prov.districts.length > 0) {
                this.checkoutShippingForm.district = prov.districts[0].name;
                this.onDistrictChange();
            }
        },

        onDistrictChange() {
            const prov = this.vnProvinces.find(p => p.name === this.checkoutShippingForm.city);
            if (prov) {
                const dist = prov.districts.find(d => d.name === this.checkoutShippingForm.district);
                if (dist && dist.wards && dist.wards.length > 0) {
                    this.checkoutShippingForm.ward = dist.wards[0];
                }
            }
        },

        get currentProvinceDistricts() {
            const prov = this.vnProvinces.find(p => p.name === this.checkoutShippingForm.city);
            return prov ? prov.districts : [];
        },

        get currentDistrictWards() {
            const prov = this.vnProvinces.find(p => p.name === this.checkoutShippingForm.city);
            if (!prov) return [];
            const dist = prov.districts.find(d => d.name === this.checkoutShippingForm.district);
            return dist ? dist.wards : [];
        },

        get checkoutFormErrors() {
            const errors = {};
            const f = this.checkoutShippingForm;
            const t = f.touched || {};
            const vnPhoneRegex = /^(0[35789])[0-9]{8}$/;

            if (this.hasProduct) {
                if (t.name) {
                    if (!f.name || f.name.trim().length < 2) {
                        errors.name = 'Vui lòng nhập họ tên người nhận (tối thiểu 2 ký tự)';
                    }
                }
                if (t.phone) {
                    const cleanPhone = (f.phone || '').trim().replace(/\s/g, '');
                    if (!cleanPhone) {
                        errors.phone = 'Vui lòng nhập số điện thoại người nhận';
                    } else if (!vnPhoneRegex.test(cleanPhone)) {
                        errors.phone = 'Số điện thoại không đúng định dạng VN (10 số, bắt đầu 03, 05, 07, 08, 09)';
                    }
                }
                if (this.deliveryMethod === 'door') {
                    if (t.address && (!f.address || f.address.trim().length < 5)) {
                        errors.address = 'Vui lòng nhập số nhà, tên đường chi tiết (tối thiểu 5 ký tự)';
                    }
                    if (t.city && (!f.city || !f.city.trim())) {
                        errors.city = 'Vui lòng chọn Tỉnh/Thành phố';
                    }
                    if (t.district && (!f.district || !f.district.trim())) {
                        errors.district = 'Vui lòng chọn Quận/Huyện';
                    }
                    if (t.ward && (!f.ward || !f.ward.trim())) {
                        errors.ward = 'Vui lòng chọn Phường/Xã';
                    }
                }
            }
            return errors;
        },

        get isModalCheckoutValid() {
            const f = this.checkoutForm;
            if (!f) return false;
            const cleanPhone = (f.phone || '').trim().replace(/\s/g, '');
            const vnPhoneRegex = /^(0[35789])[0-9]{8}$/;
            if (!f.name || f.name.trim().length < 2) return false;
            if (!cleanPhone || !vnPhoneRegex.test(cleanPhone)) return false;
            if (this.hasProduct) {
                if (!f.address || f.address.trim().length < 5) return false;
            }
            return true;
        },

        get isCheckoutShippingFormValid() {
            if (!this.hasProduct) return true;
            const f = this.checkoutShippingForm;
            const cleanPhone = (f.phone || '').trim().replace(/\s/g, '');
            const vnPhoneRegex = /^(0[35789])[0-9]{8}$/;
            if (!f.name || f.name.trim().length < 2) return false;
            if (!cleanPhone || !vnPhoneRegex.test(cleanPhone)) return false;
            if (this.deliveryMethod === 'door') {
                if (!f.address || f.address.trim().length < 5) return false;
                if (!f.city || !f.city.trim()) return false;
                if (!f.district || !f.district.trim()) return false;
                if (!f.ward || !f.ward.trim()) return false;
            }
            return true;
        },

        touchAllCheckoutFields() {
            this.checkoutShippingForm.touched = {
                name: true,
                phone: true,
                address: true,
                city: true,
                district: true,
                ward: true
            };
        },

        proceedToPaymentStep() {
            if (this.hasProduct) {
                this.touchAllCheckoutFields();
            }
            if (this.hasService) {
                this.checkoutBookingContactTouched.name = true;
                this.checkoutBookingContactTouched.phone = true;
                if (this.hasPetShip) {
                    this.checkoutBookingContactTouched.street = true;
                    this.checkoutBookingContactTouched.district = true;
                    this.checkoutBookingContactTouched.ward = true;
                }
            }
            if (!this.isStep2CheckoutValid) {
                alert('⚠️ Vui lòng hoàn tất đầy đủ thông tin nhận hàng / lịch hẹn hợp lệ trước khi tiếp tục!');
                return;
            }
            this.goToCartStep(3);
        },

        // VietQR Dynamic Generator (Requirement 2.2)
        get vietQrUrl() {
            const bankId = 'MB';
            const accountNo = '888899996666';
            const template = 'compact2';
            const amount = (this.currentPendingOrder ? this.currentPendingOrder.amount_paid : this.currentPayment) || 0;
            const orderCode = (this.currentPendingOrder ? this.currentPendingOrder.orderCode : this.completedOrderNumber) || '#DH157817';
            const cleanCode = orderCode.replace('#', '');
            const memo = encodeURIComponent('PETCARE360 ' + cleanCode);
            const accountName = encodeURIComponent('CT CP PETCARE360 VIETNAM');
            return `https://img.vietqr.io/image/${bankId}-${accountNo}-${template}.png?amount=${amount}&addInfo=${memo}&accountName=${accountName}`;
        },

        get formattedCountdown() {
            const m = Math.floor(this.orderCountdownSeconds / 60);
            const s = this.orderCountdownSeconds % 60;
            return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
        },

        startOrderCountdown() {
            if (this.orderCountdownTimer) clearInterval(this.orderCountdownTimer);
            this.orderCountdownSeconds = 900; // 15 phút
            this.orderCountdownTimer = setInterval(() => {
                if (this.orderCountdownSeconds > 0) {
                    this.orderCountdownSeconds--;
                } else {
                    clearInterval(this.orderCountdownTimer);
                    this.handleOrderTimeout();
                }
            }, 1000);
        },

        handleOrderTimeout() {
            if (this.currentPendingOrder && this.currentPendingOrder.status === 'PENDING_PAYMENT') {
                this.currentPendingOrder.status = 'CANCELLED';
                this.currentPendingOrder.statusText = 'Đã hủy (Hết thời gian giữ chỗ 15p)';
                this.currentPendingOrder.badgeColor = 'bg-rose-100 text-rose-800 border-rose-200';
                this.releaseStock(this.currentPendingOrder);
                alert('⚠️ Đơn hàng ' + this.currentPendingOrder.orderCode + ' đã hết 15 phút giữ chỗ và tự động bị hủy. Toàn bộ tồn kho đã được hoàn trả.');
            }
        },

        holdStockForCart() {
            this.cart.forEach(item => {
                if (this.isProductItem(item)) {
                    const prod = this.products.find(p => p.id === item.id);
                    if (prod) {
                        const qty = Number(item.qty || item.quantity) || 1;
                        if (typeof prod.stock === 'number') {
                            prod.stock = Math.max(0, prod.stock - qty);
                        }
                        if (typeof prod.stockQ1 === 'number') {
                            prod.stockQ1 = Math.max(0, prod.stockQ1 - qty);
                        }
                        prod.reservedStock = (prod.reservedStock || 0) + qty;
                    }
                }
            });
            this.orderStockHeld = true;
        },

        releaseStock(order) {
            if (!order || !order.items) return;
            order.items.forEach(item => {
                if (this.isProductItem(item)) {
                    const prod = this.products.find(p => p.id === item.id);
                    if (prod) {
                        const qty = Number(item.qty || item.quantity) || 1;
                        if (typeof prod.stock === 'number') {
                            prod.stock += qty;
                        }
                        if (typeof prod.stockQ1 === 'number') {
                            prod.stockQ1 += qty;
                        }
                        if (prod.reservedStock) {
                            prod.reservedStock = Math.max(0, prod.reservedStock - qty);
                        }
                    }
                }
            });
            this.orderStockHeld = false;
        },

        deductStockPermanently(order) {
            if (!order || !order.items) return;
            order.items.forEach(item => {
                if (this.isProductItem(item)) {
                    const prod = this.products.find(p => p.id === item.id);
                    if (prod && prod.reservedStock) {
                        const qty = Number(item.qty || item.quantity) || 1;
                        prod.reservedStock = Math.max(0, prod.reservedStock - qty);
                    }
                }
            });
            this.orderStockHeld = false;
        },

        // Finalize Order (Requirement 1.6 & 2.3)
        finalizeOrder() {
            this.completedOrderNumber = '#' + Math.floor(100000 + Math.random() * 900000);
            this.completedOrderDate = new Date().toLocaleDateString('vi-VN');

            // Hold Stock for 15 mins
            this.holdStockForCart();

            let paymentType = 'product_only';
            if (this.hasProduct && this.hasService) {
                paymentType = 'mixed_cart';
            } else if (this.hasHotel) {
                paymentType = 'hotel_deposit';
            } else if (this.hasOtherService) {
                paymentType = 'service_full';
            }

            const newOrder = {
                id: 'ORD-' + Math.floor(1000 + Math.random() * 9000),
                orderCode: this.completedOrderNumber,
                date: this.completedOrderDate,
                status: 'PENDING_PAYMENT',
                statusText: 'Chờ thanh toán (Giữ chỗ 15p)',
                badgeColor: 'bg-amber-100 text-amber-800 border-amber-200',
                payment_type: paymentType,
                has_mixed_cart: this.hasProduct && this.hasService,
                amount_paid: this.currentPayment,
                balance_due: this.remainingBalance,
                total: this.grandTotal,
                grandTotal: this.grandTotal,
                currentPayment: this.currentPayment,
                remainingBalance: this.remainingBalance,
                subtotal: this.cartSubtotal,
                totalProduct: this.totalProduct,
                totalOtherService: this.totalOtherService,
                totalHotel: this.totalHotel,
                hotelDeposit: this.hotelDeposit,
                shippingFee: this.effectiveShippingFee,
                shippingDiscount: this.shippingDiscount,
                orderDiscount: this.orderDiscount,
                totalDiscount: this.totalDiscount,
                appliedVouchers: { ...this.appliedVouchers },
                paymentMethod: this.paymentMethod,
                paymentMethodLabel: this.paymentMethod === 'vietqr' ? 'Chuyển khoản VietQR MB Bank' : (this.paymentMethod === 'atm' ? 'Thẻ ATM / Internet Banking' : (this.paymentMethod === 'visa' ? 'Thẻ Quốc tế Visa/Mastercard' : (this.paymentMethod === 'ewallet' ? 'Ví điện tử' : 'Thanh toán COD'))),
                paymentStatus: 'unpaid',
                recipient: { ...this.checkoutShippingForm },
                items: this.cart.map(i => ({ ...i, img: i.img || i.image || this.getItemImage(i), image: i.image || i.img || this.getItemImage(i) })),
                holdStockExpiresAt: Date.now() + 15 * 60 * 1000,
                receiptUrl: null
            };

            this.currentPendingOrder = newOrder;
            this.customerOrdersEnhanced.unshift(newOrder);
            this.orders.unshift(newOrder);

            this.startOrderCountdown();
            this.webhookSuccessReceived = false;
            this.uploadedReceiptUrl = null;

            this.cart = [];
            this.cartStep = 4;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        // Webhook Simulator (Requirement 2.3)
        simulatePaymentWebhook() {
            if (!this.currentPendingOrder) return;
            if (this.orderCountdownTimer) clearInterval(this.orderCountdownTimer);

            const isDeposit = (this.currentPendingOrder.payment_type === 'hotel_deposit' || (this.currentPendingOrder.has_mixed_cart && this.currentPendingOrder.balance_due > 0));
            const finalStatus = isDeposit ? 'DEPOSIT_PAID' : 'PAID';
            const finalStatusText = isDeposit ? ('Đã cọc 50% (Còn thu: ' + this.formatCurrency(this.currentPendingOrder.balance_due) + ')') : 'Đã thanh toán 100%';

            this.currentPendingOrder.status = finalStatus;
            this.currentPendingOrder.statusText = finalStatusText;
            this.currentPendingOrder.badgeColor = 'bg-emerald-100 text-emerald-800 border-emerald-200';
            this.currentPendingOrder.paymentStatus = 'paid';

            this.deductStockPermanently(this.currentPendingOrder);
            this.webhookSuccessReceived = true;

            alert(`⚡ [WEBHOOK PAYMENT.SUCCESS]\nĐã nhận thông báo thanh toán ' + this.formatCurrency(this.currentPendingOrder.amount_paid) + ' cho đơn ' + this.currentPendingOrder.orderCode + '!
Trạng thái đơn: ' + finalStatus + ' | Đã trừ kho vĩnh viễn.`);
        },

        handleReceiptUpload(event) {
            const file = event.target.files && event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.uploadedReceiptUrl = e.target.result;
                    if (this.currentPendingOrder) {
                        this.currentPendingOrder.receiptUrl = this.uploadedReceiptUrl;
                    }
                    alert('📷 Đã tải lên biên lai chuyển khoản thành công! Bạn có thể nhấn "Duyệt đơn thủ công" để hoàn tất.');
                };
                reader.readAsDataURL(file);
            }
        },

        adminManualApprove() {
            if (!this.currentPendingOrder) return;
            this.simulatePaymentWebhook();
        },
        // 8. TÀI KHOẢN SAAS HELPERS
        saveAccountProfile() {
            alert('🎉 Đã lưu thông tin tài khoản cá nhân thành công!');
        },

        changePassword() {
            if (this.changePasswordForm.newPass !== this.changePasswordForm.confirm) {
                alert('Mật khẩu xác nhận không khớp!');
                return;
            }
            this.showChangePasswordModal = false;
            this.changePasswordForm = { current: '', newPass: '', confirm: '' };
            alert('🔒 Đã đổi mật khẩu tài khoản thành công!');
        },

        openAddAddressModal() {
            this.editingAddress = null;
            this.addressForm = { id: Date.now(), label: 'Địa chỉ mới', receiver: this.customerProfile.name, phone: this.customerProfile.phone, fullAddress: '', isDefault: false };
            this.showAddressModal = true;
        },

        openEditAddressModal(addr) {
            this.editingAddress = addr;
            this.addressForm = { ...addr };
            this.showAddressModal = true;
        },

        saveAddressForm() {
            if (!this.addressForm.fullAddress.trim()) {
                alert('Vui lòng nhập địa chỉ chi tiết!');
                return;
            }
            if (this.editingAddress) {
                const idx = this.addresses.findIndex(a => a.id === this.editingAddress.id);
                if (idx > -1) this.addresses[idx] = { ...this.addressForm };
            } else {
                this.addresses.push({ ...this.addressForm, id: Date.now() });
            }
            this.showAddressModal = false;
            alert('Đã cập nhật sổ địa chỉ thành công!');
        },

        deleteAddress(id) {
            if (confirm('Bạn có chắc muốn xóa địa chỉ này không?')) {
                this.addresses = this.addresses.filter(a => a.id !== id);
                alert('Đã xóa địa chỉ thành công!');
            }
        },

        setDefaultAddress(id) {
            this.addresses.forEach(a => a.isDefault = (a.id === id));
            alert('Đã đặt làm địa chỉ giao hàng mặc định!');
        },

        scrollToUrgentTasks() {
            const el = document.getElementById('urgent-tasks-section');
            if (el) el.scrollIntoView({ behavior: 'smooth' });
        }
    };
}
</script>
'''
