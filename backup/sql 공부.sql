SELECT * FROM stock.kosdaq;  # select 컬럼명 from 테이블명

select 회사명, 업종, 주요제품, 지역 from stock.kosdaq; # select 컬럼명 from 테이블명

select * from stock.kosdaq
where 회사명 = '신성델타테크';   # where 컬럼명 = 내가 찾는 값

select * from stock.kosdaq
order by 상장일 limit 10;   # Order by 정렬, limit 몇 개 가져올지

select * from stock.kosdaq
order by 상장일 desc limit 10;   # desc 를 사용해서 내림차순 정렬alter

-- 반도체 제조업인 회사의  회사명,종목 코드 가져오기


