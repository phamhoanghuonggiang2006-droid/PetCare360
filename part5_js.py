JS_HTML = '''<!-- ==================== LOGIC XỬ LÝ DỮ LIỆU & ALPINE.JS STORE TOÀN DIỆN ==================== -->
<script>
function superPetCareApp() {
    return {
        // Trạng thái xác thực & Điều hướng
        isLoggedIn: false, // Mặc định khi vào là Khách chưa đăng nhập
        currentRole: 'customer', // Mặc định hiển thị giao diện khách hàng
        activeCustomerTab: 'home', // 'home' | 'petshare' | 'products' | 'services' | 'faq' | 'legal' | 'profile'
        get currentTab() { return this.activeCustomerTab; },
        set currentTab(val) { this.activeCustomerTab = val; },

        activeAdminTab: 'dashboard', // 'dashboard' | 'appointments' | 'orders' | 'products' | 'pets' | 'analytics'
        get adminTab() { return this.activeAdminTab; },
        set adminTab(val) { this.activeAdminTab = val; },

        adminTimeFilter: 'all', // 'all' | 'today' | '7days' | 'month' | 'quarter'
        globalBranch: 'all', // 'all' | 'HN' | 'Q7' | 'BT'
        currentOrderTypeTab: 'all',
        showLowStockOnly: false,
        sidebarOpen: false,

        // Bộ lọc & Tìm kiếm
        searchQuery: '',
        filterCategory: 'all',
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
        selectedArticleModal: null,
        selectedPetHealthModal: null,
        selectedOrder: null,

        // Login form
        loginUsername: '',
        loginPassword: '',
        loginError: '',

        // Hồ sơ người dùng
        customerProfile: {
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

        // 3 Thú cưng chi tiết kèm sổ sức khỏe
        pets: [
            {
                id: 1,
                name: 'Bơ (Butter)',
                type: 'Chó',
                breed: 'Corgi Pembroke Welsh',
                gender: 'Đực',
                age: '2 tuổi',
                weight: '11.5 kg',
                chipId: '900118000452311',
                chip: '900118000452311',
                avatar: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80',
                image: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80',
                allergies: 'Không ghi nhận dị ứng thuốc, nhạy cảm với thức ăn chứa nhiều mỡ động vật.',
                vaccines: [
                    { name: 'Vắc-xin 7 bệnh chó (Nobivac DHPPi + L4)', date: '15/01/2026', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '15/01/2027', status: 'Đã hoàn thành' },
                    { name: 'Phòng ngừa dại (Rabisin)', date: '15/01/2026', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '15/01/2027', status: 'Đã hoàn thành' },
                    { name: 'Xổ giun định kỳ & Nhỏ gáy Advocate', date: '01/03/2026', doctor: 'BS Đỗ Hoàng Nam', nextDate: '01/06/2026', status: 'Sắp tới hạn' }
                ],
                medicalHistory: [
                    { date: '10/02/2026', diagnosis: 'Viêm da kẽ ngón chân do ẩm ướt', treatment: 'Vệ sinh dung dịch Chlorhexidine 2%, bôi kem kháng viêm 5 ngày', notes: 'Giữ chân khô ráo sau khi đi dạo' },
                    { date: '05/11/2025', diagnosis: 'Khám sức khỏe tổng quát & Siêu âm ổ bụng', treatment: 'Chỉ số gan thận bình thường, thể trạng khỏe mạnh', notes: 'Bổ sung thêm glucosamine hỗ trợ cột sống ngắn' }
                ]
            },
            {
                id: 2,
                name: 'Mochi',
                type: 'Mèo',
                breed: 'Anh Lông Ngắn (Silver Shaded)',
                gender: 'Cái',
                age: '1.5 tuổi',
                weight: '4.2 kg',
                chipId: '900118000789123',
                chip: '900118000789123',
                avatar: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=400&q=80',
                image: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=400&q=80',
                allergies: 'Dị ứng phấn hoa nhẹ, nhạy cảm với thuốc gây mê nhóm ketamine (đã ghi nhận trong hồ sơ mổ).',
                vaccines: [
                    { name: 'Vắc-xin 4 bệnh mèo (Purevax RCPCh)', date: '20/12/2025', doctor: 'BS Trần Thu Hà', nextDate: '20/12/2026', status: 'Đã hoàn thành' },
                    { name: 'Vắc-xin phòng dại (Rabisin)', date: '20/12/2025', doctor: 'BS Trần Thu Hà', nextDate: '20/12/2026', status: 'Đã hoàn thành' }
                ],
                medicalHistory: [
                    { date: '12/10/2025', diagnosis: 'Phẫu thuật triệt sản nội soi vi phẫu', treatment: 'Hồi phục hoàn toàn sau 48h, vết mổ liền đẹp không sẹo', notes: 'Đã cắt chỉ, chế độ dinh dưỡng hạt Sterilised' }
                ]
            },
            {
                id: 3,
                name: 'Đậu Đậu',
                type: 'Chó',
                breed: 'Poodle Tiny màu Nâu Đỏ',
                gender: 'Đực',
                age: '3 tuổi',
                weight: '3.6 kg',
                chipId: '900118000994120',
                chip: '900118000994120',
                avatar: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=400&q=80',
                image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=400&q=80',
                allergies: 'Tiền sử dị ứng thức ăn chứa đạm bò (bị đỏ tai và gãi ngứa).',
                vaccines: [
                    { name: 'Vắc-xin 7 bệnh chó (Nobivac DHPPi)', date: '05/08/2025', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '05/08/2026', status: 'Đã hoàn thành' },
                    { name: 'Phòng dại Rabisin', date: '05/08/2025', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '05/08/2026', status: 'Đã hoàn thành' }
                ],
                medicalHistory: [
                    { date: '14/01/2026', diagnosis: 'Lấy cao răng siêu âm & đánh bóng răng', treatment: 'Vệ sinh mảng bám vôi răng độ 2, xịt keo ong khử khuẩn', notes: 'Duy trì gặm thanh sạch răng hàng ngày' }
                ]
            }
        ],
        get allPets() { return this.pets; },
        set allPets(val) { this.pets = val; },
        get myPets() { return this.pets; },
        set myPets(val) { this.pets = val; },

        // 12 Sản phẩm chi tiết
        products: [
            {
                id: 1,
                sku: 'PET-FD01',
                name: 'Thức Ăn Hạt Royal Canin Mini Adult (Chó Nhỏ)',
                brand: 'Royal Canin (Pháp)',
                price: 360000,
                rating: 4.9,
                reviews: 184,
                reviewsCount: 184,
                sold: 1420,
                stock: 95,
                stockHN: 40,
                stockQ7: 35,
                stockBT: 20,
                category: 'Thức ăn khô',
                categoryAdmin: 'Thức ăn khô',
                img: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
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
                brand: 'Royal Canin (Pháp)',
                price: 395000,
                rating: 5.0,
                reviews: 216,
                reviewsCount: 216,
                sold: 1890,
                stock: 120,
                stockHN: 50,
                stockQ7: 45,
                stockBT: 25,
                category: 'Thức ăn khô',
                categoryAdmin: 'Thức ăn khô',
                img: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
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
                brand: 'Orijen (Canada)',
                price: 890000,
                rating: 4.9,
                reviews: 92,
                reviewsCount: 92,
                sold: 530,
                stock: 45,
                stockHN: 20,
                stockQ7: 15,
                stockBT: 10,
                category: 'Thức ăn khô',
                categoryAdmin: 'Thức ăn khô',
                img: 'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?auto=format&fit=crop&w=500&q=80',
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
                brand: 'Monge (Italy)',
                price: 420000,
                rating: 4.8,
                reviews: 135,
                reviewsCount: 135,
                sold: 1120,
                stock: 80,
                stockHN: 35,
                stockQ7: 30,
                stockBT: 15,
                category: 'Pate & Treats',
                categoryAdmin: 'Pate & Treats',
                img: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=500&q=80',
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
                brand: 'Inaba Ciao (Nhật Bản)',
                price: 215000,
                rating: 5.0,
                reviews: 410,
                reviewsCount: 410,
                sold: 3400,
                stock: 250,
                stockHN: 100,
                stockQ7: 90,
                stockBT: 60,
                category: 'Pate & Treats',
                categoryAdmin: 'Pate & Treats',
                img: 'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=500&q=80',
                desc: 'Treat dạng kem số 1 tại Nhật Bản, vị thơm ngon cuốn hút mọi chú mèo. Cung cấp nước dồi dào ngừa sỏi thận và chiết xuất trà xanh giảm mùi hôi chất thải.',
                description: 'Treat dạng kem số 1 tại Nhật Bản, vị thơm ngon cuốn hút.',
                ingredients: 'Thịt cá ngừ tươi Maguro, chiết xuất sò điệp, collagen biển, chiết xuất trà xanh.',
                usage: 'Cho ăn như món tráng miệng hoặc phần thưởng khi huấn luyện, 2-4 thanh mỗi ngày.'
            },
            {
                id: 6,
                sku: 'PET-MD01',
                name: 'Thuốc Trị Ve Rận & Tẩy Giun NexGard Spectra (Dạng Viên Nhai Thịt Bò)',
                brand: 'Boehringer Ingelheim (Pháp)',
                price: 460000,
                rating: 5.0,
                reviews: 320,
                reviewsCount: 320,
                sold: 2100,
                stock: 75,
                stockHN: 30,
                stockQ7: 25,
                stockBT: 20,
                category: 'Thuốc & Y tế',
                categoryAdmin: 'Thuốc & Y tế',
                img: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=500&q=80',
                desc: 'Viên nhai vị thịt bò thơm ngon bảo vệ toàn diện 1 tháng: tiêu diệt bọ chét, ve chó, ghẻ Demodex, phòng giun tim và tẩy sạch các loại giun đường ruột.',
                description: 'Viên nhai vị thịt bò thơm ngon bảo vệ toàn diện 1 tháng.',
                ingredients: 'Afoxolaner và Milbemycin Oxime tinh khiết chuẩn dược phẩm thú y quốc tế.',
                usage: 'Cho chó nhai trực tiếp như bánh thưởng. Dùng định kỳ 1 viên/tháng cho cún từ 8 tuần tuổi.'
            },
            {
                id: 7,
                sku: 'PET-MD02',
                name: 'Tuýp Nhỏ Gáy Phòng Trị Ký Sinh Trùng Toàn Diện Cho Mèo Revolution Plus',
                brand: 'Zoetis (Mỹ)',
                price: 385000,
                rating: 4.9,
                reviews: 198,
                reviewsCount: 198,
                sold: 1650,
                stock: 88,
                stockHN: 40,
                stockQ7: 30,
                stockBT: 18,
                category: 'Thuốc & Y tế',
                categoryAdmin: 'Thuốc & Y tế',
                img: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=500&q=80',
                desc: 'Dược chất thế hệ mới tiêu diệt 6 loại ký sinh trùng gây hại trên mèo: bọ chét, ấu trùng bọ chét, ve, rận tai, giun tim, giun đũa và giun móc chỉ với 1 giọt nhỏ gáy.',
                description: 'Dược chất thế hệ mới tiêu diệt 6 loại ký sinh trùng trên mèo.',
                ingredients: 'Selamectin và Sarolaner nồng độ cao an toàn cho mèo từ 8 tuần tuổi.',
                usage: 'Vạch lông sau gáy mèo và bóp hết tuýp thuốc trực tiếp lên da.'
            },
            {
                id: 8,
                sku: 'PET-VS01',
                name: 'Cát Đậu Nành Tofu Cature Kháng Khuẩn Tự Nhiên (Hương Trà Xanh 6L)',
                brand: 'Cature (Mỹ)',
                price: 165000,
                rating: 4.8,
                reviews: 280,
                reviewsCount: 280,
                sold: 2890,
                stock: 190,
                stockHN: 80,
                stockQ7: 70,
                stockBT: 40,
                category: 'Vệ sinh & Khử mùi',
                categoryAdmin: 'Vệ sinh & Khử mùi',
                img: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=500&q=80',
                desc: '100% bã đậu nành tự nhiên vón cục siêu tốc trong 3 giây, kiểm soát mùi hôi vượt trội, tan hoàn toàn trong nước xả bồn cầu cực kỳ tiện lợi và thân thiện môi trường.',
                description: '100% bã đậu nành tự nhiên vón cục siêu tốc trong 3 giây.',
                ingredients: 'Sợi đậu nành hữu cơ, tinh bột ngô tự nhiên, chiết xuất lá trà xanh diệt khuẩn.',
                usage: 'Đổ cát vào khay vệ sinh độ dày khoảng 5-7cm. Dọn các cục vón hàng ngày.'
            },
            {
                id: 9,
                sku: 'PET-VS02',
                name: 'Sữa Tắm Trị Nấm & Khử Mùi Hôi Cho Thú Cưng Davis Chlorhexidine 4%',
                brand: 'Davis (Mỹ)',
                price: 340000,
                rating: 4.9,
                reviews: 145,
                reviewsCount: 145,
                sold: 980,
                stock: 60,
                stockHN: 25,
                stockQ7: 20,
                stockBT: 15,
                category: 'Vệ sinh & Khử mùi',
                categoryAdmin: 'Vệ sinh & Khử mùi',
                img: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=500&q=80',
                desc: 'Sữa tắm dược liệu đặc trị viêm da, nấm da, vi khuẩn và mùi hôi khó chịu trên chó mèo. Chứa hoạt chất Chlorhexidine Gluconate 4% được các bác sĩ da liễu thú y khuyên dùng.',
                description: 'Sữa tắm dược liệu đặc trị viêm da, nấm da, vi khuẩn.',
                ingredients: 'Chlorhexidine Gluconate 4.0%, chất tạo bọt dịu nhẹ từ dừa, tinh dầu dưỡng ẩm da.',
                usage: 'Làm ướt lông, thoa dầu tắm tạo bọt và xoa bóp đều trong 5-10 phút rồi xả sạch với nước.'
            },
            {
                id: 10,
                sku: 'PET-PK01',
                name: 'Balo Phi Thuyền Vận Chuyển Thú Cưng Thông Khí Đa Chiều VIP',
                brand: 'PetCare Pro',
                price: 490000,
                rating: 4.7,
                reviews: 86,
                reviewsCount: 86,
                sold: 620,
                stock: 35,
                stockHN: 15,
                stockQ7: 12,
                stockBT: 8,
                category: 'Phụ kiện & Đồ chơi',
                categoryAdmin: 'Phụ kiện & Đồ chơi',
                img: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=500&q=80',
                desc: 'Balo vận chuyển thú cưng cao cấp chất liệu nhựa ABS cứng cáp chống va đập, nắp trong suốt tầm nhìn rộng, hệ thống 9 lỗ thoáng khí và đệm lót êm ái cho bé dưới 8kg.',
                description: 'Balo vận chuyển thú cưng cao cấp chất liệu nhựa ABS cứng cáp.',
                ingredients: 'Nhựa ABS an toàn thực phẩm, vải Oxford 900D chống thấm, lưới thép không gỉ.',
                usage: 'Phù hợp khi chở bé đi tiêm phòng, du lịch hoặc dạo phố an toàn tuyệt đối.'
            },
            {
                id: 11,
                sku: 'PET-PK02',
                name: 'Trụ Cào Móng Cây Cat Tree 3 Tầng Kèm Nhà Cầu Ngủ Mèo',
                brand: 'CozyPet',
                price: 680000,
                rating: 4.9,
                reviews: 64,
                reviewsCount: 64,
                sold: 410,
                stock: 28,
                stockHN: 12,
                stockQ7: 10,
                stockBT: 6,
                category: 'Phụ kiện & Đồ chơi',
                categoryAdmin: 'Phụ kiện & Đồ chơi',
                img: 'https://images.unsplash.com/photo-1545249390-6bdfa286032f?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1545249390-6bdfa286032f?auto=format&fit=crop&w=500&q=80',
                desc: 'Cây cào móng cao cấp quấn dây đay sisal tự nhiên bền chắc, khung gỗ ép công nghiệp chịu lực, bọc vải nhung mềm mịn giúp mèo xả stress và bảo vệ sofa nội thất gia đình.',
                description: 'Cây cào móng cao cấp quấn dây đay sisal tự nhiên bền chắc.',
                ingredients: 'Gỗ chịu lực MDF, dây thừng Sisal tự nhiên, vải nỉ lông cừu nhân tạo.',
                usage: 'Đặt tại góc phòng khách nơi mèo thường xuyên qua lại hoặc gần cửa sổ đón nắng.'
            },
            {
                id: 12,
                sku: 'PET-MD03',
                name: 'Gel Dinh Dưỡng Bổ Sung Năng Lượng & Vitamin Nutri-plus Gel',
                brand: 'Virbac (Pháp)',
                price: 295000,
                rating: 5.0,
                reviews: 260,
                reviewsCount: 260,
                sold: 2150,
                stock: 92,
                stockHN: 40,
                stockQ7: 32,
                stockBT: 20,
                category: 'Thuốc & Y tế',
                categoryAdmin: 'Thuốc & Y tế',
                img: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                desc: 'Thực phẩm bổ sung năng lượng cao cấp chứa đầy đủ vitamin nhóm B, A, D, E và các khoáng chất thiết yếu cho thú cưng đang dưỡng bệnh, sau phẫu thuật hoặc mẹ mang thai/cho con bú.',
                description: 'Thực phẩm bổ sung năng lượng cao cấp chứa đầy đủ vitamin.',
                ingredients: 'Vitamin A, D3, E, B1, B2, B6, B12, Nicotinamide, Canxi Pantothenate, Axit Folic, Sắt, Mangan, Magiê.',
                usage: 'Cho ăn trực tiếp hoặc trộn vào thức ăn. Liều lượng: 1-2 muỗng cà phê/5kg thể trọng.'
            }
        ],

        // 12 Dịch vụ chuẩn y khoa & làm đẹp
        services: [
            {
                id: 1,
                name: 'Gói Spa & Grooming Cắt Tỉa Lông Tạo Kiểu Toàn Diện',
                price: 350000,
                duration: '120 - 150 phút',
                expert: 'Master Groomer & Kỹ thuật viên cao cấp',
                doctor: 'Master Groomer & KTV cao cấp',
                category: 'Spa & Làm đẹp',
                img: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80',
                desc: 'Gói chăm sóc sắc đẹp đẳng cấp nhất cho bé cưng: tắm sục ozone thải độc da, sấy chải bông phồng, cắt móng mài góc tròn, vệ sinh nhổ lông tai và cắt tỉa lông tạo kiểu theo chuẩn dáng giống loài.',
                description: 'Gói chăm sóc sắc đẹp đẳng cấp nhất cho bé cưng.',
                steps: [
                    { title: 'Kiểm tra da lông & tư vấn form dáng', desc: 'Kiểm tra tình trạng búi lông, ve rận, nấm và tư vấn dáng cắt tỉa phù hợp.' },
                    { title: 'Vệ sinh sơ bộ chuyên sâu', desc: 'Cắt mài móng không chảy máu, nhổ sạch lông tai, cạo lông đệm chân và vệ sinh hậu môn.' },
                    { title: 'Tắm bồn sục Ozone thư giãn 2 lần', desc: 'Dùng dầu gội hữu cơ nhập khẩu khử mùi, massage giải tỏa căng thẳng và ủ xả phục hồi lông.' },
                    { title: 'Sấy ion âm & chải tơi lông chuyên nghiệp', desc: 'Sấy gió ấm bảo vệ da, chải gỡ rối hoàn toàn và đánh bông lớp lông lót.' },
                    { title: 'Cắt tỉa tạo kiểu nghệ thuật & xịt tinh dầu', desc: 'Master Groomer tỉa thủ công từng góc cạnh sắc sảo và xịt tinh dầu dưỡng lông.' }
                ]
            },
            {
                id: 2,
                name: 'Khám Sức Khỏe Tổng Quát & Tầm Soát Bệnh Lý Thú Cưng',
                price: 250000,
                duration: '45 - 60 phút',
                expert: 'ThS. Bác sĩ Thú y chuyên khoa Nội',
                doctor: 'ThS. BS Nguyễn Minh Quân',
                category: 'Khám & Điều trị',
                img: 'https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def?auto=format&fit=crop&w=600&q=80',
                desc: 'Quy trình kiểm tra toàn diện 12 cơ quan trọng yếu: tim phổi, răng miệng, mắt tai, ổ bụng, xương khớp, huyết áp và kiểm tra ký sinh trùng da lông.',
                description: 'Quy trình kiểm tra toàn diện 12 cơ quan trọng yếu.',
                steps: [
                    { title: 'Thu thập tiền sử bệnh & cân đo chỉ số sinh tồn', desc: 'Đo thân nhiệt, huyết áp, cân nặng, nhịp tim và nghe phổi bằng ống nghe chuyên dụng.' },
                    { title: 'Khám lâm sàng chi tiết mắt - tai - miệng', desc: 'Nội soi ống tai, kiểm tra giác mạc và đánh giá mức độ vôi răng hay viêm nướu.' },
                    { title: 'Sờ nắn ổ bụng & kiểm tra hệ vận động khớp', desc: 'Đánh giá gan lách thận bàng quang và phản xạ các khớp xương chi.' },
                    { title: 'Soi tươi da lông kiểm tra nấm & ghẻ Demodex', desc: 'Lấy mẫu biểu bì kiểm tra dưới kính hiển vi quang học độ phóng đại lớn.' },
                    { title: 'Tư vấn phác đồ phòng bệnh & cấp sổ theo dõi', desc: 'Bác sĩ phân tích kết quả, lập phác đồ dinh dưỡng và chế độ tiêm phòng tối ưu.' }
                ]
            },
            {
                id: 3,
                name: 'Tiêm Chủng Vắc-xin Phòng Bệnh Đa Giá Nhập Khẩu (Chó & Mèo)',
                price: 220000,
                duration: '30 phút',
                expert: 'Bác sĩ Thú y chính quy',
                doctor: 'BS Trần Thu Hà',
                category: 'Tiêm chủng & Phòng dịch',
                img: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80',
                desc: 'Tiêm phòng vắc-xin chính hãng (Nobivac, Zoetis) phòng 7 bệnh nguy hiểm trên chó và 4 bệnh trên mèo. Được lưu trữ trong hệ thống tủ lạnh bảo quản chuẩn GSP y tế.',
                description: 'Tiêm phòng vắc-xin chính hãng lưu trữ chuẩn GSP y tế.',
                steps: [
                    { title: 'Khám sàng lọc trước tiêm', desc: 'Đo thân nhiệt và xác nhận thể trạng hoàn toàn khỏe mạnh, không sốt, không ủ bệnh.' },
                    { title: 'Kiểm tra tem mã lô & hạn sử dụng vắc-xin', desc: 'Khách hàng trực tiếp đối chiếu tem niêm phong và hạn sử dụng của lọ thuốc.' },
                    { title: 'Thực hiện tiêm dưới da chuẩn kỹ thuật không đau', desc: 'Sát khuẩn kỹ càng, sử dụng kim tiêm siêu nhỏ hạn chế tối đa cảm giác nhói.' },
                    { title: 'Theo dõi phản ứng sốc phản vệ 15 phút tại chỗ', desc: 'Bé được nghỉ ngơi tại phòng chờ có điều hòa và bác sĩ túc trực quan sát.' },
                    { title: 'Dán tem vào sổ tiêm & cài đặt lịch nhắc hẹn', desc: 'Cấp chứng nhận tiêm phòng và gửi tin nhắn SMS nhắc lịch tái chủng tự động.' }
                ]
            },
            {
                id: 4,
                name: 'Cấp Cứu Thú Y 24/7 & Hồi Sức Tích Cực (ICU)',
                price: 500000,
                duration: 'Phục vụ 24/24h',
                expert: 'Đội ngũ Bác sĩ Cấp cứu & Ngoại khoa thường trực',
                doctor: 'BS Đỗ Hoàng Nam (Đội trưởng ICU)',
                category: 'Cấp cứu 24/7',
                img: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80',
                desc: 'Phòng cấp cứu vô trùng trang bị máy thở oxy cao áp, máy sốc tim, monitor theo dõi huyết động học và đội xe cấp cứu cơ động đón tận nhà bất kể ngày đêm.',
                description: 'Phòng cấp cứu vô trùng trang bị máy thở oxy cao áp 24/7.',
                steps: [
                    { title: 'Tiếp nhận khẩn cấp & phân loại bệnh tình (Triage)', desc: 'Xác định nhanh tình trạng suy hô hấp, xuất huyết, ngộ độc hay đa chấn thương.' },
                    { title: 'Thiết lập đường truyền tĩnh mạch & hỗ trợ oxy', desc: 'Đặt catheter ven ngay lập tức, truyền dịch cân bằng điện giải và thở oxy buồng kín.' },
                    { title: 'Xét nghiệm cấp cứu tại giường & Chụp X-quang/Siêu âm', desc: 'Đọc kết quả khí máu và hình ảnh chẩn đoán trong vòng 5-10 phút.' },
                    { title: 'Phẫu thuật khẩn cấp hoặc điều trị nội trú ICU', desc: 'Chuyển thẳng vào phòng mổ áp lực dương hoặc lồng hồi sức kiểm soát nhiệt ẩm.' },
                    { title: 'Báo cáo diễn tiến sức khỏe liên tục cho gia đình', desc: 'Cập nhật tình trạng qua Zalo/Camera giám sát lồng bệnh 24/24.' }
                ]
            },
            {
                id: 5,
                name: 'Khách Sạn Thú Cưng Pet Hotel Đẳng Cấp 5 Sao (Có Camera 24/7)',
                price: 200000,
                duration: 'Tính theo ngày (24 giờ)',
                expert: 'Quản gia thú cưng & Bác sĩ túc trực',
                doctor: 'KTV Quản gia Pet Hotel',
                category: 'Khách sạn thú cưng',
                img: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=600&q=80',
                desc: 'Phòng lưu trú riêng biệt máy lạnh 24/7, lọc không khí ion âm diệt khuẩn. Khách hàng có tài khoản xem camera riêng của phòng bé bất kỳ lúc nào.',
                description: 'Phòng lưu trú riêng biệt máy lạnh 24/7 kèm camera xem trực tiếp.',
                steps: [
                    { title: 'Tiếp nhận & kiểm tra sức khỏe ban đầu', desc: 'Xác nhận sổ tiêm ngừa, kiểm tra ve rận và lập thực đơn ăn uống theo thói quen của bé.' },
                    { title: 'Nhận phòng VIP riêng biệt khử khuẩn bằng tia UV', desc: 'Trang bị nệm êm ái, khay cát riêng biệt và đồ chơi yêu thích.' },
                    { title: 'Chế độ dinh dưỡng 3 bữa tiêu chuẩn quốc tế', desc: 'Phục vụ hạt cao cấp Royal Canin/Orijen kèm pate tươi nấu trong ngày.' },
                    { title: 'Giờ vận động vui chơi sân vườn 2 lần/ngày', desc: 'Nhân viên dắt bé dạo chơi và tương tác tại khu vận động trong nhà sạch sẽ.' },
                    { title: 'Báo cáo video & nhật ký chăm sóc hàng ngày', desc: 'Gửi clip ăn uống, sinh hoạt và tặng gói tắm sấy trước khi check-out đón về.' }
                ]
            },
            {
                id: 6,
                name: 'Lấy Cao Răng Siêu Âm Không Đau & Đánh Bóng Men Răng',
                price: 320000,
                duration: '60 phút',
                expert: 'Bác sĩ Nha khoa Thú y',
                doctor: 'BS Nha khoa Thú y',
                category: 'Khám & Điều trị',
                img: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80',
                desc: 'Sử dụng đầu rung siêu âm tần số cao bóc tách nhẹ nhàng mảng bám vôi răng dưới nướu, chữa dứt điểm viêm lợi và mùi hôi miệng kéo dài.',
                description: 'Đầu rung siêu âm tần số cao bóc tách mảng bám không đau.',
                steps: [
                    { title: 'Thăm khám mức độ viêm nướu & tiền mê nhẹ', desc: 'Tiền mê an toàn bằng khí mê Isoflurane giúp bé nằm yên không lo sợ.' },
                    { title: 'Lấy mảng bám bằng máy siêu âm nước ấm', desc: 'Làm sạch triệt để từng kẽ răng và túi nha chu mà không mòn men răng.' },
                    { title: 'Đánh bóng bề mặt răng bằng paste nha khoa', desc: 'Tạo bề mặt nhẵn bóng ngăn ngừa thức ăn và vi khuẩn tái bám dính.' },
                    { title: 'Xịt gel kháng khuẩn sinh học thảo dược', desc: 'Làm dịu mô nướu, hỗ trợ tái tạo niêm mạc miệng tổn thương.' },
                    { title: 'Hướng dẫn chủ nuôi chăm sóc răng tại nhà', desc: 'Tư vấn loại gel đánh răng enzym và đồ gặm làm sạch mảng bám.' }
                ]
            },
            {
                id: 7,
                name: 'Tắm Trị Liệu Trị Nấm & Viêm Da Chuyên Sâu Bằng Dược Thảo',
                price: 280000,
                duration: '90 phút',
                expert: 'Kỹ thuật viên Da liễu Thú y',
                doctor: 'KTV Da liễu Thú y',
                category: 'Spa & Làm đẹp',
                img: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=600&q=80',
                desc: 'Phác đồ điều trị dứt điểm các bệnh lý da liễu: nấm Microsporum, viêm da Demodex, viêm nang lông có mủ và vảy gàu ngứa ngáy dữ dội.',
                description: 'Phác đồ điều trị dứt điểm các bệnh lý da liễu và nấm ngứa.',
                steps: [
                    { title: 'Cạo sạch vùng lông tổn thương khu trú', desc: 'Tạo sự thông thoáng để thuốc tiếp xúc trực tiếp vào ổ nấm/vi khuẩn.' },
                    { title: 'Tắm xả bằng nước ấm ion hóa loại bỏ tế bào chết', desc: 'Làm mềm vảy gàu và rửa trôi chất nhờn tích tụ trên bề mặt da.' },
                    { title: 'Ủ dầu tắm dược liệu trị nấm Davis Chlorhexidine 15 phút', desc: 'Hoạt chất thấm sâu tiêu diệt bào tử nấm và vi khuẩn gây mủ.' },
                    { title: 'Ngâm bồn thảo dược phục hồi hàng rào bảo vệ da', desc: 'Chiết xuất yến mạch và tràm trà giúp giảm ngứa tức thì.' },
                    { title: 'Sấy khô bằng lồng sấy gió nhẹ & xịt dưỡng ẩm', desc: 'Không làm khô rát da, phục hồi nang lông mọc lại nhanh chóng.' }
                ]
            },
            {
                id: 8,
                name: 'Phẫu Thuật Triệt Sản Nội Soi An Toàn Vi Phẫu (Chó & Mèo)',
                price: 650000,
                duration: '120 phút',
                expert: 'Bác sĩ Ngoại khoa trưởng ca',
                doctor: 'BS Ngoại khoa Thú y',
                category: 'Phẫu thuật ngoại khoa',
                img: 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80',
                desc: 'Phương pháp vi phẫu đường mổ siêu nhỏ (dưới 1cm) hạn chế đau đớn, không chảy máu, khâu thẩm mỹ chỉ tự tiêu không cần quay lại cắt chỉ.',
                description: 'Phương pháp vi phẫu đường mổ siêu nhỏ chỉ tự tiêu.',
                steps: [
                    { title: 'Xét nghiệm máu kiểm tra đông máu & chức năng gan thận', desc: 'Đảm bảo bé đủ điều kiện chịu mê an toàn tuyệt đối 100%.' },
                    { title: 'Gây mê đa mô thức bằng máy thở Isoflurane hiện đại', desc: 'Theo dõi nhịp tim, nồng độ oxy trong máu liên tục suốt ca mổ.' },
                    { title: 'Tiến hành phẫu thuật trong phòng vô trùng tuyệt đối', desc: 'Dụng cụ tiệt trùng Autoclave, bác sĩ phẫu thuật mặc áo vô khuẩn.' },
                    { title: 'Khâu chỉ thẩm mỹ tự tiêu giấu vết mổ', desc: 'Không để lại vết sẹo lồi, thú cưng không cần đeo vòng chống liếm quá lâu.' },
                    { title: 'Hồi tỉnh tại phòng chăm sóc hậu phẫu êm dịu', desc: 'Tiêm thuốc giảm đau 24h và cấp thuốc uống chống viêm tại nhà.' }
                ]
            },
            {
                id: 9,
                name: 'Siêu Âm Màu 4D & Chụp X-Quang Kỹ Thuật Số (DR) Tận Nơi',
                price: 300000,
                duration: '40 phút',
                expert: 'Bác sĩ Chẩn đoán Hình ảnh Thú y',
                doctor: 'BS CĐHA Thú y',
                category: 'Chẩn đoán hình ảnh',
                img: 'https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80',
                desc: 'Máy siêu âm Doppler màu hiện đại chẩn đoán thai kỳ, sỏi bàng quang, khối u và máy X-quang kỹ thuật số liều phóng xạ thấp kiểm tra xương khớp.',
                description: 'Máy siêu âm Doppler màu hiện đại và X-quang kỹ thuật số.',
                steps: [
                    { title: 'Chuẩn bị tư thế và cạo lông vùng kiểm tra', desc: 'Vệ sinh da và bôi gel siêu âm chuyên dụng không gây kích ứng.' },
                    { title: 'Quét siêu âm Doppler đánh giá chi tiết các tạng', desc: 'Đo kích thước tim thận, kiểm tra tuần hoàn máu và đếm số lượng thai nhi.' },
                    { title: 'Chụp phim X-quang các tư thế chuẩn', desc: 'Đánh giá dị vật đường tiêu hóa, gãy xương hoặc thoát vị đĩa đệm.' },
                    { title: 'Hội chẩn hình ảnh với bác sĩ chuyên khoa', desc: 'Phân tích bất thường và lập bản báo cáo chẩn đoán hình ảnh chuẩn xác.' },
                    { title: 'Trả file ảnh kỹ thuật số chất lượng cao qua App', desc: 'Khách hàng có thể lưu trữ và xem lại hình ảnh trên hồ sơ bệnh án điện tử.' }
                ]
            },
            {
                id: 10,
                name: 'Xét Nghiệm Máu Tổng Quát 18 Chỉ Số & Test Nhanh Bệnh Truyền Nhiễm',
                price: 380000,
                duration: '30 - 45 phút lấy kết quả ngay',
                expert: 'Kỹ thuật viên Xét nghiệm Y khoa',
                doctor: 'KTV Xét nghiệm Thú y',
                category: 'Xét nghiệm chẩn đoán',
                img: 'https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=600&q=80',
                desc: 'Hệ thống máy xét nghiệm huyết học và sinh hóa tự động IDEXX (Mỹ) cho kết quả chính xác 99.9% chỉ trong 15 phút, phát hiện sớm suy thận, viêm tụy, Care, Parvo, FIP.',
                description: 'Máy xét nghiệm sinh hóa tự động IDEXX Mỹ lấy kết quả sau 15p.',
                steps: [
                    { title: 'Lấy mẫu máu tĩnh mạch êm ái', desc: 'Kỹ thuật viên thao tác chuẩn xác, lượng máu lấy rất nhỏ không gây mệt cho bé.' },
                    { title: 'Chạy máy huyết học tự động 18 chỉ số (CBC)', desc: 'Kiểm tra bạch cầu (nhiễm trùng), hồng cầu (thiếu máu), tiểu cầu.' },
                    { title: 'Đo sinh hóa chức năng gan, thận và đường huyết', desc: 'Đánh giá nồng độ men gan ALT, Creatinine, BUN, Glucose máu.' },
                    { title: 'Thực hiện test nhanh kháng nguyên bệnh truyền nhiễm', desc: 'Kit test chuyên biệt phát hiện virus Parvo, Care, Giảm bạch cầu (FPV).' },
                    { title: 'Bác sĩ giải thích tường tận từng chỉ số bất thường', desc: 'Đưa ra lời khuyên dinh dưỡng hoặc phác đồ can thiệp kịp thời.' }
                ]
            },
            {
                id: 11,
                name: 'Vật Lý Trị Liệu & Phục Hồi Chức Năng Cột Sống - Khớp',
                price: 300000,
                duration: '60 phút',
                expert: 'Bác sĩ Phục hồi Chức năng Thú y',
                doctor: 'BS PHCN Thú y',
                category: 'Phục hồi chức năng',
                img: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                desc: 'Liệu trình vật lý trị liệu laser giảm đau sâu, thủy trị liệu bồn bơi nước ấm và châm cứu phục hồi phản xạ thần kinh cho các bé bị liệt 2 chân sau, thoái hóa khớp.',
                description: 'Laser giảm đau sâu, thủy trị liệu và châm cứu phục hồi khớp.',
                steps: [
                    { title: 'Đánh giá thang điểm đau & mức độ vận động', desc: 'Kiểm tra phản xạ cơ bắp, độ co duỗi khớp và mức độ tổn thương thần kinh.' },
                    { title: 'Chiếu tia Laser cường độ thấp giảm viêm sâu', desc: 'Tăng cường tuần hoàn máu nuôi dưỡng mô sụn và cắt đứt cơn đau cơ.' },
                    { title: 'Thủy trị liệu (Hydrotherapy) trên máy chạy bộ dưới nước', desc: 'Nước nâng đỡ trọng lượng cơ thể giúp bé tập bước đi mà không áp lực lên xương.' },
                    { title: 'Xoa bóp nắn chỉnh cơ và kéo giãn nhẹ nhàng', desc: 'Chống teo cơ, duy trì độ dẻo dai của gân dây chằng.' },
                    { title: 'Bài tập phục hồi tại nhà cùng chủ nuôi', desc: 'Hướng dẫn các động tác mát-xa và dụng cụ hỗ trợ xe lăn nếu cần thiết.' }
                ]
            },
            {
                id: 12,
                name: 'Đưa Đón Thú Cưng Khám Bệnh & Spa Tận Cửa Bằng Xe Chuyên Dụng (Pet Taxi)',
                price: 150000,
                duration: 'Theo lịch hẹn khách đặt',
                expert: 'Tài xế chuyên trách & Nhân viên an toàn thú cưng',
                doctor: 'Đội xe Pet Taxi Cơ Động',
                category: 'Dịch vụ tiện ích',
                img: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=600&q=80',
                desc: 'Xe ô tô cứu thương & đưa đón thú cưng chuyên dụng, khoang xe rộng rãi có điều hòa mát lạnh, lồng vận chuyển êm ái, dây an toàn chuyên dụng và tài xế am hiểu tâm lý động vật.',
                description: 'Xe ô tô chuyên dụng đưa đón thú cưng tận nhà an toàn chu đáo.',
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

        // Lịch hẹn Admin
        appointments: [
            {
                id: 'APT-1089',
                customerName: 'Nguyễn Phương Thảo',
                customerPhone: '0988 123 456',
                petName: 'Bơ (Butter)',
                petType: 'Cún Corgi',
                serviceName: 'Gói Spa & Grooming Cắt Tỉa Lông Toàn Diện',
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
                serviceName: 'Khám Sức Khỏe Tổng Quát & Tầm Soát',
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
                serviceName: 'Tiêm Chủng Vắc-xin 7 Bệnh Nhập Khẩu',
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
                serviceName: 'Lấy Cao Răng Siêu Âm Không Đau',
                date: '2026-10-20',
                time: '16:00',
                branch: 'Chi nhánh Quận 7',
                status: 'Đã đặt hẹn',
                notes: 'Bé khó tính khi đụng vào miệng, cần tiền mê nhẹ.'
            }
        ],

        // Đơn hàng Admin
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
                items: 'Cát Đậu Nành Cature 6L (x2), Balo Phi Thuyền',
                total: 820000,
                totalAmount: 820000,
                paymentMethod: 'COD khi nhận hàng',
                status: 'Hoàn thành',
                branch: 'BT'
            }
        ],

        // Khách hàng Admin
        customers: [
            {
                id: 1,
                name: 'Nguyễn Phương Thảo',
                phone: '0988 123 456',
                email: 'phuongthao.petcare@gmail.com',
                tier: 'Thành viên Vàng',
                petCount: 3,
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
                spent: 4500000,
                totalSpent: 4500000,
                points: 1250,
                avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=300&q=80',
                createdAt: '05/06/2025'
            }
        ],

        // Doanh thu chi tiết
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

        // Forms
        newPetData: {
            name: '',
            type: 'Chó',
            breed: '',
            gender: 'Đực',
            age: '',
            weight: '',
            avatar: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80',
            allergies: ''
        },

        newProdForm: {
            sku: '',
            name: '',
            brand: '',
            price: null,
            stockHN: 20,
            stockQ7: 20,
            stockBT: 10,
            category: 'Thức ăn khô',
            img: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
            desc: ''
        },

        restockForm: {
            productId: '',
            branch: 'HN',
            quantity: 50,
            costPrice: null,
            supplier: '',
            notes: ''
        },

        checkoutForm: {
            name: 'Nguyễn Phương Thảo',
            phone: '0988 123 456',
            address: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
            paymentMethod: 'vietqr'
        },

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

        get filteredProducts() {
            return this.products.filter(p => {
                const cat = (this.filterCategory || 'all');
                const matchCat = cat === 'all' || p.category.toLowerCase().includes(cat.toLowerCase());
                const query = (this.searchQuery || this.productSearchQuery || '').toLowerCase();
                const matchSearch = !query || p.name.toLowerCase().includes(query) || p.brand.toLowerCase().includes(query);
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
                const matchLow = !this.showLowStockOnly || p.stock <= 30;
                return matchQ && matchLow;
            });
        },

        get filteredAdminPets() {
            return this.pets.filter(p => {
                const q = (this.petSearchQuery || '').toLowerCase();
                return !q || p.name.toLowerCase().includes(q) || p.breed.toLowerCase().includes(q) || (p.chipId && p.chipId.includes(q));
            });
        },

        get filteredAdminCustomers() {
            return this.customers.filter(c => {
                const q = (this.customerSearchQuery || '').toLowerCase();
                return !q || c.name.toLowerCase().includes(q) || c.phone.includes(q) || c.email.toLowerCase().includes(q);
            });
        },

        get totalRevenueFiltered() {
            if (this.adminTimeFilter === 'today') return 12450000;
            if (this.adminTimeFilter === '7days') return 89200000;
            if (this.adminTimeFilter === 'month') return 345000000;
            if (this.adminTimeFilter === 'quarter') return 980000000;
            return 1245000000;
        },

        get pendingOrdersCount() {
            return this.orders.filter(o => o.status !== 'Hoàn thành').length;
        },

        get inProgressAppointmentsCount() {
            return this.appointments.filter(a => a.status === 'Đang tiếp khách' || a.status === 'Đã đặt hẹn').length;
        },

        get lowStockCount() {
            return this.products.filter(p => p.stock <= 30).length;
        },

        get urgentTasksCount() {
            return this.pendingOrdersCount + this.inProgressAppointmentsCount;
        },

        // Helper label formatters
        formatCurrency(amount) {
            if (!amount && amount !== 0) return '0 đ';
            return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(amount);
        },

        formatMoney(amount) {
            return this.formatCurrency(amount);
        },

        getBranchLabel(code) {
            if (code === 'HN') return 'Cầu Giấy';
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
            return status || 'Đã ghi nhận';
        },

        // Khởi tạo app
        initApp() {
            console.log('PetCare360 Unified SuperApp Initialized!');
            if (window.lucide) {
                window.lucide.createIcons();
            }
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
        },

        applyTimeFilter(period) {
            this.adminTimeFilter = period;
            alert('Đã cập nhật bộ lọc thời gian: ' + this.getTimeFilterLabel(period));
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
            this.activeCustomerTab = 'services';
        },

        openOrderDetail(order) {
            this.selectedOrder = order;
            this.orderDrawerOpen = true;
        },

        // Thao tác giỏ hàng & Đặt lịch
        addToCart(product, qty = 1) {
            const existing = this.cart.find(item => item.id === product.id && !item.isService);
            if (existing) {
                existing.qty += qty;
            } else {
                this.cart.push({
                    id: product.id,
                    name: product.name,
                    price: product.price,
                    img: product.img || product.image,
                    qty: qty,
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
                cartService = {
                    id: service.id,
                    name: service.name,
                    price: service.price,
                    img: service.img || service.image,
                    qty: 1,
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

            const incompleteService = this.cart.find(item => item.isService && (!item.bookingDate || !item.selectedPet));
            if (incompleteService) {
                alert('⚠️ NHẮC NHỞ: Bạn chưa điền đầy đủ thông tin "Đặt lịch chi tiết" (chọn thú cưng và ngày hẹn) cho dịch vụ: "' + incompleteService.name + '". Vui lòng hoàn tất thông tin để phòng khám chuẩn bị buồng chăm sóc chu đáo trước khi thanh toán!');
                this.openBookingModalForService(incompleteService);
                return;
            }

            this.showCartDrawer = false;
            this.cartOpen = false;
            this.showCheckoutModal = true;
        },

        confirmOrderAndPay() {
            const orderId = 'ORD-' + Math.floor(1000 + Math.random() * 9000);
            const serviceItems = this.cart.filter(item => item.isService);

            // Đồng bộ sang Admin Lịch hẹn
            serviceItems.forEach(serv => {
                this.appointments.unshift({
                    id: 'APT-' + Math.floor(1000 + Math.random() * 9000),
                    customerName: this.checkoutForm.name,
                    customerPhone: this.checkoutForm.phone,
                    petName: serv.selectedPet,
                    petType: 'Thú cưng khách chọn',
                    serviceName: serv.name,
                    date: serv.bookingDate,
                    time: serv.bookingTime || '09:00',
                    branch: serv.bookingBranch || 'Chi nhánh Quận 7',
                    status: 'Đã đặt hẹn',
                    notes: serv.bookingNotes || 'Khách hàng đặt trực tuyến qua SuperApp.'
                });
            });

            // Tạo bản ghi đơn hàng
            this.orders.unshift({
                id: orderId,
                customer: this.checkoutForm.name,
                date: new Date().toISOString().split('T')[0],
                items: this.cart.map(i => i.name + (i.isService ? ' (Dịch vụ)' : ' (x' + i.qty + ')')).join(', '),
                total: this.cartTotal,
                totalAmount: this.cartTotal,
                paymentMethod: this.checkoutForm.paymentMethod === 'vietqr' ? 'Chuyển khoản VietQR' : (this.checkoutForm.paymentMethod === 'momo' ? 'Ví MoMo' : 'COD'),
                status: 'Đã thanh toán',
                branch: 'Q7'
            });

            const earnedPoints = Math.floor(this.cartTotal / 10000);
            this.customerProfile.points += earnedPoints;

            this.cart = [];
            this.showCheckoutModal = false;

            alert('🎉 CHÚC MỪNG QUÝ KHÁCH! Đơn hàng & Lịch hẹn ' + orderId + ' đã được thanh toán thành công! Bạn được cộng thêm ' + earnedPoints + ' điểm thành viên.');
        },

        // Quản lý thú cưng & Hồ sơ
        saveNewPet() {
            if (!this.newPetData.name) {
                alert('Vui lòng nhập tên cho bé!');
                return;
            }
            const newId = this.pets.length + 1;
            const newPet = {
                id: newId,
                name: this.newPetData.name,
                type: this.newPetData.type,
                breed: this.newPetData.breed || 'Chưa cập nhật',
                gender: this.newPetData.gender,
                age: this.newPetData.age || 'Mới nhận nuôi',
                weight: this.newPetData.weight || '3.0 kg',
                chipId: '900118000' + Math.floor(100000 + Math.random() * 900000),
                chip: '900118000' + Math.floor(100000 + Math.random() * 900000),
                avatar: this.newPetData.avatar || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80',
                image: this.newPetData.avatar || 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80',
                allergies: this.newPetData.allergies || 'Không ghi nhận dị ứng.',
                vaccines: [
                    { name: 'Khám lâm sàng ban đầu', date: new Date().toLocaleDateString('vi-VN'), doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: 'Hẹn 1 tháng sau', status: 'Đã hoàn thành' }
                ],
                medicalHistory: [
                    { date: new Date().toLocaleDateString('vi-VN'), diagnosis: 'Tạo hồ sơ thú cưng mới trên hệ thống PetCare360', treatment: 'Khám sàng lọc và tư vấn dinh dưỡng ban đầu', notes: 'Bé ngoan, thể trạng ổn định.' }
                ]
            };
            this.pets.push(newPet);
            this.customerProfile.petCount = this.pets.length;
            this.showAddPetModal = false;
            this.addPetModalOpen = false;
            alert('Đã thêm hồ sơ bé ' + this.newPetData.name + ' vào tài khoản của bạn thành công!');
        },

        deletePet(id) {
            if (confirm('Bạn có chắc muốn xóa hồ sơ thú cưng này không?')) {
                this.pets = this.pets.filter(p => p.id !== id);
                this.customerProfile.petCount = this.pets.length;
                alert('Đã xóa hồ sơ bé thành công.');
            }
        },

        setDefaultPet(id) {
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
            const totalStock = (parseInt(this.newProdForm.stockHN) || 0) + (parseInt(this.newProdForm.stockQ7) || 0) + (parseInt(this.newProdForm.stockBT) || 0);
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
                stock: totalStock || 50,
                stockHN: parseInt(this.newProdForm.stockHN) || 20,
                stockQ7: parseInt(this.newProdForm.stockQ7) || 20,
                stockBT: parseInt(this.newProdForm.stockBT) || 10,
                category: this.newProdForm.category,
                categoryAdmin: this.newProdForm.category,
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
                prod.stock += addQty;
                if (this.restockForm.branch === 'HN') prod.stockHN = (prod.stockHN || 0) + addQty;
                else if (this.restockForm.branch === 'Q7') prod.stockQ7 = (prod.stockQ7 || 0) + addQty;
                else prod.stockBT = (prod.stockBT || 0) + addQty;

                this.showRestockModal = false;
                this.restockModalOpen = false;
                alert('Đã nhập thêm ' + addQty + ' sản phẩm "' + prod.name + '" vào chi nhánh thành công! Tồn kho mới: ' + prod.stock);
            }
        },

        // Chat
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

        // Các hành động phụ
        setOrderTypeFilter(type) {
            this.currentOrderTypeTab = type;
        },

        showToast(msg) {
            alert(msg);
        },

        toggleDarkMode() {
            alert('Hệ thống đang chuyển đổi chế độ hiển thị!');
        },

        refreshChart() {
            alert('Đã cập nhật số liệu biểu đồ phân tích thời gian thực!');
        },

        scrollToUrgentTasks() {
            alert('Đang cuộn đến các nhiệm vụ khẩn cấp!');
        }
    };
}
</script>
'''
