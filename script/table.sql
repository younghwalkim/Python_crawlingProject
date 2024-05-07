-- ũ�Ѹ� ������ ����� ���̺� ���� ��ũ��Ʈ
-- table.sql

-- ���̹� ��ȭ�� ���� ���� ������ ũ�Ѹ�
-- ���̺�� : movie
-- ���̽��� Movie Class �ʵ��� ���̺� �÷��� ��ġ��Ŵ. => �ʵ���� '__' ������
-- rank : pk, ������ �÷��� not null
-- �÷� comment �� ����

DROP TABLE MOVIE CASCADE  CONSTRAINTS;

CREATE TABLE MOVIE (
    RANK NUMBER CONSTRAINT PK_MOVIE PRIMARY KEY,
    TITLE VARCHAR2(100) NOT NULL,
    STAR_POINT NUMBER(7,2) NOT NULL, 
    RELEASE_DATE VARCHAR2(20),
    GENRE VARCHAR2(30),
    LINK VARCHAR2(2000)    
);

COMMENT ON MOVIE.RANK IS '�󿵼���';
COMMENT ON MOVIE.TITLE IS '��ȭ����';
COMMENT ON MOVIE.STAR_POINT IS '��ȭ����';
COMMENT ON MOVIE.RELEASE_DATE IS '������';
COMMENT ON MOVIE.GENRE IS '�帣';
COMMENT ON MOVIE.LINK IS '�������� url';

COMMIT;
